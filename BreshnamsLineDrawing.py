from OpenGL.GL import *
from OpenGL.GLUT import *

def plot_point(x, y):
    glVertex2f(x / 200.0, y / 200.0)  # Normalize to OpenGL coordinates

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    glBegin(GL_POINTS)

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            plot_point(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            plot_point(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    plot_point(x, y)  # Plot last point
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    bresenham_line(-100, -50, 100, 50)  # Example line
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background black
    glColor3f(1.0, 1.0, 1.0)          # Line color white
    glPointSize(5.0)                  # Point size

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bresenham Line Drawing")
init()
glutDisplayFunc(display)
glutMainLoop()
