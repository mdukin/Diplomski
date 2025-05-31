import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

import sys
import numpy as np
import math
import time


def draw_line(tocka1, tocka2):
    
    glColor3f(1.0, 1.0, 1.0)  

    glBegin(GL_LINES)
    glVertex2f(tocka1[0],tocka1[1])  
    glVertex2f(tocka2[0],tocka2[1])  
    glEnd()


def read_from_file_poligon(path):
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

def read_from_file(path):
    with open(path, 'r') as file:
        vrhovi = []
        for line in file:

            vrh = np.array([float(x) for x in line.strip().split()])
            vrhovi.append(vrh)

        return np.array(vrhovi)

def bezierova_krivulja(tocke, n):
    def b_in(i, n, t):
        return math.factorial(n) / (math.factorial(i) * math.factorial(n - i)) * (t**i) * ((1 - t)**(n - i))

    def bezier(t):
        pt = np.zeros(n)
        for i in range(n + 1):
            pt += tocke[i] * b_in(i, n, t)
        return pt

    return bezier

def nacrtaj_poligon(poligon):
    v1 = poligon[0]
    v2 = poligon[1]
    v3 = poligon[2]

    glBegin(GL_LINE_LOOP)
    glVertex3f(v1[0], v1[1], v1[2])
    glVertex3f(v2[0], v2[1], v2[2])
    glVertex3f(v3[0], v3[1], v3[2])
    glEnd()


def nacrtaj_tijelo(poligoni,ravnine):
    global ociste, glediste
    #vektor_promatraca = ociste #-glediste
    vektor_promatraca = np.append(ociste,1)
    for i, poligon in enumerate(poligoni):
        kut = np.dot(vektor_promatraca, ravnine[i])
        if kut >  0 :
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

def izracunaj_skalirane_vrhove(vrhovi):

    h= izracunaj_ekran(ociste, glediste)
    for vrh in vrhovi:
        
        vrh[0] /=h
        vrh[1] /=h
    return vrhovi


def izracunaj_poligone_i_ravnine(vrhovi, poligoni_topoloski):
    poligoni = []
    ravnine = []
    for poligon_topoloski in poligoni_topoloski:
        v1 = vrhovi[poligon_topoloski[0] - 1]
        v2 = vrhovi[poligon_topoloski[1] - 1]
        v3 = vrhovi[poligon_topoloski[2] - 1]

        normala = np.cross(v2[:3] - v1[:3], v3[:3] - v1[:3])
        d = -np.dot(normala, v1[:3])

        ravnine.append(np.hstack([normala, d]))
        poligoni.append([v1, v2, v3])
    return poligoni, ravnine


def transformiraj_pogled(vrhovi, top_polig):
    rucno = False
    if rucno:
        T = izracunaj_matricu_transformacije(ociste, glediste)
        P = izracunaj_matricu_projekcije(ociste,glediste)

        vrhovi = np.dot(vrhovi, T)
        vrhovi = np.dot(vrhovi, P)

        vrhovi = izracunaj_skalirane_vrhove(vrhovi)


        nacrtaj_tijelo(poligoni)
    else:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 800/600, 0.1, 100.0)
            
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(ociste[0], ociste[1], ociste[2], glediste[0], glediste[1], glediste[2], 0, 1, 0)

    poligoni, ravnine = izracunaj_poligone_i_ravnine(vrhovi, top_polig)
    nacrtaj_tijelo(poligoni, ravnine)


def srediste(vrhovi):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    return srediste[:3]

def izracunaj_ekran(ociste, glediste):
        H = np.sqrt((ociste[0]-glediste[0])**2 +
                (ociste[1]-glediste[1])**2 +
                (ociste[2]-glediste[2])**2 )
        return H
    

ociste = np.array([2.0, 2.0,2.0])
glediste = np.array([0,0,0])

def main():
    global window, ociste, glediste
    if not glfw.init():
        return

    tocke = read_from_file("ciklus 3/tocke.txt")
    bk = bezierova_krivulja(tocke, len(tocke)-1)

    tijelo = "bird"

    vrhovi, top_polig = read_from_file_poligon("ciklus 3/files/" + tijelo + ".obj")

    glediste = srediste(vrhovi)

    window = glfw.create_window(800, 600, "", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.swap_buffers(window)
    
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        for t in np.linspace(0.0, 1.0, num=100):
            ociste = bk(t)
            print(ociste, glediste)
            glClear(GL_COLOR_BUFFER_BIT)
            transformiraj_pogled(vrhovi, top_polig)
            time.sleep(0)
            glfw.swap_buffers(window)
        

    glfw.terminate()


if __name__ == "__main__":
    main()
