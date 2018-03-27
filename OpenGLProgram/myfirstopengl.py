import sys
from math import pi as PI
from math import sin, cos
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyPyOpenGLTest:
    def __init__(self,width=640,height=480,title='My First OpenGL'):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_DEPTH)
        glutInitWindowSize(wifth,height)
        self.window = glutCreateWindow(title)
        
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width,height)
        
    def InitGL(self,width,height):
        glClearColor(1.0,1.0,1.0,0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)

    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-3.0, 2.0, -8.0)
        
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glEnd()

        glutSwapBuffers()

    def MainLoop(self):
        glutMainLoop()

if __name__=='__main__':
    w = MyPyOpenGLTest()
    w.MainLoop()
