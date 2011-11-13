from OpenGL.GLUT import *
from pyglet.gl import *
from pyglet import image
import os
from shelf import Shelf

class Teapot:
    def __init__(self, size=40, image_file='silverware.jpg'):
        self.size = size
        self.scale = 1
        self.texture_status = True
        self.image_file = image_file
        self.load_textures()
        self.shelf = Shelf() 

        # rotational values
        self.xrot = self.yrot = self.zrot = True
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

        # draw the shelf
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        self.shelf.draw()
        glPopMatrix()
        
        if self.texture_status:
            glBindTexture(GL_TEXTURE_2D, self.texture.id)
        else:
            glDisable(GL_TEXTURE_2D)
            glColor3f(0, 0, 0)
        
        # draw the teapot
        glPushMatrix()
        glScalef(self.scale, self.scale, self.scale)
        glTranslatef(0, 2 * self.size, 0) 
        
        glRotatef(self.rot, int(self.xrot), int(self.yrot), int(self.zrot))
        glutSolidTeapot(self.size)
        glPopMatrix()
        
        glColor3f(1, 1, 1)
        # resetting texture
        glEnable(GL_TEXTURE_2D)

    def update(self):
        # a bit of a hack, I guess .. weird
        if(self.xrot == False and self.yrot == False and self.zrot == False):
            self.rot += 0.0
        else:
            self.rot += 0.5
