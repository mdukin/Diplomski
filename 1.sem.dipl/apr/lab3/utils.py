from Matrica import Matrica
import math
import autograd.numpy as np

k = 0.5*(math.sqrt(5)-1)

def min_na_pravcu(x,vektor,F):
                lambda_function = F.trans_to_1_dim(x,vektor)
                l,r = unimodalni(0, lambda_function)
                opt_lambda = zlatni_rez(l,r,f=lambda_function)
                F.counter += lambda_function.counter
                x_ret =  x + opt_lambda * vektor
                if F.F(x_ret) < F.F(x) :
                     return x_ret
                return x + 0.01 * np.ones_like(x)


def solve_lup(A:Matrica,b:Matrica):
    
    lu,P = A.LUP()
    b = P*b
    lup = P*lu
    y = lup._supst_unaprijed(b)
    x = lup._supst_unatrag(y)
    return x

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
