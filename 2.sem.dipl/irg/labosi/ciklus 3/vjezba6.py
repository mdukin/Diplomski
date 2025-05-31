import glfw
from OpenGL.GL import *
import sys
import numpy as np
import math

def skaliraj_vrhove(vrhovi):
    vrhovi = np.array(vrhovi)
    min_vrijednost = np.min(vrhovi, axis=0)
    max_vrijednost = np.max(vrhovi, axis=0)
    srediste = (min_vrijednost + max_vrijednost) / 2

    translatirani_vrhovi = vrhovi - srediste

    max_abs = np.max(np.abs(translatirani_vrhovi))
    skalirani_vrhovi = (translatirani_vrhovi / max_abs)

    return skalirani_vrhovi

def draw_line(tocka1, tocka2):
    
    glColor3f(1.0, 1.0, 1.0)  

    glBegin(GL_LINES)
    glVertex2f(tocka1[0],tocka1[1])  
    glVertex2f(tocka2[0],tocka2[1])  
    glEnd()

def draw_poligon(tocke):
    for i in range(1,len(tocke)):
        draw_line( tocke[i-1], tocke[i] )


def read_from_file(path):
    with open(path, 'r') as file:
        vrhovi = []
        for line in file:

            vrh = np.array([float(x) for x in line.strip().split()])
            vrhovi.append(vrh)

        return np.array(vrhovi)

def draw_bezier(bk):
        glColor3f(1.0, 0.0, 0.0)  # Red 
        glBegin(GL_LINE_STRIP)
        for t in np.linspace(0.0, 1.0, num=100):
            pt= bk(t)
            glVertex2f(pt[0], pt[1])
        glEnd()

def bezierova_krivulja(tocke, n):
    def b_in(i, n, t):
        return math.factorial(n) / (math.factorial(i) * math.factorial(n - i)) * (t**i) * ((1 - t)**(n - i))

    def bezier(t):
        pt = np.zeros(n)
        for i in range(n + 1):
            pt += tocke[i] * b_in(i, n, t)
        return pt

    return bezier

def main():
    global window
    if not glfw.init():
        return

    tocke = read_from_file("ciklus 3/tocke.txt")
    tocke = skaliraj_vrhove(tocke)

    bk = bezierova_krivulja(tocke, len(tocke)-1)

    window = glfw.create_window(800, 600, "", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.swap_buffers(window)
    
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        draw_poligon(tocke)
        draw_bezier(bk)
        glfw.swap_buffers(window)
        

    glfw.terminate()


if __name__ == "__main__":
    main()
