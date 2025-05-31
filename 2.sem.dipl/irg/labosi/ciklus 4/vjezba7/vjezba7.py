import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def read_from_file(path):
    with open(path, 'r') as file:
        vrhovi = []
        poligoni_topoloski = []
        for line in file:
            if line.startswith("v"):
                vrh = np.array([float(x) for x in line[1:].strip().split()])
                vrh = np.append(vrh, 1)
                vrhovi.append(vrh)
            elif line.startswith("f"):
                poligon = np.array([int(x) for x in line[1:].strip().split()])
                poligoni_topoloski.append(poligon)
        return np.array(vrhovi), np.array(poligoni_topoloski)



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


def nacrtaj_poligon(poligon, intensity=1):
    v1, v2, v3 = poligon
    glColor3f(intensity, intensity, intensity)

    glBegin(GL_TRIANGLES)  
    glVertex3f(v1[0], v1[1], v1[2])
    glVertex3f(v2[0], v2[1], v2[2])
    glVertex3f(v3[0], v3[1], v3[2])
    glEnd()

def izracunaj_centar_poligona(poligon):
    return np.mean(poligon, axis=0)

def nacrtaj_tijelo(poligoni, ravnine):
    global ociste

    ociste_h = np.append(ociste, 1)
    for i, poligon in enumerate(poligoni):
        centar = izracunaj_centar_poligona(poligon)
        vektor_promatraca = ociste_h - centar
        kut = np.dot(vektor_promatraca, ravnine[i])
        if kut > 0:
            intensity = izracunaj_intenzitet(ravnine[i][:3], centar)
            nacrtaj_poligon(poligon, intensity)




def keys_callback(window, key, scancode, action, mods):
    global ociste, glediste

    if key == glfw.KEY_UP and action == glfw.PRESS:
        ociste[1] += 0.2

    if key == glfw.KEY_DOWN and action == glfw.PRESS:
        ociste[1] -= 0.2

    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        ociste[0] -= 0.2

    if key == glfw.KEY_RIGHT and action == glfw.PRESS:
        ociste[0] += 0.2

    if key == glfw.KEY_1 and action == glfw.PRESS:
        ociste[2] += 0.2

    if key == glfw.KEY_2 and action == glfw.PRESS:
        ociste[2] -= 0.2

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

    print(ociste, glediste)


def transformiraj_pogled(vrhovi, top_polig):

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(55.0, 800 / 600, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(ociste[0], ociste[1], ociste[2], glediste[0], glediste[1], glediste[2], 0, 0, 1)

    poligoni, ravnine = izracunaj_poligone_i_ravnine(vrhovi, top_polig)
    nacrtaj_tijelo(poligoni, ravnine)


def izracunaj_intenzitet(normala, centroid, ka=0.1, kd=0.7):
    L = izvor_svijetla - centroid[:3]
    L = L / np.linalg.norm(L)
    N = normala / np.linalg.norm(normala)

    ambijent_komp = ka * intenzitet_izvora
    difuz_komp = kd * max(np.dot(L, N), 0) * intenzitet_izvora

    return ambijent_komp + difuz_komp

def srediste(vrhovi):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    return srediste[:3]

ociste = np.array([3.0, 3.0, 3.0])
glediste = np.array([0.98939657, 0.48553023, 0.04101622])
izvor_svijetla = np.array([5.0, 5.0, 5.0])
intenzitet_izvora = 1.5


def izracunaj_skalirane_vrhove(vrhovi):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    translatirani_vrhovi = vrhovi - srediste

    max_abs = np.max(np.abs(translatirani_vrhovi))
    skalirani_vrhovi = (translatirani_vrhovi / max_abs)

    return skalirani_vrhovi

def main():
    global window, glediste, ociste

    tijelo = "bird"

    vrhovi, top_polig = read_from_file("ciklus 3/files/" + tijelo + ".obj")
    #vrhovi = izracunaj_skalirane_vrhove(vrhovi)

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
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
        transformiraj_pogled(vrhovi, top_polig)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
