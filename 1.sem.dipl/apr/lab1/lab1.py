from Matrica import Matrica

def solve(A,b):
    y = A._supst_unaprijed(b)
    x = A._supst_unatrag(y)
    return x

def zad1():
    A = Matrica.readFromFile("files/2A")
    B = A / 2.33333333
    B = B * 2.33333333
    print(A)
    print(B)

    print("/ 2.33333333 ; * 2.33333333\n")
    print("matrice jednake? ", A == B)
    print("matrice jednake? eps = 10e-9 ",A._equal_precise(B) )

def zad2():
    A = Matrica.readFromFile("files/2A")
    b = Matrica.readFromFile("files/2b")

    print("A");print(A)
    print("b");print(b)
    try:
        lu = A.LU()
        print("LU");print(lu)
        x = solve(lu, b)
    except Exception as e:
        print("\033[91mError:"+str(e)+ "\033[0m")


    lu,P = A.LUP()
    print("LUP") ;print(P * lu)
    x = solve(P*lu,P*b)

    print(x)

def zad3():

    A = Matrica.readFromFile("files/3A")
    b = Matrica([[2],[2],[2]])

    print("A");print(A)
    print("b");print(b)
    try:
        lu = A.LU()
        print("LU") ;print(lu)
        x = solve(lu, b)
    except Exception as e:
        print("\033[91mError:"+str(e)+ "\033[0m")

    try:
        lu, P = A.LUP()
        print("LUP");print(P *lu)
        x = solve(P * lu, P * b)
        print("x");print(x)
        print("A*x")
        print(A*x)
    except Exception as e:
        print("\033[91mError:"+str(e)+ "\033[0m")


def zad4():
   A = Matrica.readFromFile("files/4A")
   b = Matrica.readFromFile("files/4b")

   print("A");print(A)
   print("b");print(b)
   lu = A.LU()
   print("LU"); print(lu)
   x = solve(lu,b)
   print("x"); print(x)

   lup,P = A.LUP()
   print("LUP") ; print(P*lup)
   x = solve(P*lup,P*b)
   print("x") ; print(x)

def zad5():
    A = Matrica.readFromFile("files/5A")
    b = Matrica.readFromFile("files/5b")

    print("A"); print(A)
    print("b"); print(b)

    #zbog nula na dijagonali lup, kod lu dijenje s 0
    try:
        lu = A.LU()
        print("LU"); print(lu)
        x = solve(lu, b)
    except Exception as e:
        print("\033[91mError:"+str(e)+ "\033[0m")

    lup, P = A.LUP()
    print("LUP"); print(P*lup)
    x = solve(P * lup, P * b)
    print("x") ; print(x)
    print("A * x")
    print(A * x)

def zad6():
    A = Matrica.readFromFile("files/6A")
    b = Matrica.readFromFile("files/6b")

    print("A") ;print(A)
    print("b"); print(b)

    try:
        lu = A.LU()
        print("LU"); print(lu)
        x = solve(lu,b)
        print("x") ;print(x)
    except Exception as e :
        print("\033[91mError:" + str(e) + "\033[0m")
    try:
        lup, P = A.LUP()
        print("LUP"); print(P*lup)
        x = solve(P * lup, P * b)
        print("x") ; print(x)
    except Exception as e:
        print("\033[91mError:" + str(e) + "\033[0m")

    T =Matrica([
        [1e-9, 0, 0],
        [0, 1, 0],
        [0, 0, 1e10]
    ])
    print("T"); print(T)

    A = T * A
    b = T * b
    print(A,b)

    print("LU")
    print(A.LU())
    x = solve(A.LU(),b)
    print("x")
    print(x)

def zad7():
    A = Matrica.readFromFile("files/7A")
    print("A"); print(A)
    try:
        print(A._inverse() )

        print(A._inverse() * A)
    except Exception as e:
        print("\033[91mError:" + str(e) + "\033[0m")

def zad8():
    A = Matrica.readFromFile("files/8A")
    print("A"); print(A)
    A_inv = A._inverse()
    print("A inverz"); print(A_inv)
    print("A * inv A"); print(A * A_inv)

def zad9():
    A = Matrica.readFromFile("files/9A")
    print("A"); print(A)
    print("det = " ,A.determinanta())
def zad10():

    A = Matrica.readFromFile("files/10A")
    print("A"); print(A)
    print("det = " ,A.determinanta())

print("ZADATAK 1\n")
zad1()
print()
print("ZADATAK 2\n")
zad2()
print()
print("ZADATAK 3\n")
zad3()
print()
print("ZADATAK 4\n")
zad4()
print()
print("ZADATAK 5\n")
zad5()
print()
print("ZADATAK 6\n")
zad6()
print()
print("ZADATAK 7\n")
zad7()
print()
print("ZADATAK 8\n")
zad8()
print()
print("ZADATAK 9\n")
zad9()
print()
print("ZADATAK 10\n")
zad10()

A = Matrica([[0,1,2],
             [2,0,3],
             [3,5,1]])
b = Matrica([[6],[9],[3]])

lup,p = A.LUP()

print(p*lup)
x = solve(p*lup,p*b)


print(x)