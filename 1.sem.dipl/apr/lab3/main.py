
from algoritmi import gradijentni_spust, gauss_newthon, newthon_raphson
from funkcije import f1,f2,f3,f4,f5,f6
from funkcije import x0_1,x0_2,x0_3,G1,G2,G3,G4,G5,G6
import autograd.numpy as np
import matplotlib.pyplot as plt
import math

def print_rez(xmin, grad_call, F_call, F_val):
    print("x: ", xmin , " g_call: ", grad_call, " F_call", F_call, "F(x):",F_val)

class Colors:
    RED = '\033[91m'
    END = '\033[0m'

def zad1():
    print(f"\n{Colors.RED}Zadatak 1{Colors.END}")
    xmin, grad_call, F_call, F_val = gradijentni_spust(x0=x0_3, F=f3)
    print_rez(xmin, grad_call, F_call, F_val)

def zad2():
    print(f"\n{Colors.RED}Zadatak 2{Colors.END}")
    print("\ngradijentni spust (f1,f2)(lin_prezrazivanje)")
    xmin, grad_call, F_call, F_val = gradijentni_spust(x0=x0_1, F=f1, linijsko_pretrazivanje=True)
    print_rez(xmin, grad_call, F_call, F_val)
    xmin, grad_call, F_call, F_val = gradijentni_spust(x0=x0_2, F=f2, linijsko_pretrazivanje=True)
    print_rez(xmin, grad_call, F_call, F_val)

    print("\nnewthon_raphson (f1,f2)(lin_prezrazivanje)")
    xmin, grad_call, F_call, F_val = newthon_raphson(x0=x0_1, F=f1, linijsko_pretrazivanje=True)
    print_rez(xmin, grad_call, F_call, F_val)
    xmin, grad_call, F_call, F_val = newthon_raphson(x0=x0_2, F=f2, linijsko_pretrazivanje=True)
    print_rez(xmin, grad_call, F_call, F_val)

def zad3():
    print(f"\n{Colors.RED}Zadatak 3{Colors.END}")
    print("\nbez linijskog pretrazivanja (f4) (3,3) ( 1,2)")
    xmin, grad_call, F_call, F_val = newthon_raphson(x0=np.array([3, 3], dtype=np.float64), F=f4, linijsko_pretrazivanje=False)
    print_rez(xmin, grad_call, F_call, F_val)
    xmin, grad_call, F_call, F_val = newthon_raphson(x0=np.array([1, 2], dtype=np.float64), F=f4, linijsko_pretrazivanje=False)
    print_rez(xmin, grad_call, F_call, F_val)

    print("\nsa linijskim pretrazivanjem (f4) (3,3) ( 1,2)")
    xmin, grad_call, F_call, F_val = newthon_raphson(x0=np.array([3, 3], dtype=np.float64), F=f4, linijsko_pretrazivanje=True)
    print_rez(xmin, grad_call, F_call, F_val)
    xmin, grad_call, F_call, F_val = newthon_raphson(x0=np.array([1, 2], dtype=np.float64), F=f4, linijsko_pretrazivanje=True)
    print_rez(xmin, grad_call, F_call, F_val)

def zad4():
    print(f"\n{Colors.RED}Zadatak 4{Colors.END}")
    xmin, grad_call, F_call, F_val = gauss_newthon(x0=x0_1, F=f1, G=G1)
    print_rez(xmin, grad_call, F_call, F_val)

def zad5():
    print(f"\n{Colors.RED}Zadatak 5{Colors.END}")
    x0s = [np.array([-2, 2], dtype=np.float64), np.array([2, 2], dtype=np.float64), np.array([2, -2], dtype=np.float64)]
    for x0 in x0s:
        print("\nx0:", x0)
        xmin, grad_call, F_call, F_val = gauss_newthon(x0=x0, F=f5, G=G5)
        print_rez(xmin, grad_call, F_call, F_val)

def zad6():
    print(f"\n{Colors.RED}Zadatak 6{Colors.END}")
    x0 = np.array([1, 1, 1], dtype=np.float64)
    xmin, grad_call, F_call, F_val = gauss_newthon(x0=x0, F=f6, G=G6)
    print_rez(xmin, grad_call, F_call, F_val)

    Mt = lambda t: xmin[0] * math.e ** (xmin[1] * t) + xmin[2]

    t_values = np.linspace(0, 8, 1000)
    Mt_values = Mt(t_values)
    tocke = [[1, 3], [2, 4], [3, 4], [5, 5], [6, 6], [7, 8]]
    tocke_x, tocke_y = zip(*tocke)

    plt.scatter(tocke_x, tocke_y, color='red', label='Points')
    plt.plot(t_values, Mt_values, label='M(t)')
    plt.xlabel('t')
    plt.ylabel('M(t)')

    plt.grid(True)
    plt.show()

#zad1()
#zad2()
#zad3()
#zad4()
#zad5()
#zad6()

