from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))  # Calculate number of steps needed

    x_inc = dx / steps  # Calculate increment in x
    y_inc = dy / steps  # Calculate increment in y

    x = x1
    y = y1

    glBegin(GL_POINTS)
    for _ in range(steps + 1):
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line_dda(-0.8, -0.4, 0.8, 0.4)  # Example line using DDA
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)          # Draw in white
    glPointSize(2.0)                  # Point size

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"DDA Line Drawing")
init()
glutDisplayFunc(display)
glutMainLoop()
