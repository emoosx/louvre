from pyglet.gl import *
from pyglet import image
import os

class Floor:
    def __init__(self, width, height, image_file):
        self.width = width
        self.height = height
        self.load_textures(image_file)

    def load_textures(self, image_file):
        texture_file = os.getcwd() + os.path.join('/images', image_file)
        texture_surface = image.load(texture_file)
        tt = texture_surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, tt.id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.texture = tt


    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0);     glVertex3f(-self.width, -self.height, 0);
        glTexCoord2f(1.0, 0.0);     glVertex3f(self.width, -self.height, 0);
        glTexCoord2f(1.0, 1.0);     glVertex3f(self.width, self.height, 0);
        glTexCoord2f(0.0, 1.0);     glVertex3f(-self.width, self.height, 0);
        glEnd()


