from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Definiranje funkcije za crtanje objekta
def draw_object():
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(-1, 1, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Prvi objekt
    glPushMatrix()               # Pohrani trenutnu matricu
    glLoadIdentity()             # Reset matrice
    glTranslatef(-2, 0, -5)      # Pomakni objekt u određeni položaj
    glRotatef(45, 0, 1, 0)       # Rotiraj objekt za 45 stupnjeva oko y-osi
    glColor3f(1.0, 0.0, 0.0)     # Crvena boja
    draw_object()                # Nacrtaj objekt
    glPopMatrix()                # Vrati matricu prije transformacija ovog objekta

    # Drugi objekt
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(2, 0, -5)       # Pomakni drugi objekt na drugu poziciju
    glRotatef(30, 1, 0, 0)       # Rotiraj ovaj objekt za 30 stupnjeva oko x-osi
    glColor3f(0.0, 0.0, 1.0)     # Plava boja
    draw_object()                # Nacrtaj drugi objekt
    glPopMatrix()

    glutSwapBuffers()

# Postavljanje OpenGL prozora
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Rotacija objekata")

glutDisplayFunc(display)
glEnable(GL_DEPTH_TEST)
glutMainLoop()
