import autograd.numpy as np
import math
class funkcija:
    def __init__(self, F) -> None:
        self.F = F
        self.counter = 0
    
    def get_func(self, X):
        return self.F(X)
    
    def call(self,X):
        self.counter += 1
        return self.F(X)
    
    def trans_to_1_dim(self,X,v):
        return funkcija(lambda a: self.F(X + a * v) )
    
    def get_counter(self):
        count = self.counter
        self.counter = 0
        return count

f1 = funkcija(lambda X: 100 * np.power(X[1] - np.power(X[0], 2), 2) + np.power(1 - X[0], 2))

f2 = funkcija(lambda X: (X[0]-4)**2 + 4*(X[1]-2)**2 )

f3 = funkcija(lambda X: (X[0]-2)**2 + (X[1]+3)**2 )

f4 = funkcija(lambda X: 0.25*X[0]**4 - X[0]**2 + 2*X[0] + (X[1]-1)**2 )

f5 = funkcija(lambda X: ( X[1]**2+X[0]**2 - 1)**2 + (X[1]-X[0]**2)**2 )


G1 =  lambda X : np.array([ 10*(X[1]-X[0]**2) , (1-X[0]) ])

G2 = lambda X : np.array([(X[0]-4) ,  2*(X[1]-2) ] ) 

G3 = lambda X: np.array([ (X[0]-2) , (X[1]+3)])

G4 = lambda X : np.array([ (0.5*X[0]**2-2) ,(X[0]+1), (X[1]-1) ])

G5 = lambda X : np.array([ X[1]**2+X[0]**2 - 1, (X[1]-X[0]**2) ])


x0_1 = np.array([-1.9,2],dtype = np.float64 )
x0_2 = np.array([0.1,0.3],dtype = np.float64 )
x0_3 = np.array([0,0],dtype = np.float64 )

tocke = [ [1,3], [2,4], [3,4], [5,5], [6,6], [7,8] ]

G6 = lambda X : np.array([
         X[0]* math.e ** ( X[1] * 1) + X[2] - 3,
         X[0]* math.e ** ( X[1] * 2)+ X[2] - 4,
         X[0]* math.e ** ( X[1] * 3) + X[2] - 4,
         X[0]* math.e ** ( X[1] * 5)+ X[2] - 5,
         X[0]* math.e ** ( X[1] * 6)+ X[2] - 6,
         X[0]* math.e ** ( X[1] * 7) + X[2] - 8
            ])

f6 = funkcija(lambda X:    
       (X[0]* math.e ** ( X[1] * 1) + X[2] - 3)**2 +
       (X[0]* math.e ** ( X[1] * 2)+ X[2] - 4)**2 +
       (X[0]* math.e ** ( X[1] * 3) + X[2] - 4)**2 +
       (X[0]* math.e ** ( X[1] * 5)+ X[2] - 5)**2 +
       (X[0]* math.e ** ( X[1] * 6)+ X[2] - 6)**2 +
       (X[0]* math.e ** ( X[1] * 7) + X[2] - 8)**2  )