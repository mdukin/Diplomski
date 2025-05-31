import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
from utils import *
izvor_svijetla = np.array([5,5,5])
intenzitet_izvora = 2

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


def izracunaj_intenzitet(normala, centroid, ka=0.1, kd=0.7):
    L = izvor_svijetla - centroid[:3]
    L = L / np.linalg.norm(L)
    N = normala / np.linalg.norm(normala)

    ambijent_komp = ka * intenzitet_izvora
    difuz_komp = kd * max(np.dot(L, N), 0) * intenzitet_izvora

    return ambijent_komp + difuz_komp


def rotiraj_obj(e):
    s = np.array([0,0,1]) 
    os = np.cross(s, e)    
    fi = np.arccos(np.dot(s, e) / (np.linalg.norm(s) * np.linalg.norm(e)))  #
    stupnjevi = np.degrees(fi) 
    glRotatef(stupnjevi, os[0], os[1], os[2])  


def nacrtaj_tijelo( ociste, der, pt, vrhovi, top_polig, dcm = False):
    ociste_h = np.append(ociste, 1)

    glPushMatrix()
    glTranslatef(pt[0], pt[1], pt[2]) 

    e = der[:3]  
    if not dcm:
        rotiraj_obj(e)          

    poligoni, ravnine = izracunaj_poligone_i_ravnine(vrhovi, top_polig)

    for i, poligon in enumerate(poligoni):
        centar = izracunaj_centar_poligona(poligon)
        vektor_promatraca = ociste_h - centar
        kut = np.dot(vektor_promatraca, ravnine[i])
        

        intensity = izracunaj_intenzitet(ravnine[i][:3], centar)
        nacrtaj_poligon(poligon,intensity)

    glPopMatrix()  