import pyopencl as cl
import numpy as np
import time

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

kernel = """
__kernel void isPrime(__global const int *polje,
                       __global int *sum,
                       const int N) {
    int gid = get_global_id(0);

    int G = get_global_size(0);
    
    while(gid < N){

        int num = polje[gid];
        int is_prime = 1; // Assume the number is prime

        if (num <= 1) {
            is_prime = 0; // Numbers less than or equal to 1 are not prime
        } else {
            for (int i = 2; i <= (int)sqrt((float)num); i++) {
                if (num % i == 0) {
                    is_prime = 0;
                    break;
                }
            }
        }
        
        if (is_prime) {
            (*sum)++;
            //atomic_inc(sum);
        }

        gid += G ;
    }
    
}
"""

program = cl.Program(context, kernel).build()

N = 2 ** 20

polje = np.arange(N).astype(np.int32)
sum = np.zeros(1, dtype=np.int32)  #


mf = cl.mem_flags
polje_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=polje)
sum_buf = cl.Buffer(context, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=sum)


global_size = (1024,)  # Total number of work-items
local_size = (64,)  # Number of work-items per work-group

start_par = time.time()
program.isPrime(queue, global_size, local_size, polje_buf, sum_buf, np.int32(N))
queue.finish()  # Ensure the kernel execution is finished
end_par = time.time()

cl.enqueue_copy(queue, sum, sum_buf).wait()

time_par = end_par - start_par

print(f"Parallel part time: {time_par:.6f} seconds")

print(f"Sum of primes: {sum}")

start = time.time()

sum_primes = 0
for num in polje:
    if is_prime(num):
        sum_primes += 1

end = time.time()

print(f"Sequential execution time: {end - start:.6f} seconds")
print(f"Sum of primes: {sum_primes}")

print("N:" , N)
