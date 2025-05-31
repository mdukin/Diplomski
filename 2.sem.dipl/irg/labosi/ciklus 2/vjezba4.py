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
                vrhovi.append(vrh)

            elif line.startswith("f"):
                poligon = np.array([int(x) for x in line[1:].strip().split()])
                poligoni_topoloski.append(poligon)
        return vrhovi, poligoni_topoloski



def izracunaj_translatirane_i_skalirane_vrhove(vrhovi):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    translatirani_vrhovi = vrhovi - srediste

    alfa = 0
    beta = 0
    gama = 0

    Rx = [ [1, 0, 0,],
            [0, np.cos(alfa), np.sin(alfa)],
            [0, -np.sin(alfa), np.cos(alfa)]]
    
    Ry = [[np.cos(beta), 0, np.sin(beta)],
          [0,      1,      0],
          [-np.sin(beta), 0, np.cos(beta)]]
    
    Rz = [[np.cos(gama), np.sin(gama), 0 ],
          [-np.sin(gama), np.cos(gama), 0],
          [0,0,1]]
    
    
    rotirani_vrhovi = [np.dot(Ry, vrh) for vrh in translatirani_vrhovi]

    rotirani_vrhovi = [np.dot(Rx, vrh) for vrh in rotirani_vrhovi]

    rotirani_vrhovi = [np.dot(Rz, vrh) for vrh in rotirani_vrhovi]

    max_abs = np.max(np.abs(rotirani_vrhovi))
    skalirani_vrhovi = (rotirani_vrhovi / max_abs)

    return skalirani_vrhovi


def izracunaj_poligone_i_ravnine(vrhovi, poligoni_topoloski):
    poligoni = []
    ravnine = []
    for poligon_topoloski in poligoni_topoloski:
        v1 = vrhovi[poligon_topoloski[0] - 1]
        v2 = vrhovi[poligon_topoloski[1] - 1]
        v3 = vrhovi[poligon_topoloski[2] - 1]

        normala = np.cross(v2 - v1, v3 - v1)
        d = -np.dot(normala, v1)

        ravnine.append(np.hstack([normala, d]))
        poligoni.append([v1, v2, v3])
    return poligoni, ravnine


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



def ucitaj_tocku():
    line = input("3D tocka?(skalirano): ")
    vrh = np.array([float(x) for x in line.strip().split()])
    return np.append(vrh, 1)

def ispitaj_odnos(V, ravnine):
    for R in ravnine :
        if np.dot(V, R) > 0:
            print(R)
            print("izvan tijela!")
            #return
    print("unutar tijela!!")
    return

def main():
    global window

    tijelo = "bird"

    vrhovi, top_polig = read_from_file("files/" + tijelo + ".obj")

    vrhovi = izracunaj_translatirane_i_skalirane_vrhove(vrhovi)

    poligoni, ravnine = izracunaj_poligone_i_ravnine(vrhovi, top_polig)

    print(ravnine)

    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.swap_buffers(window)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        nacrtaj_tijelo(poligoni)
        glfw.swap_buffers(window)

        V = ucitaj_tocku()
        ispitaj_odnos(V, ravnine)
        

    glfw.terminate()


if __name__ == "__main__":
    main()
