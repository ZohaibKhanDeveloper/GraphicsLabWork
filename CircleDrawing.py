from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def draw_circle():
    r = 0.5  # radius in OpenGL coordinates
    glBegin(GL_POINTS)
    x = -r
    while x <= r:
        y = math.sqrt(r**2 - x**2)
        glVertex2f(x, y)    # Upper half
        glVertex2f(x, -y)   # Lower half (symmetric)
        x += 0.001
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)          # White points
    glPointSize(2.0)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Circle using Equation")
init()
glutDisplayFunc(display)
glutMainLoop()
