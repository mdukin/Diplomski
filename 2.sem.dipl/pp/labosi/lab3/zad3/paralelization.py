import pyopencl as cl
import numpy as np

# Inicijalizacija OpenCL
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# OpenCL kernel kod
kernel = """
__kernel void jacobistep(__global double* psinew,
                         __global const double* psi,
                         int m,
                         int n) 
{
    int i = get_global_id(0) + 1;
    int j = get_global_id(1) + 1;

    if (i <= m && j <= n) {
        int idx = i * (m + 2) + j;
        psinew[idx] = 0.25 * (psi[(i - 1) * (m + 2) + j] +
                              psi[(i + 1) * (m + 2) + j] +
                              psi[i * (m + 2) + j - 1] +
                              psi[i * (m + 2) + j + 1]);
    }
}

__kernel void deltasq(__global const double* newarr,
                      __global const double* oldarr,
                      __global double* result, 
                      int m,
                      int n) {
    int i = get_global_id(0) + 1;
    int j = get_global_id(1) + 1;

    if (i <= m && j <= n) {
        int idx = i * (m + 2) + j;
        double tmp = newarr[idx] - oldarr[idx];
        result[idx] = tmp * tmp;
    }
}

__kernel void copy(__global double* dst,
                   __global const double* src, 
                   int m, 
                   int n) {
    int i = get_global_id(0) + 1;
    int j = get_global_id(1) + 1;

    if (i <= m && j <= n) {
        int idx = i * (m + 2) + j;
        dst[idx] = src[idx];
    }
}
"""

program, global_size, local_size, mf = None, None, None, None

def init_program(m, n):
    global program, global_size, mf, local_size
    program = cl.Program(context, kernel).build()
    mf = cl.mem_flags
    global_size = (m, n) 
    local_size = None

def jacobistep_parallel(psitmp, psi, m, n):
    psi_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=psi)
    psitmp_buf = cl.Buffer(context, mf.WRITE_ONLY, psitmp.nbytes)

    program.jacobistep(queue, global_size, None, psitmp_buf, psi_buf, np.int32(m), np.int32(n))
    cl.enqueue_copy(queue, psitmp, psitmp_buf).wait()

def deltasq_parallel(psitmp, psi, m, n):
    rezultati = np.zeros((m + 2) * (n + 2), dtype=np.float64)

    psitmp_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=psitmp)
    psi_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=psi)
    rezultati_buf = cl.Buffer(context, mf.WRITE_ONLY, rezultati.nbytes)

    program.deltasq(queue, global_size, None, psitmp_buf, psi_buf, rezultati_buf, np.int32(m), np.int32(n))
    cl.enqueue_copy(queue, rezultati, rezultati_buf).wait()

    dsq = np.sum(rezultati)
    return dsq

def copy_parallel(psi, psitmp, m, n):
    psi_buf = cl.Buffer(context, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=psi)
    psitmp_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=psitmp)

    program.copy(queue, global_size, None, psi_buf, psitmp_buf, np.int32(m), np.int32(n))
    cl.enqueue_copy(queue, psi, psi_buf).wait()