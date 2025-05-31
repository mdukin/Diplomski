import numpy as np
from utils import zlatni_rez, unimodalni, solve_lup, min_na_pravcu
from autograd import grad,jacobian
from Matrica import Matrica
from funkcije import funkcija


def gradijentni_spust(x0:np.array, F:funkcija,epsilon = 10**-6, linijsko_pretrazivanje = False):
    x = np.copy(x0)
    pozivi_gradijenta = 0
    gradijent = grad(F.get_func)
    best_value = F.F(x)
    n_nepoboljsanja = 0
    while True : 
        gradijent_vektor = gradijent(x)
        pozivi_gradijenta+=1
        if np.linalg.norm(gradijent_vektor) < epsilon or pozivi_gradijenta >5000:
            break

        if linijsko_pretrazivanje :
            x = min_na_pravcu(x,gradijent_vektor,F)
        else:
            x -= gradijent_vektor

        current_value = F.F(x)
        if current_value < best_value:
            best_value = current_value
            n_nepoboljsanja = 0
        else:
            n_nepoboljsanja += 1

        if n_nepoboljsanja >= 10:
            print("Moguća divergencija!!!!: ")
            break

    return x, pozivi_gradijenta, F.get_counter(), F.get_func(x)

def newthon_raphson(x0:np.array, F:funkcija,epsilon = 10**-6, linijsko_pretrazivanje = False):
    x = np.copy(x0)
    n = x0.size
    n_nepoboljsanja = 0
    best_value = F.F(x)
    gradijent = grad(F.get_func)
    pozivi_gradijenta_i_hess_matrice = 0
    while True : 

        gradijent_vektor_neg = -Matrica(gradijent(x).reshape(2, -1))

        Hess_matrix =  Matrica(jacobian(gradijent)(x) )._transpose()

        pozivi_gradijenta_i_hess_matrice += 1

        dx = solve_lup(Hess_matrix,gradijent_vektor_neg).values.flatten()
    
        if np.linalg.norm(dx) < epsilon or pozivi_gradijenta_i_hess_matrice >3000:
            break
        
        if linijsko_pretrazivanje :
            x = min_na_pravcu(x,dx,F)
        else:    
            x += dx

        current_value = F.F(x)
        if current_value < best_value:
            best_value = current_value
            n_nepoboljsanja = 0
        else:
            n_nepoboljsanja += 1

        if n_nepoboljsanja >= 20:
            print("Moguća divergencija!!!!")
            break

    return x, pozivi_gradijenta_i_hess_matrice, F.get_counter(), F.get_func(x)

def gauss_newthon(x0:np.array, F:funkcija, G ,epsilon = 10**-6, linijsko_pretrazivanje = False):
    x = np.copy(x0)
    grad_iter = 0
    n_nepoboljsanja = 0
    best_value = F.F(x)
    while True : 
        gx = G(x)
        Jx = jacobian(G)(x)

        n = gx.size
        grad_iter +=1
        G_m =  Matrica(gx.reshape(n,-1))       
        J_m = Matrica(Jx) 

        A = J_m._transpose() * J_m
        g = J_m._transpose() * G_m

        dx = 0.01 * np.ones_like(x)
        if linijsko_pretrazivanje :
            x = min_na_pravcu(x,dx,F)

        else:    
            try:
                dx = solve_lup(A, -g).values.flatten()
                x += dx
            except:
                x += dx

        if np.linalg.norm(dx) < epsilon or grad_iter >3000:
            break
        current_value = F.F(x)
        if current_value < best_value:
            best_value = current_value
            n_nepoboljsanja = 0
        else:
            n_nepoboljsanja += 1

        if n_nepoboljsanja >= 20:
            print("Moguća divergencija!!!!!")
            break

    return x , grad_iter, F.get_counter(), F.get_func(x)