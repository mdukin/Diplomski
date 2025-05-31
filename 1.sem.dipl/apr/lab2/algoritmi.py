import math
import numpy as np
from funkcija import funkcija

k = 0.5*(math.sqrt(5)-1)

def zlatni_rez(a, b, f, e= 10e-6, ispis = False):
    c = b - k * (b - a)
    d = a + k * (b - a)
    fc = f.call(c)
    fd = f.call(d)
    while  (b - a) > e :
        if ispis is True:
            print(a, c, d, b)
        if fc < fd :
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = f.call(c)
        else : 
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = f.call(d)
    
    return (a+b) /2

def unimodalni(tocka, f, h=1):

    l = tocka - h
    r = tocka + h
    m = tocka ; step = h* 2

    fm = f.call(tocka)
    fl = f.call(l)
    fr = f.call(r)
    if fm < fr and fm < fl:
        return l,r
    elif fm > fr:
        while fm >fr :
            l = m
            m = r
            fm = fr
            r = tocka + h * step; step *= 2
            fr = f.call(r)
    else:
        while fm > fl:
            r = m
            m = l
            fm = fl
            l = tocka - h * step; step *= 2
            fl = f.call(l)
    return l,r

def koordinatno_trazenje(X0,F, epsilon=10e-6, max_iter = 1000, ispis = False ):
    
    iter = 0
    n = X0.size
    eps = np.array([epsilon for i in range(n)])
    X = np.copy(X0)
    e = np.eye(n)
    Xs = np.copy(X) + 2*eps

    while np.all(np.abs(X - Xs) > eps) and iter < max_iter:
        iter += 1
        Xs = np.copy(X)
        if ispis == True:
            print("X: ", X, "f(X): ", F.F(X))
        for i in range(n):
            lambda_function = F.trans_to_1_dim(Xs,e[i])
            l,r = unimodalni(Xs[i], lambda_function)
            opt_lambda = zlatni_rez(l,r,f=lambda_function)
            F.counter += lambda_function.counter
            X[i] += opt_lambda # e[i] = 1

    return X

def simpleks(X0, F, pomak = 1 ,alfa=1, beta=0.5, gama=2,sigma = 0.5, epsilon = 10e-6 , max_iter = 1000, ispis = False):

    iter = 0
    X = np.array(X0)
    N = X0.size
    n = N+ 1 # broj tocaka, dim+1 
    e = np.eye(n-1)

    for i in range(n-1):
        X = np.vstack((X, X0 + e[i] * pomak))

    f_values = np.array([F.call(xi) for xi in X])

    while True :
        iter += 1
        l = np.argmin(f_values)
        h = np.argmax(f_values)

        Xc = np.zeros(N)
        for j in range(n):
            if j != h: Xc += ( X[j] / N )

        Xc_value = F.call(Xc)

        if ispis is True:
            print("Xc: ", Xc ," F(Xc): ", Xc_value )

        if np.sqrt(np.sum([ (f_values[i]-Xc_value)**2 for i in range(n) ]) / n) <= epsilon or iter >= max_iter:
            break
        
        Xr = (1+alfa) * Xc - alfa * X[h]      
        Xr_value = F.call(Xr)
        if Xr_value < f_values[l]:
            Xe = (1-gama)*Xc - gama*Xr # - na predavanju, + u skripti
            Xe_value = F.call(Xe)
            if Xe_value < f_values[l]:
                X[h] =Xe ; f_values[h] = Xe_value
            else:
                X[h] = Xr ; f_values[h] = Xr_value
        else:  
            if all(Xr_value > f_values[i] for i in range(n) if i != h) :
                if Xr_value < f_values[h]:
                    X[h] = Xr ; f_values[h] = Xr_value
                Xk = (1-beta)*Xc + beta * X[h]
                Xk_value = F.call(Xk)
                if Xk_value < f_values[h]:
                    X[h] = Xk ; f_values[h] = Xk_value
                else:
                    for j in range(n):
                        if j != l:
                            X[j] += X[l] * sigma
                    f_values = np.array([F.call(xi) for xi in X])
            else:
                X[h] = Xr; f_values[h] = Xr_value
    return Xc

def istrazi(Xp, dx, F):
    x = np.copy(Xp)
    for i in range(len(Xp)):
        P = F.call(x)
        x[i] += dx
        N = F.call(x)
        if N > P:
            x[i] -= 2 * dx
            N = F.call(x)
            if N > P:
                x[i] += dx
    return x

def hooke_jeeves(X0, F, epsilon = 10e-6,dx = 1,ispis = False):

    Xp , Xb= np.copy(X0), np.copy(X0)
    n = X0.size

    Xb_value = F.call(Xb)
    while dx> epsilon:
        Xn = istrazi(Xp, dx,F)
        Xn_value = F.call(Xn)
        if ispis is True:
            print("Xb:",Xb, Xb_value , "Xp:", Xp, F.F(Xp),  "Xn:" ,Xn, Xn_value)
        if Xn_value < Xb_value:
            Xp = 2*Xn - Xb
            Xb = np.copy(Xn) ; Xb_value = Xn_value
        else:
            dx /= 2
            Xp = np.copy(Xb)
    return Xb
