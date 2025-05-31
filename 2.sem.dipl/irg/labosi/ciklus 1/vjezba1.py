import numpy as np


def zad1():
    a = np.array([2,3,-4])
    b = np.array([-1,4,-1])
    c = np.array([2,2,4])

    v1 = a+b
    s = np.dot(v1,b)
    v2 = np.cross(v1, c)

    v3 = v2/np.linalg.norm(v2)
    v4 = -v2

    A =  np.array([[1,2,3],
                   [2,1,3],
                   [4,5,1]])
    
    B =  np.array([[-1,2,-3],
                   [5,-2,7],
                   [-4,-1,3]])
    
    M1 = A+B

    M2 = np.dot(A, np.transpose(B))
   
    M3 = np.dot(A, np.linalg.inv(B))

    V = np.dot(np.array([1,2,3,1]),
               np.array([[1,0,0,0],
                         [0,2,0,0],
                         [0,0,1,0],
                         [2,3,3,1]]))

    print("v1: ", v1)
    print("s: ", s)
    print("v2: ", v2)
    print("v3: ",v3)
    print("v4: ",v4)
    print("M1:")
    print(M1)
    print("M2:")
    print(M2)
    print("M3:")
    print(M3)
    print("V: ", V)

def zad2():

    j1 = list(float(i)
               for i in input("1.jedn: ").split(' '))
    j2 = list(float(i)
               for i in input("2.jedn: ").split(' '))
    j3 = list(float(i)
               for i in input("3.jedn: ").split(' '))
    
    X = np.array([[j1[0], j1[1], j1[2]],
                  [j2[0], j2[1], j2[2]],
                  [j3[0], j3[1], j3[2]]])
    T = np.array([j1[3],j2[3],j3[3]])

    t = np.dot(np.linalg.inv(X), T)

    print(t)

def zad3():
    A = list(float(i)
               for i in input("A: ").split(' '))
    B = list(float(i)
               for i in input("B: ").split(' '))
    C = list(float(i)
               for i in input("C: ").split(' '))
    
    T = list(float(i)
               for i in input("T: ").split(' '))
    
    X = np.array([[A[0], B[0], C[0]],
                  [A[1], B[1], C[1]],
                  [A[2], B[2], C[2]] ])

    t = np.dot(np.linalg.inv(X), T)

    print(t)


zadatak_num = input("zadatak? (1,2,3)")
print()

if zadatak_num == "1":
    zad1()
if zadatak_num == "2":
    zad2()
if zadatak_num == "3":
    zad3()

a = np.array([1,2,3])
b = np.array([2,3,4])

