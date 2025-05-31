import numpy as np
from ogr import ogr_nejednakosti, ogr_ekspl

def calc_Xc(tocke_simplexa,n,h):
        n_simplexa = len(tocke_simplexa)
        Xc = np.zeros(n)
        for j in range(n_simplexa):
            if j != h: Xc += ( tocke_simplexa[j] / (n_simplexa-1) )
        return Xc

def box_postupak(X0:np.array, ogr_eksplicitna:ogr_ekspl, ogr_nejednakosti:ogr_nejednakosti, f, alfa = 1.3, epsilon = 10**-6):

    if not (ogr_eksplicitna.zadovoljava(X0) and ogr_nejednakosti.zadovoljava(X0)) :
        return " X0 ne zadovoljava ogr"
    
    #init simplex
    Xc = X0.copy()
    n = len(Xc)
    Xd = ogr_eksplicitna.Xd; Xg = ogr_eksplicitna.Xg
    tocke_simplexa = []
    tocke_simplexa.append(X0)
    for _ in range(2*n):
        Xt = np.empty(n)
        for i in range(n):
            R = np.random.uniform(0, 1)
            Xt[i] = Xd[i]+ R * (Xg[i] - Xd[i])
        while not ogr_nejednakosti.zadovoljava(Xt):
            Xt = 0.5 * (Xt + Xc)
        tocke_simplexa.append(Xt)
        Xc = np.zeros(n)
        for j in range(len(tocke_simplexa)):
            Xc += ( tocke_simplexa[j] / (len(tocke_simplexa)) )
    
    n_simplexa = len(tocke_simplexa)
    f_values = np.array([f(xt) for xt in tocke_simplexa])

    #box
    for _ in range(10000):  

        h = np.argmax(f_values)
        f_values[h] = -np.inf
        h2 = np.argmax(f_values)

        Xc = calc_Xc(tocke_simplexa,n,h)
        Xc_value = f(Xc)

        Xr = (1+alfa)*Xc - alfa*tocke_simplexa[h] 
        for i in range(n):
            if Xr[i] < Xd[i]:
                Xr[i] = Xd[i]
            elif Xr[i] > Xg[i]:
                Xr[i] = Xg[i]

        while not ogr_nejednakosti.zadovoljava(Xr):
            Xr = 0.5 * ( Xr + Xc)
        if f(Xr) > f_values[h2]:
            Xr = 0.5 * ( Xr + Xc)
        tocke_simplexa[h] = Xr

        f_values = np.array([f(xt) for xt in tocke_simplexa])
        uvj_stop =np.sqrt(np.sum([ (f_values[i]-Xc_value)**2 for i in range(n_simplexa) ]) / n_simplexa) 
        if uvj_stop <= epsilon :
            break

    return Xc