import pyopencl as cl
import numpy as np
import time

PI = np.pi

# Create OpenCL context and queue
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# Define OpenCL program source
kernel = """
__kernel void doSingleJob(
                       const int n,
                       __global double *rezultati) 
{

    int gid = get_global_id(0);
    int G = get_global_size(0);

	double h, sum, x;
	int i ;

	h   = 1.0 / (double) n;

    for (i = gid+1; i <= n; i += G)     // i=1 -> n
    {	x = h * ((double)i - 0.5);
        x= 4.0 / (1.0 + x*x);

        rezultati[i-1] = h*x;
    }

}
"""

# Create program and build
program = cl.Program(context, kernel).build()

N = 2 ** 25

rezultati = np.zeros(N, dtype=np.float64)  


mf = cl.mem_flags
rezultati_buf = cl.Buffer(context, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=rezultati)



global_size = (N,)  # Total number of work-items
local_size = (32,)  # Number of work-items per work-group

# Measure the parallel part (executing the kernel)
start_par = time.time()
program.doSingleJob(queue, global_size, local_size, np.int32(N), rezultati_buf)
queue.finish()  # Ensure the kernel execution is finished
end_par = time.time()

# Copy result from the buffer
cl.enqueue_copy(queue, rezultati, rezultati_buf).wait()

# Calculate elapsed times
time_par = end_par - start_par

print(f"Parallel part time: {time_par:.6f} seconds")

mypi1 = rezultati.sum()

print(f"pi: {mypi1}")

start = time.time()

rs = np.zeros(N, dtype=np.float64)  
sum = np.zeros(1, dtype=np.float64)  
for i in range(1,N+1):
    x = (i-0.5)/N
    x = 1 / (1+ x**2)
    rs[i-1] = x*4/N
    sum[0] += x*4/N
mypi2 = rs.sum()

end = time.time()

print(f"Sequential execution time: {end - start:.6f} seconds")
print(f"pi: {mypi2}")

print(mypi1 - PI)
print(mypi2 - PI)
print(sum-PI)
print(mypi1-mypi2)


