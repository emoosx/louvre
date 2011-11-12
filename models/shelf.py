from pyglet.gl import *
from pyglet import image
import os

class shelf:
    def __init__(self, height=100, radius=100, image_file='shelf.jpg'):
        self.radius = radius
        self.height = height
        self.image_file = image_file
        self.load_textures()

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
        quad = gluNewQuadric()
        gluQuadricTexture(quad, GL_TRUE)
        gluCylinder(quad, 5, 5, self.height, 100, 100) 
        gluDisk(quad, 0, self.radius, 100, 100 )
