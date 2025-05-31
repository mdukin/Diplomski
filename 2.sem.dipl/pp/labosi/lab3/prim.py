import pyopencl as cl
import numpy as np
import time

# Create OpenCL context and queue
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# Define OpenCL program source
program_source = """
__kernel void vector_add(__global const float *a,
                         __global const float *b,
                         __global float *c) {
    int gid = get_global_id(0);
    c[gid] = a[gid] + b[gid];
}
"""

# Create program and build
program = cl.Program(context, program_source).build()

# Define input arrays and output array
a = np.random.rand(1024).astype(np.float32)
b = np.random.rand(1024).astype(np.float32)
c = np.empty_like(a)

# Measure the sequential part (creating buffers and copying data to the GPU)
start_seq = time.time()
mf = cl.mem_flags
a_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
c_buf = cl.Buffer(context, mf.WRITE_ONLY, c.nbytes)
end_seq = time.time()

# Define the number of threads (work-items)
global_size = (1024,)  # Total number of work-items
local_size = (64,)     # Number of work-items per work-group

# Measure the parallel part (executing the kernel)
start_par = time.time()
program.vector_add(queue, global_size, local_size, a_buf, b_buf, c_buf)
queue.finish()  # Ensure the kernel execution is finished
end_par = time.time()

# Copy result from the buffer
cl.enqueue_copy(queue, c, c_buf).wait()

# Calculate elapsed times
time_seq = end_seq - start_seq
time_par = end_par - start_par

print(f"Sequential part time: {time_seq:.6f} seconds")
print(f"Parallel part time: {time_par:.6f} seconds")

start = time.time()
for i in range(len(c)):  
    c[i] = a[i] + b[i]
end = time.time()

print(f" time: {(end-start):.6f} seconds")

num_compute_units = device.get_info(cl.device_info.MAX_COMPUTE_UNITS)

print(num_compute_units)
