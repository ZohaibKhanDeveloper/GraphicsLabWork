from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def plot_8_symmetric(xc, yc, x, y):
    glVertex2f((xc + x), (yc + y))
    glVertex2f((xc - x), (yc + y))
    glVertex2f((xc + x), (yc - y))
    glVertex2f((xc - x), (yc - y))
    glVertex2f((xc + y), (yc + x))
    glVertex2f((xc - y), (yc + x))
    glVertex2f((xc + y), (yc - x))
    glVertex2f((xc - y), (yc - x))

def draw_circle():
    r = 0.5
    step = 0.001
    glBegin(GL_POINTS)
    x = 0.0
    while x <= r / math.sqrt(2):  # Only iterate through first octant
        y = math.sqrt(r**2 - x**2)
        plot_8_symmetric(0.0, 0.0, x, y)
        x += step
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background black
    glColor3f(1.0, 1.0, 1.0)          # Circle color white
    glPointSize(2.0)                  # Point size

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Circle using Equation - 8 Symmetric")
init()
glutDisplayFunc(display)
glutMainLoop()
