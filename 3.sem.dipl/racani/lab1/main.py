import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from scipy.interpolate import BSpline
from utils import *
import time
from utils_obj import *

R = []
top_polig = []
vrhovi = []

def R_i(i):
    if i - 1 < 0 or i + 2 >= len(R):
        raise IndexError("err")
    
    return R[i-1:i+3]

B_matrica = (1/6) * np.array([
    [-1, 3, -3, 1],
    [3, -6, 3, 0],
    [-3, 0, 3, 0],
    [1, 4, 1, 0]
])

B_matrica_der = (1/2) * np.array([
    [-1, 3, -3, 1],
    [2, -4, 2, 0],
    [-1, 0, 1, 0]
])

p_der = lambda t,i : np.array([t*t, t, 1]) @ B_matrica_der @ R_i(i)

P_double_der = lambda t,i : np.array([2*t, 1, 0]) @ B_matrica_der @ R_i(i)

p = lambda t,i :  np.array([t*t*t, t*t, t, 1]) @ B_matrica @ R_i(i) 

def draw_B():
        glColor3f(1.0, 0.0, 0.0)  # Red 
        glBegin(GL_LINE_STRIP)
        for i in range(1,10):
            for t in np.linspace(0.0, 1.0, num=100):
                pt= p(t,i)
                glVertex3f(pt[0], pt[1], pt[2])
        glEnd()

def draw_der(t,i):
        glColor3f(0.0, 0.0, 1.0)  # Blue

        pt = p(t,i)
        der= p_der(t,i)
        end_pt = pt+der 
        nacrtaj_tijelo(ociste, der, pt, vrhovi, top_polig)

        glBegin(GL_LINES)
        glVertex3f(pt[0], pt[1], pt[2])        
        glVertex3f(end_pt[0], end_pt[1], end_pt[2])  
        glEnd()


def normala(t,i):
     return np.cross(p_der(t,i), P_double_der(t,i))

def binormala(t,i):
     return np.cross(p_der(t,i), normala(t,i))


def main():
    global window,R, glediste, ociste,vrhovi, top_polig
    if not glfw.init():
        return

    R = ucitaj_tocke("tocke.txt")
    R = skaliraj_vrhove(R)

    ociste = np.array([0,-0.9,1.8])
    glediste = np.array([0,0,0.5])

    tijelo = "bird"
    vrhovi, top_polig = read_from_file("files/" + tijelo + ".obj")
    vrhovi = skaliraj_vrhove(vrhovi,0.15)

    window = glfw.create_window(1000, 800, "", None, None)

    if not window:
        glfw.terminate()
        return
    
    glfw.swap_buffers(window)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        transformiraj_pogled(ociste,glediste)
        for i in range(1,10):
            for t in np.linspace(0.0, 1.0, num=10):
                glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)                
                draw_B()
                draw_der(t,i)
                glfw.swap_buffers(window)


    glfw.terminate()


if __name__ == "__main__":
    main()
