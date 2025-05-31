import numpy as np

def boundarypsi(psi, m, n, b, h, w):

    for i in range(b + 1, b + w):
        psi[i * (m + 2) + 0] = float(i - b)

    for i in range(b + w, m + 1):
        psi[i * (m + 2) + 0] = float(w)


    for j in range(1, h + 1):
        psi[(m + 1) * (m + 2) + j] = float(w)

    for j in range(h + 1, h + w):
        psi[(m + 1) * (m + 2) + j] = float(w - j + h)
