import glfw
from OpenGL.GL import *
import sys
import numpy as np


class vrh:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y
    def tuple(self):
        return self.x, self.y

class brid:
    def __init__(self, point1: vrh, point2: vrh):
        self.a = - ( point1.y - point2.y )
        self.b = - ( -point1.x + point2.x )
        self.c = - ( point1.x * point2.y - point2.x * point1.y )
    def print(self):
        print( self.a, self.b, self.c)


vrhovi = []
bridovi  = []
counter = 0
n = 0
V = None
xmin = sys.maxsize; xmax = 0; ymin = sys.maxsize; ymax = 0


def normalized_point(point:vrh):
    width, height = glfw.get_framebuffer_size(window)
    xpos = (point.x / width) * 2 - 1
    ypos = ((height - point.y) / height) * 2 - 1
    return vrh(xpos, ypos)

def draw_line(point1:vrh, point2:vrh):
    
    glColor3f(1.0, 1.0, 1.0)  

    x1,y1 = normalized_point(point1).tuple()
    x2,y2 = normalized_point(point2).tuple()

    glBegin(GL_LINES)
    glVertex2f(x1,y1)  
    glVertex2f(x2,y2)  
    glEnd()

def draw_poligon():
    global vrhovi, n, bridovi
    for i in range(1,n+1):
        draw_line( vrhovi[i-1], vrhovi[i] )

def draw_point(point:vrh):
    ### ispitaj odnos, unutar ili izvan
    unutar_poligona = True
    for brid in bridovi:
        if point.x * brid.a + point.y * brid.b + brid.c > 0 :
            unutar_poligona = False
            break

    if unutar_poligona:
        glColor3f(1.0, 0.0, 0.0)
    else:
        glColor3f(0.0, 1.0, 0.0)

    point = normalized_point(point)
    glBegin(GL_LINES)
    glVertex2f(point.x-0.05,point.y)  
    glVertex2f(point.x+0.05,point.y)  
    glVertex2f(point.x,point.y-0.05)  
    glVertex2f(point.x,point.y+0.05)  
    glEnd() 

def bojanje():
    global flag
    
    linespace = np.linspace(ymin,ymax, 1000)

    for y in linespace:
        L = xmin
        D = xmax
        for i in range(0,n):
            
            if bridovi[i].a == 0 : break
            
            x1 = (- bridovi[i].b * y - bridovi[i].c ) / bridovi[i].a


            ##L
            if vrhovi[i].y >= vrhovi[i+1].y :
                if x1 > L : L = x1
            ##D
            if vrhovi[i].y < vrhovi[i+1].y :
                if x1 <D : D = x1            


        #if L < D : 
        draw_line(vrh(L, y), vrh(D,y))




def mouse_button_callback(window, button, action, mods):
    global vrhovi, counter, n,V, xmax,xmin,ymax,ymin
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        if counter < n : 
            xpos, ypos = glfw.get_cursor_pos(window)
            vrhovi.append(vrh(xpos,ypos))

            counter +=1
            print(counter)
            draw_point(vrh(xpos,ypos))
            if xpos > xmax : xmax = xpos
            if xpos < xmin : xmin = xpos
            if ypos > ymax : ymax = ypos
            if ypos < ymin : ymin = ypos

            if counter == n:
                vrhovi.append(vrhovi[0])
                for i in range(1,n+1):
                    bridovi.append(brid(vrhovi[i-1], vrhovi[i]))

        elif counter == n : 
            xpos, ypos = glfw.get_cursor_pos(window)
            V = vrh(xpos, ypos)



def main():
    global window, n

    if not glfw.init():
        return
    
    n = int(input("n??: "))


    window = glfw.create_window(800, 600, "", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.swap_buffers(window)

    glfw.set_mouse_button_callback(window, mouse_button_callback)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        if counter == n:
            glClear(GL_COLOR_BUFFER_BIT)
            draw_poligon()
            if V is not None:
                bojanje()
                draw_point(V)
        glfw.swap_buffers(window)
            
    glfw.terminate()

if __name__ == "__main__":
    main()
