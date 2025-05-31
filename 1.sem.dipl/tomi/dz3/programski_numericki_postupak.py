import numpy as np
from itertools import product

U = np.array([[2,8,0,2],
             [2,0,0,0],
             [3,6,5,2],
             [4,5,8,9]])
n = len(U)
m= len(U[0])

precision=50 # sto vece to preciznije, ali i sporije ocito
range = np.linspace(0,1,precision)

x = np.zeros(n)
V = -np.inf

for combination in product(range, repeat=n):
    if sum(combination) != 1:
        continue
    
    X = np.array(combination)

    new_min = np.min(np.matmul(X,U))

    if new_min > V:
        V = new_min
        x = X

ys = []
for combination in product(range, repeat=m):
    if sum(combination) != 1:
        continue
    
    Y = np.array(combination).transpose()

    max = np.max(np.matmul(U,Y))
    if max == V:
        ys.append(Y)

print("V:",V)
print("x prob:",x)
print("ys probs:",ys)

