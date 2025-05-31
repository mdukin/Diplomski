import numpy as np

def istrazi(Xp, dx, f):
    x = np.copy(Xp)
    for i in range(len(Xp)):
        P = f(x)
        x[i] += dx
        N = f(x)
        if N > P:
            x[i] -= 2 * dx
            N = f(x)
            if N > P:
                x[i] += dx
    return x

def hooke_jeeves(X0, f, epsilon = 10e-6,dx = 0.5):

    Xp , Xb= np.copy(X0), np.copy(X0)

    Xb_value = f(Xb)
    while dx> epsilon:
        Xn = istrazi(Xp, dx,f)
        Xn_value = f(Xn)

        if Xn_value < Xb_value:
            Xp = 2*Xn - Xb
            Xb = np.copy(Xn) ; Xb_value = Xn_value
        else:
            dx /= 2
            Xp = np.copy(Xb)
    return Xb

