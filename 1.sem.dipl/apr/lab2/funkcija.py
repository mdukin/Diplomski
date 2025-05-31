import numpy as np
class funkcija:
    def __init__(self, F) -> None:
        self.F = F
        self.dim = len(F.__code__.co_varnames)
        self.counter = 0

    def call(self,X):
        self.counter += 1
        return self.F(X)
    
    def trans_to_1_dim(self,X,v):
        return funkcija(lambda a: self.F(X + a * v) )
    
    def reset_counter(self):
        self.counter = 0


f1 = funkcija( lambda X: 100*(X[1]-X[0])**2 + (1-X[0])**2 )

f2 = funkcija(lambda X: (X[0]-4)**2 + 4*(X[1]-2)**2 )

f3 = funkcija(lambda X: sum((X[i] - (i+1)) ** 2 for i in range(X.size)))

f4 = funkcija(lambda X: np.abs((X[0]-X[1]) * (X[0]+X[1])) + np.sqrt(X[0]**2 + X[1]**2) ) 

f6 = funkcija(lambda X: 0.5 + (np.sin(np.sqrt(sum( X[i] ** 2 for i in range(X.size))))**2 - 0.5) /
                             ( 1+0.001 * sum( X[i] ** 2 for i in range(X.size)) )**2 )

x0_1 = np.array([-1.9,2],dtype = np.float64 )
x0_2 = np.array([0.1,0.3],dtype = np.float64 )
x0_3 = np.array([0,0,0,0,0],dtype = np.float64 )
x0_4 = np.array([5.1,1.1],dtype = np.float64 )
x0_6 = np.array([0,0,0],dtype = np.float64 )

