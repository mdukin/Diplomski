import glfw
from OpenGL.GL import *
import sys
import numpy as np


def read_from_file(path):
    with open(path, 'r') as file:
        vrhovi = []
        poligoni_topoloski = []
        for line in file:

            if line.startswith("v"):
                vrh = np.array([float(x) for x in line[1:].strip().split()])
                vrh = np.append(vrh,1)
                vrhovi.append(vrh)

            elif line.startswith("f"):
                poligon = np.array([int(x) for x in line[1:].strip().split()])
                poligoni_topoloski.append(poligon)
        return np.array(vrhovi), np.array(poligoni_topoloski)



def izracunaj_skalirane_vrhove(vrhovi):

    h= izracunaj_ekran(ociste, glediste)
    for vrh in vrhovi:

        vrh[0] /=h
        vrh[1] /=h

    return vrhovi


def izracunaj_poligone(vrhovi, poligoni_topoloski):
    poligoni = []

    for poligon_topoloski in poligoni_topoloski:
        v1 = vrhovi[poligon_topoloski[0] - 1]
        v2 = vrhovi[poligon_topoloski[1] - 1]
        v3 = vrhovi[poligon_topoloski[2] - 1]

        poligoni.append([v1, v2, v3])
    return poligoni


def nacrtaj_poligon(poligon):
    v1 = poligon[0]
    v2 = poligon[1]
    v3 = poligon[2]

    glBegin(GL_LINE_LOOP)
    glVertex3f(v1[0], v1[1], v1[2])
    glVertex3f(v2[0], v2[1], v2[2])
    glVertex3f(v3[0], v3[1], v3[2])
    glEnd()


def nacrtaj_tijelo(poligoni):
    for poligon in poligoni:
        nacrtaj_poligon(poligon)


def izracunaj_matricu_transformacije(ociste, glediste):
    T1 = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [-ociste[0], -ociste[1], -ociste[2], 1]])
    
    xg1 = glediste[0] - ociste[0]
    yg1 = glediste[1] - ociste[1]
    zg1 = glediste[2] - ociste[2]

    alfa = np.arctan2(yg1, xg1)

    T2 = np.array([[np.cos(alfa), -np.sin(alfa), 0, 0],
                   [np.sin(alfa), np.cos(alfa), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]] )
    
    xg2 = np.sqrt(xg1**2 + yg1**2)
    yg2 = 0
    zg2 = zg1

    beta = np.arctan2(xg2, zg1)

    T3 = np.array([[np.cos(beta), 0, np.sin(beta), 0],
                   [0, 1, 0, 0],
                   [-np.sin(beta), 0, np.cos(beta), 0],
                   [0, 0, 0, 1]] )
    
    T4 = np.array([[0, -1, 0, 0],
                   [1, 0, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    
    T5 = np.array([[-1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    T = np.dot(T1, np.dot(T2, np.dot(T3, np.dot(T4, T5))))

    return T


def izracunaj_matricu_projekcije(ociste, glediste):
    H = np.sqrt((ociste[0]-glediste[0])**2 +
                (ociste[1]-glediste[1])**2 +
                (ociste[2]-glediste[2])**2 )
    
    return np.array([[1,0,0,0],
                    [0,1,0,0],
                    [0,0,0,1/H],
                    [0,0,0,0]])

def izracunaj_ekran(ociste, glediste):
        H = np.sqrt((ociste[0]-glediste[0])**2 +
                (ociste[1]-glediste[1])**2 +
                (ociste[2]-glediste[2])**2 )
        #return ociste[0]*H / ociste[2], ociste[1]*H/ociste[2]
        return H
    

def keys_callback(window, key, scancode, action,mods):
    global ociste, glediste 

    if key == glfw.KEY_UP and action == glfw.PRESS:
        ociste[1] += 0.2

    if key == glfw.KEY_DOWN and action == glfw.PRESS:
        ociste[1] -=  0.2

    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        ociste[0] -=  0.2

    if key == glfw.KEY_RIGHT and action == glfw.PRESS:
        ociste[0] +=  0.2
    
    if key == glfw.KEY_1 and action == glfw.PRESS:
        ociste[2] +=  0.2

    if key == glfw.KEY_2 and action == glfw.PRESS:
        ociste[2] -=  0.2
    
    ###

    if key == glfw.KEY_Q and action == glfw.PRESS:
        glediste[0] += 0.2

    if key == glfw.KEY_W and action == glfw.PRESS:
        glediste[0] -= 0.2

    if key == glfw.KEY_E and action == glfw.PRESS:
        glediste[1] -= 0.2

    if key == glfw.KEY_R and action == glfw.PRESS:
        glediste[1] += 0.2
    
    if key == glfw.KEY_A and action == glfw.PRESS:
        glediste[2] += 0.2

    if key == glfw.KEY_S and action == glfw.PRESS:
        glediste[2] -= 0.2

    print(ociste,glediste)

def transformiraj_pogled(vrhovi, top_polig):
    T = izracunaj_matricu_transformacije(ociste, glediste)
    P = izracunaj_matricu_projekcije(ociste,glediste)

    vrhovi = np.dot(vrhovi, T)
    vrhovi = np.dot(vrhovi, P)

    vrhovi = izracunaj_skalirane_vrhove(vrhovi)

    poligoni = izracunaj_poligone(vrhovi, top_polig)

    nacrtaj_tijelo(poligoni)


ociste = np.array([2.0, 2.0, 2.0])
glediste = np.array([0.98939657, 0.48553023, 0.04101622])


def srediste(vrhovi):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    return srediste[:3]

def main():
    global window, glediste, ociste

    tijelo = "bird"

    vrhovi, top_polig = read_from_file("ciklus 3/files/" + tijelo + ".obj")

    glediste = srediste(vrhovi)

    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.swap_buffers(window)

    glfw.set_key_callback(window, keys_callback)
    
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        transformiraj_pogled(vrhovi, top_polig)
        glfw.swap_buffers(window)
        

    glfw.terminate()


if __name__ == "__main__":
    main()
