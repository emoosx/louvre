from pyglet.gl import *
from OpenGL.GLUT import *
from pyglet import image
import os
from shelf import shelf

class teapot:
    def __init__(self, size=40, image_file='silverware.jpg'):
        self.size = size
        self.image_file = image_file
        self.load_textures()
        self.shelf = shelf() 

        # rotational values
        self.xrot = self.yrot = self.zrot = False
        self.rot = 0.0

    def load_textures(self):
        texture_file = os.getcwd() + os.path.join('/images', self.image_file)
        texture_surface = image.load(texture_file)
        texture = texture_surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, texture.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.texture = texture

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)

        # draw the shelf
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        self.shelf.draw()
        glPopMatrix()
        
        # draw the teapot
        glPushMatrix()
        glTranslatef(0, self.size, 0) 
        
        # weird
        glRotatef(self.rot, int(self.xrot), int(self.yrot), int(self.zrot))
        glutSolidTeapot(self.size)
        glPopMatrix()

    def update(self):
        if(self.xrot == False and self.yrot == False and self.zrot == False):
            self.rot == 0.0
        else:
            self.rot += 0.5
