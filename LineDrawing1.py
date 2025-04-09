from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_line():
    m = 0.5  # slope
    b = 0.0  # y-intercept

    glBegin(GL_POINTS)
    x = -0.8
    while x <= 0.8:
        y = m * x + b
        glVertex2f(x, y)
        x += 0.01
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    glFlush()

glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow(b"Slope Intercept Line")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutDisplayFunc(display)
glutMainLoop()
