import numpy as np
from Matrica import Matrica
import matplotlib.pyplot as plt
from  exsplicitni_postupci import exsplicitan_postupak
from implicitni_postupci import implicitan_postupak


def Runge_Kutta_4(A, x0, T = 0.01,tmax=10,B=Matrica(np.zeros((2, 2))), r=lambda t:0):
      
        x1_list=[]
        x2_list=[]
        t_values = []
        Xk = x0
        tk=0

        while tk <= tmax:
        
            x1_list.append(Xk.get(0,0))
            x2_list.append(Xk.get(1,0))
            t_values.append(tk)

            m1 = A * Xk + B * r(tk)
            m2 = A * Xk + A *(T/2)*m1 + B * r(tk+T/2)
            m3 = A * Xk + A *(T/2)*m2 + B * r(tk+T/2) 
            m4 = A * Xk + A *(T/2)*m3 + B * r(tk+T)

            Xk =   Xk +( m1 + (m2*2) + (m3*2) + m4  )* (T/6) 

            tk += T

        return t_values, x1_list,x2_list

def pred_korekt(x0:Matrica, predikator :exsplicitan_postupak, korektor: implicitan_postupak, n=1,T = 0.01,tmax=10 ):

        x1_list=[]
        x2_list=[]
        t_values = []

        Xk = x0
        tk = 0

        while tk <= tmax : 
            x1_list.append(Xk.get(0,0))
            x2_list.append(Xk.get(1,0))
            t_values.append(tk)

            Xk_pred = predikator.next(Xk, tk)
            for _ in range(n):
                Xk_pred = korektor.next_korektor(Xk, Xk_pred, tk, tk+T)
            Xk = Xk_pred

            tk+=T

        return t_values, x1_list,x2_list
