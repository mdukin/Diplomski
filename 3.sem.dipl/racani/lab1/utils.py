import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

u_vektor = []

def B(i,k,u):
    if k==0:
        if u >= u_vektor[i] and u < u_vektor[i+1] : return 1
        else: return 0
    
    r1 = u_vektor[i+k]-u_vektor[i]
    s1 = 0 if r1 == 0 else B(i,k-1,u) * (u-u_vektor[i] )/ r1

    r2 = u_vektor[i+k+1]-u_vektor[i+1]
    s2 = 0 if r2 == 0 else B(i+1,k-1,u) * (u_vektor[i+k+1]-u )/ r2

    return s1 + s2

def skaliraj_vrhove(vrhovi,mi = 1):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    translatirani_vrhovi = vrhovi - srediste

    max_abs = np.max(np.abs(translatirani_vrhovi))
    skalirani_vrhovi = (translatirani_vrhovi / max_abs)

    return skalirani_vrhovi * mi


def ucitaj_tocke(ime_datoteke):
    with open(ime_datoteke, 'r') as file:
        tocke = [list(map(float, linija.split())) for linija in file]

    R = np.array(tocke)
    R = np.hstack([R, np.ones((R.shape[0], 1))])
    return R

def transformiraj_pogled(ociste, glediste):

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800 / 600, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(ociste[0], ociste[1], ociste[2], glediste[0], glediste[1], glediste[2], 0, 0 ,1)

def rotiraj(vrhovi,a,b,g):
    alfa = a
    beta = b
    gama = g

    Rx = [ [1, 0, 0,],
            [0, np.cos(alfa), np.sin(alfa)],
            [0, -np.sin(alfa), np.cos(alfa)]]
    
    Ry = [[np.cos(beta), 0, np.sin(beta)],
          [0,      1,      0],
          [-np.sin(beta), 0, np.cos(beta)]]
    
    Rz = [[np.cos(gama), np.sin(gama), 0 ],
          [-np.sin(gama), np.cos(gama), 0],
          [0,0,1]]
    
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    vrhovi = vrhovi - srediste
    
    rotirani_vrhovi = [np.dot(Ry, vrh[:3]) for vrh in vrhovi]

    rotirani_vrhovi = [np.dot(Rx, vrh) for vrh in rotirani_vrhovi]

    rotirani_vrhovi = [np.dot(Rz, vrh) for vrh in rotirani_vrhovi]
    return rotirani_vrhovi

