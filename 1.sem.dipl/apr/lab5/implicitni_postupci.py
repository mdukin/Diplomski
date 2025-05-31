import numpy as np
from Matrica import Matrica

class implicitan_postupak:
    def __init__(self,A, T = 0.01,tmax=10):
        self.A = A
        self.T = T
        self.tmax = tmax

    def next(self,x):
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

class Obrnuti_Euler(implicitan_postupak):
    def __init__(self, A, T=0.01, tmax=10, B=Matrica(np.zeros((2, 2))), r=lambda t:0):
        super().__init__(A, T, tmax)
        U = Matrica(np.eye(2))
        P = U - A * T
        self.P = P._inverse()

        self.Q = P * T * B
        self.B = B
        self.r = r

    def next(self, x, tk):
        return self.P * x  + self.Q * self.r(tk)
    
    
    def next_korektor(self, xk, xk_pred, tk, tk_pred):
        return xk +  ( self.A * xk_pred  + self.B * self.r(tk_pred) ) * self.T
    

class Trapez(implicitan_postupak):
    def __init__(self, A, T=0.01, tmax=10, B=Matrica(np.zeros((2, 2))), r=lambda t:0):
        super().__init__(A, T, tmax)
        U = Matrica(np.eye(2))
        R1 = U - A * (T/2)
        R2 = U + A * (T/2)

        self.R = R1._inverse() * R2

        self.S = R1._inverse()* (T/2) * B
        self.r = r

        self.B = B


    def next(self, x,tk):
        tk_pred =tk + self.T
        return self.R * x  + self.S * self.r(tk) + self.S * self.r(tk_pred)
    
    def next_korektor(self, xk, xk_pred, tk, tk_pred):
        return xk + ( self.A * xk + self.B * self.r(tk) + self.A * xk_pred + self.B * self.r(tk_pred) ) * (self.T/2)
     