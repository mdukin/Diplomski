import algoritmi
import numpy as np
from random import randint 
from funkcija import f1,f2,f3,f4,f6, funkcija
from funkcija import x0_1,x0_2,x0_3,x0_4,x0_6

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def ispis_1_dim(x0, f):
    l,r = algoritmi.unimodalni(x0, f = f)
    x = algoritmi.zlatni_rez(l,r,f = f )
    print(colors.YELLOW + "\n          ZLATNI REZ" + colors.ENDC)
    print("x=",x, "f_called:",f.counter) ; f.reset_counter()

def ispis_vise_dim(x0, f):

    x = algoritmi.koordinatno_trazenje(x0,F=f) 

    print(colors.YELLOW + "\n         KOORDINATNO TREAŽENJE." + colors.ENDC)    
    print("x=",x, "F_called: ", f.counter) ; f.reset_counter()

    x = algoritmi.hooke_jeeves(x0,F = f, dx=3.5)

    print(colors.YELLOW + "\n         HOOKE_JEEVES." + colors.ENDC)
    print("x=",x, "F_called: ", f.counter) ; f.reset_counter()

    x = algoritmi.simpleks(x0,F = f) 

    print(colors.YELLOW + "\n         SIMPLEX." + colors.ENDC)
    print("x=",x, "F_called: ", f.counter) ; f.reset_counter()


def prvi():
    print(colors.RED + "\n -----------ZADATAK1--------------- \n" + colors.ENDC)
    f = funkcija(lambda x: (x-3)**2)

    x0s = [10,30,50]

    for xi in x0s :
        x0 = np.array([xi],dtype = np.float64 )
        print(colors.OKGREEN +"\nPOC TOCKA: ",x0," MIN: [3]"  + colors.ENDC)

        ispis_1_dim(x0,f)
        ispis_vise_dim(x0,f)


def drugi():
   print(colors.RED + "\n -----------ZADATAK2--------------- \n" + colors.ENDC)

   print(colors.OKGREEN +"FUNKCIJA 1, POC TOCKA: " + str(x0_1) + " MIN: [1,1]"+ colors.ENDC)
   ispis_vise_dim(x0_1, f1)

   print(colors.OKGREEN+"\nFUNKCIJA 2, POC TOCKA: " + str(x0_2) + " MIN: [4,2]"+ colors.ENDC)
   ispis_vise_dim(x0_2, f2)

   print(colors.OKGREEN+"\nFUNKCIJA 3, POC TOCKA: " + str(x0_3) + " MIN: [1,2,3,...n]"+ colors.ENDC)
   ispis_vise_dim(x0_3, f3)

   print(colors.OKGREEN+"\nFUNKCIJA 4, POC TOCKA: " + str(x0_4) + " MIN: [0,0]"+ colors.ENDC)
   ispis_vise_dim(x0_4, f4)

def treci():
    print(colors.RED + "\n -----------ZADATAK3--------------- \n" + colors.ENDC)
    print(colors.OKGREEN +"FUNKCIJA 4, POC TOCKA: [5,5] MIN: [1,1]"+ colors.ENDC)

    X0 = np.array([5,5],dtype = np.float64)
    x = algoritmi.simpleks(X0,F = f4)

    print(colors.YELLOW + "\n         SIMPLEX." + colors.ENDC)
    print(x, "F_called: ", f4.counter) ; f4.reset_counter()

    x = algoritmi.hooke_jeeves(X0, F= f4)

    print(colors.YELLOW + "\n         HOOKE_JEEVES." + colors.ENDC)
    print(x, "F_called ", f4.counter) ; f4.reset_counter()

def cetvrti():
    pomaci = [1,5,10,15,20] 
    x0s = [0.5,20]

    print(colors.RED + "\n -----------ZADATAK4--------------- \n" + colors.ENDC)
    print(colors.YELLOW + "        SIMPLEX." + colors.ENDC)
    
    for xi in x0s:
        X0 = np.array([xi,xi],dtype = np.float64)
        print(colors.OKGREEN + "\nPOC_TOCKA=" + str(X0)+ colors.ENDC)
        for pomak in pomaci:
            x = algoritmi.simpleks(X0,pomak = pomak, F = f1)

            print(colors.OKBLUE+ "\nPOMAK: " + str(pomak)+ colors.ENDC)
            print("x=",x, "F_called: ", f1.counter) ; f1.reset_counter()


def peti():
    print(colors.RED + "\n -----------ZADATAK5--------------- \n" + colors.ENDC)
    print(colors.OKGREEN + "FUNKCIJA 6 MIN: 0-VEKTOR" + colors.ENDC)

    n = 10000
    found_min = 0
    for _ in range(n):
        X_rand = np.array([randint(-50,50), randint(-50,50)])
        x = algoritmi.hooke_jeeves(X_rand, f6, epsilon=10e-4)
        if f6.call(x) < 10e-4: found_min += 1

    print(colors.YELLOW + "        HOOKE_JEEVES." + colors.ENDC)
    print("Za",n, "slučajnih x0 minimum pronađen " , found_min , " puta.")
    print("Vjerojatnost pronalazenja minimuma: ", 100 * found_min/n, "%")
    print("Prosječan broj poziva F za svaku slučajnu točku: ", f6.counter/n)

#sprvi()
drugi()
#treci()
#cetvrti()
#peti()
