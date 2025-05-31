import glfw
from OpenGL.GL import *

point1 = ()
point2 = ()
points = 0
pomak = 20

def plotLineLow(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    y_korak = 1 if dy > 0 else -1
    dy = abs(dy)
    D = 2 * dy - dx
    y = y0

    glBegin(GL_POINTS)
    for x in range(x0, x1 + 1):
        draw_point(x, y)
        if D > 0:
            y += y_korak
            D += 2 * (dy - dx)
        else:
            D += 2 * dy
    glEnd()

def plotLineHigh(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    x_pomak = 1 if dx > 0 else -1
    dx = abs(dx)
    D = 2 * dx - dy
    x = x0

    glBegin(GL_POINTS)
    for y in range(y0, y1 + 1):
        draw_point(x, y)
        if D > 0:
            x += x_pomak
            D += 2 * (dx - dy)
        else:
            D += 2 * dx
    glEnd()

def bresenham():

    x0  = point1[0] ;y0 = point1[1]
    x1  = point2[0]; y1 = point2[1]

    if abs(y1 - y0) < abs(x1 - x0):     # (-45 45)  (135 225)
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0)
        else:
            plotLineLow(x0, y0, x1, y1)
    else:                               # gore, dolje, strmo
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0)
        else:
            plotLineHigh(x0, y0, x1, y1)


def normalized_point(x,y):
    width, height = glfw.get_framebuffer_size(window)
    xpos = (x / width) * 2 - 1
    ypos = ((height - y) / height) * 2 - 1
    return xpos, ypos

def draw_point(x, y):

    x,y = normalized_point(x,y)
    glVertex2f(x,y)

def bresenham_adv():
    
    x0  = point1[0] ;y0 = point1[1]
    x1  = point2[0]; y1 = point2[1]

    dx = abs(x1-x0)
    sx = 1 if x0 < x1 else -1
    dy = - abs(y1-y0)
    sy = 1 if y0 < y1 else -1
    error = dx + dy


    glBegin(GL_POINTS)
    while True:
        draw_point(x0, y0)
        if x0 == x1 and y0 == y1: break
        e2 = 2 * error
        if e2 >= dy:
            if x0 == x1 :break
            error = error + dy
            x0 += sx
        if e2 <= dx:
            if y0 == y1: break
            error += dx
            y0 += sy
    glEnd()



def draw_line():
    
    glColor3f(1.0, 1.0, 1.0)  

    x1,y1 = normalized_point(point1[0], point1[1] + pomak)
    x2,y2 = normalized_point(point2[0], point2[1] + pomak)

    glBegin(GL_LINES)
    glVertex2f(x1,y1)  
    glVertex2f(x2,y2)  
    glEnd()



def mouse_button_callback(window, button, action, mods):
    global point1, point2, points
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        xpos, ypos = glfw.get_cursor_pos(window)

        if points != 1: 
            points = 1
            point1 = (int(xpos), int(ypos))
        elif points == 1: 
            points = 2 
            point2 = (int(xpos), int(ypos))

        print(xpos, ypos)
        print(normalized_point(xpos,ypos))



def main():
    global window, points
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.swap_buffers(window)

    glfw.set_mouse_button_callback(window, mouse_button_callback)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        if points == 2:
            points = 0
            glClear(GL_COLOR_BUFFER_BIT)
            bresenham()
            draw_line()
            glfw.swap_buffers(window)
            
            
    glfw.terminate()

if __name__ == "__main__":
    main()
