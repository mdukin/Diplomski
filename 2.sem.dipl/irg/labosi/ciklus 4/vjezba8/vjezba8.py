import glfw
from OpenGL.GL import *
import sys
import numpy as np
import math

colors = [
    (1.0, 0.0, 0.0),  # Red
    (0.0, 1.0, 0.0),  # Green
    (0.0, 0.0, 1.0),  # Blue
    (1.0, 1.0, 0.0),  # Yellow
    (1.0, 0.0, 1.0),  # Magenta
    (0.0, 1.0, 1.0),  # Cyan
    (0.5, 0.0, 0.0),  # Dark Red
    (0.0, 0.5, 0.0),  # Dark Green
    (0.0, 0.0, 0.5),  # Dark Blue
    (0.5, 0.5, 0.0),  # Olive
    (0.5, 0.0, 0.5),  # Purple
    (0.0, 0.5, 0.5),  # Teal
    (0.5, 0.5, 0.5),  # Grey
    (0.75, 0.75, 0.75), # Light Grey
    (1.0, 0.5, 0.0),  # Orange
    (0.5, 1.0, 0.5),   # Light Green
    (0.0, 0.0, 0.0)
]


def normalized_point(x,y):
    width, height = glfw.get_framebuffer_size(window)
    xpos = (x / width) * 2 - 1
    ypos = ((height - y) / height) * 2 - 1
    return xpos, ypos

def draw_point(x, y, k):

    x, y = normalized_point(x, y)
    glBegin(GL_POINTS)
    glColor3f(*colors[k])  
    glVertex2d(x, y)
    glEnd()


def draw_mandelbrot():
    eps = 100
    m = 16
    (u_min,u_max) = (-1.5, 0.5)
    (v_min,v_max) = (-1, 1)
    x_max, y_max = glfw.get_framebuffer_size(window)

    u_const = (u_max-u_min) / x_max
    v_const = (v_max-v_min) / y_max
    
    for x0 in range(0,x_max) :
        for y0 in range(0,y_max):
            u0 = u_const*x0 + u_min
            v0 = v_const*y0 + v_min

            c = complex(u0, v0)
            z = complex(0, 0)
            k = -1

            while abs(z) < eps and k < m:
                z = z*z + c
                k += 1

            draw_point(x0,y0, int(k))
            

def draw_julije():
    eps = 100
    m = 16
    (u_min,u_max) = (-1.0, 1.0)
    (v_min,v_max) = (-1.2, 1.2)
    c = complex(0.32, 0.043)
    x_max, y_max = glfw.get_framebuffer_size(window)

    u_const = (u_max-u_min) / x_max
    v_const = (v_max-v_min) / y_max
    
    for x0 in range(0,x_max) :
        for y0 in range(0,y_max):

            u0 = u_const*x0 + u_min
            v0 = v_const*y0 + v_min

            z = complex(u0, v0)
            k = -1

            while abs(z) < eps and k < m:
                z = z*z + c
                k += 1

            draw_point(x0,y0, int(k))
            

def main():
    global window
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
        #draw_mandelbrot()
        draw_julije()
        glfw.swap_buffers(window)
        

    glfw.terminate()


if __name__ == "__main__":
    main()
