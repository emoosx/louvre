from pyglet.gl import *
from OpenGL.GLUT import *

class teapot:
    def __init__(self, size):
        self.size = size

    def draw(self):
        glutSolidTeapot(self.size)
