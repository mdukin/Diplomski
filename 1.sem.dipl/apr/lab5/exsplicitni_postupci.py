import numpy as np
from Matrica import Matrica

class exsplicitan_postupak:
    def __init__(self, A,T ,tmax):
        self.A = A
        self.T = T
        self.tmax = tmax

    def next(self,x,t):
        raise NotImplementedError("")
    
    def postupak(self, x0):
        x1_list=[]
        x2_list=[]
        t_values = []

        Xk = x0
        tk = 0
        while tk <= self.tmax:

            x1_list.append(Xk.get(0,0))
            x2_list.append(Xk.get(1,0))
            t_values.append(tk)

            Xk = self.next(Xk, tk)
            tk += self.T

        return t_values, x1_list,x2_list

class Euler(exsplicitan_postupak):
    def __init__(self, A, T=0.01, tmax=10, B=Matrica(np.zeros((2, 2))), r=lambda t:0):
        super().__init__(A,T, tmax)

        U = Matrica(np.eye(2))
        self.M = U +  A * T

        self.N = B * T

        self.r = r

    def next(self, xk,tk):
        return self.M * xk + self.N * self.r(tk)
    