import numpy as np
import time
import sys
from boundary import boundarypsi
from jacobi import jacobistep, deltasq
from cfdio import gettime
import paralelization

def copy_back(psi,psitmp,m,n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            psi[i*(m+2)+j] = psitmp[i*(m+2)+j]

def main():
    printfreq = 100  # output frequency
    tolerance = 0.0   # tolerance for convergence. <=0 means do not check
    irrotational = 1

    # main arrays
    psi = None
    psitmp = None

    # command line arguments
    scalefactor = 0
    numiter = 0

    # simulation sizes
    bbase = 10
    hbase = 15
    wbase = 5
    mbase = 32
    nbase = 32

    m = n = b = h = w = 0
    iter = 0
    error = bnorm = 0.0

    # check command line parameters and parse them

    scalefactor = 64
    numiter = 1000
    if not tolerance > 0:
        print("Scale Factor = %i, iterations = %i" % (scalefactor, numiter))
    else:
        print("Scale Factor = %i, iterations = %i, tolerance= %g" % (scalefactor, numiter, tolerance))

    print("Irrotational flow")

    # Calculate b, h & w and m & n
    b = bbase * scalefactor
    h = hbase * scalefactor
    w = wbase * scalefactor
    m = mbase * scalefactor
    n = nbase * scalefactor

    print("Running CFD on %d x %d grid in serial" % (m, n))

    psi = np.zeros((m+2) * (n+2), dtype=np.float64)
    psitmp = np.zeros_like(psi)


    psi.fill(0.0)
    boundarypsi(psi, m, n, b, h, w)


    bnorm=0.0

    for i in range(0, m+2):
        for j in range(0, n+2):
            bnorm += psi[i*(m+2)+j]*psi[i*(m+2)+j]
    
    bnorm = np.sqrt(bnorm)

    print("\nStarting main loop...\n")
    tstart = gettime()

    paralelization.init_program(m,n)

    for iter in range(1, numiter + 1):

        paralelization.jacobistep_parallel(psitmp, psi, m, n)
        #jacobistep(psitmp, psi, m, n)

        if tolerance > 0 or iter == numiter:
            #error = paralelization.deltasq_parallel(psitmp, psi, m, n)
            error = deltasq(psitmp, psi, m, n)
            error = np.sqrt(error)
            error = error / bnorm

        if tolerance > 0:
            if error < tolerance:
                print("Converged on iteration %d" % iter)
                break

        # copy back

        paralelization.copy_parallel(psi,psitmp,m,n)
        #copy_back(psi,psitmp,m,n)


        if iter % printfreq == 0:
            if tolerance <= 0:
                print("Completed iteration %d" % iter)
            else:
                print("Completed iteration %d, error = %g" % (iter, error))

    if iter > numiter:
        iter = numiter

    tstop = gettime()

    ttot = tstop - tstart
    titer = ttot / float(iter)

    print("\n... finished\n")
    print("After %d iterations, the error is %g" % (iter, error))
    print("Time for %d iterations was %g seconds" % (iter, ttot))
    print("Each iteration took %g seconds" % titer)



if __name__ == "__main__":
    main()
