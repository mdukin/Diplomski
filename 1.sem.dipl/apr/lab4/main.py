import numpy as np
from ogr import ogr_nejednakosti, ogr_ekspl, ogr_jednakosti
from box import box_postupak
from prob_bez_ogr import trans_u_prob_bez_ogr

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

f1 = lambda X: 100*(X[1]-X[0]**2)**2 + (1-X[0])**2 
f2 = lambda X: (X[0]-4)**2 + 4*(X[1]-2)**2 
f4 = lambda X: (X[0]-3)**2 + X[1]**2 

x0_1 = np.array([-1.9,2],dtype = np.float64 )
x0_2 = np.array([0.1,0.3],dtype = np.float64 )
x0_3 = np.array([0,1],dtype = np.float64 )
x0_4 = np.array([0,0],dtype = np.float64 )
x0_5 = np.array([5,5],dtype = np.float64 )

ogr_nejedn = ogr_nejednakosti([lambda X: X[1] - X[0] , lambda X: 2-X[0] ])
ogr_eksp = ogr_ekspl(np.array([-100,-100]), Xg = np.array([100,100]))
ogr_jedn = ogr_jednakosti(None)

ogr_nejedn2 = ogr_nejednakosti([lambda X: 3-X[0]-X[1], lambda X: 3 + 1.5*X[0]-X[1] ] )
ogr_jedn2 = ogr_jednakosti([lambda X: X[1]-1])

def prvi():
    print(colors.OKBLUE + "\n -----------ZADATAK1--------------- \n" + colors.ENDC)

    print(colors.OKGREEN +"(BOX) FUNKCIJA 1, POC TOCKA: [-1.9,2] MIN: [1,1] " + colors.ENDC)
    Xmin = box_postupak(x0_1 ,ogr_eksp, ogr_nejedn , f1)
    print(Xmin, f1(Xmin))

    print(colors.OKGREEN +"\n(BOX) FUNKCIJA 2, POC TOCKA: [0.1,0.3] MIN: [4,2]"+ colors.ENDC)
    Xmin = box_postupak(x0_2 ,ogr_eksp, ogr_nejedn , f2)
    print(Xmin, f2(Xmin))

def drugi():
    print(colors.OKBLUE + "\n -----------ZADATAK2--------------- \n" + colors.ENDC)

    print(colors.OKGREEN +"(MIX) FUNKCIJA 1, POC TOCKA: [-1.9,2] MIN: [4,2]"+ colors.ENDC)
    Xmin = trans_u_prob_bez_ogr(x0_1, f1, ogr_nejedn, ogr_jedn)
    print(Xmin, f1(Xmin))

    print(colors.OKGREEN +"\n(MIX) FUNKCIJA 1, POC TOCKA: [0,1] MIN: [4,2]"+ colors.ENDC)
    Xmin = trans_u_prob_bez_ogr(x0_3, f1, ogr_nejedn, ogr_jedn)
    print(Xmin, f1(Xmin))

    print(colors.OKGREEN +"\n(MIX) FUNKCIJA 2, POC TOCKA: [0.1,0.3] MIN: [4,2]"+ colors.ENDC)
    Xmin = trans_u_prob_bez_ogr(x0_2, f2, ogr_nejedn, ogr_jedn)
    print(Xmin, f2(Xmin))

def treci():
    print(colors.OKBLUE + "\n -----------ZADATAK3--------------- \n" + colors.ENDC)

    print(colors.OKGREEN +"(MIX) FUNKCIJA 4, POC TOCKA: [0,0] MIN: [3,0]"+ colors.ENDC)
    Xmin = trans_u_prob_bez_ogr(x0_4, f4, ogr_nejedn2, ogr_jedn2)
    print(Xmin, f4(Xmin))

    print(colors.OKGREEN +"\n(MIX) FUNKCIJA 4, POC TOCKA: [5,5] MIN: [3,0]"+ colors.ENDC)
    Xmin = trans_u_prob_bez_ogr(x0_5, f4, ogr_nejedn2, ogr_jedn2)
    print(Xmin, f4(Xmin))
    
prvi()
drugi()
treci()

print()