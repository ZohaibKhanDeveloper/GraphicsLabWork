from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# y = mx+c
# x1 = 0.1
# y = 0.1
# x2 =1.0
#y2  = 1.0
# m = (y2-y1)/(x2-x1)
#if m<=1:
 #y = mx+c
 #
 #else:
 # x = (y-c)/m
def draw_line():
    glColor3f(1.,0.0,0.0)
    glPointSize(8)
    glLineWidth(3)
    
    glBegin(GL_POINTS)
    for i in range(0,30,1):
     glVertex2f(0.01*i,0.02*i)
    glEnd()
    glFlush()


def display():
    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set the drawing color (white)
    glColor3f(1.0, .0, 1.0)

    # Draw the line
    draw_line()

    # Swap buffers to display the rendered image
    glutSwapBuffers()

def main():
    # Initialize GLUT
    glutInit()

    # Set the display mode (double buffering and RGB)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    # Set the window size and position
    glutInitWindowSize(700, 700)
    #glutInitWindowPosition(100, 100)

    # Create a window with the title "Slope-Intercept Line"
    glutCreateWindow(b"Slope-Intercept Line")

    # Set the display callback function
    glutDisplayFunc(display)

    # Set the background color 
    glClearColor(.0, 1.0, .0, 1.0)

    # Enter the GLUT event processing loop
    glutMainLoop()

if __name__ == "__main__":
    main()