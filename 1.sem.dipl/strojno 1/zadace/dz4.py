import numpy as np

X = np.array([
    [9.5,-0.7,-2.8],
    [8.8,-0.8,-3.2],
    [6.5,-0.2,-0.8],
    [2.3,0.3,1.2],
    [2.2,0,0],
    [3.6,0.3,1.2]
])

u_mle = np.zeros(3)
for xi in X:
    u_mle += xi
u_mle = u_mle/6

print(u_mle)

E_mle = np.zeros((3, 3))

for xi in X:
    E_mle += np.outer( (xi-u_mle), (xi-u_mle)  )

E_mle =E_mle / 6
print(E_mle)

det = np.linalg.det(E_mle)

print(det)

sigma1 = np.sqrt(E_mle[0][0] ) 
sigma2 = np.sqrt(E_mle[1][1] )
sigma3 = np.sqrt(E_mle[2][2] )

p12 = E_mle[0][1] / (sigma1*sigma2)
p13 = E_mle[0][2] / (sigma1*sigma3)
p23 = E_mle[1][2] / (sigma2*sigma3)

print(p12)
print(p13)
print(p23)

X = np.delete(X, 2, axis=1)
print(X)

u_mle = np.zeros(2)
for xi in X:
    u_mle += xi
u_mle = u_mle/6

print(u_mle)

E_mle = np.zeros((2, 2))

for xi in X:
    E_mle += np.outer( (xi-u_mle), (xi-u_mle)  )

E_mle =E_mle / 6
print(E_mle)

det = np.linalg.det(E_mle)

print(det)

x = np.array([-2,1])
mu = u_mle
sigma = E_mle
n = len(x)
constant_term =1 / ((2 * np.pi) ** (n / 2) * np.linalg.det(sigma) ** 0.5)
exponent_term = -0.5 * np.dot(np.dot((x - mu).T, np.linalg.inv(sigma)), x - mu)

p = constant_term * np.exp(exponent_term)

print(p)