import numpy as np

def jacobistep(psinew, psi, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            psinew[i * (m + 2) + j] = 0.25 * (psi[(i - 1) * (m + 2) + j] + psi[(i + 1) * (m + 2) + j] + psi[i * (m + 2) + j - 1] + psi[i * (m + 2) + j + 1])

def deltasq(newarr, oldarr, m, n):
    dsq = 0.0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tmp = newarr[i * (m + 2) + j] - oldarr[i * (m + 2) + j]
            dsq += tmp * tmp
    return dsq