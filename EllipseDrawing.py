from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def plot_4_symmetric(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)

def draw_ellipse():
    a = 0.3  # Semi-major axis (horizontal)
    b = 0.7  # Semi-minor axis (vertical)
    xc, yc = 0.0, 0.0  # Center

    step = 0.001
    glBegin(GL_POINTS)
    
    x = -a
    while x <= a:
        y = b * math.sqrt(1 - (x**2) / (a**2))
        plot_4_symmetric(xc, yc, x, y)
        x += step

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_ellipse()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)          # White ellipse
    glPointSize(2.0)                  # Pixel size

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Ellipse using Equation")
init()
glutDisplayFunc(display)
glutMainLoop()
