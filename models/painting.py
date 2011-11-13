from pyglet.gl import *
from pyglet import image
import os

class Painting:
    def __init__(self, width, height, image_file, label_text):
        self.width = width
        self.height = height
        self.image_file = image_file
        self.label_text = label_text       
        self.load_textures()
    
    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id) 
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0);     glVertex3f(-self.width, -self.height, 0);
        glTexCoord2f(1, 0);     glVertex3f(self.width, -self.height, 0);
        glTexCoord2f(1, 1);     glVertex3f(self.width, self.height, 0);
        glTexCoord2f(0, 1);     glVertex3f(-self.width, self.height, 0);
        glEnd()

    def load_textures(self):
        texture_file = os.getcwd() + os.path.join('/images', self.image_file)
        texture_surface = image.load(texture_file)
        texture = texture_surface.image_data.create_texture(image.Texture)
        
        glBindTexture(GL_TEXTURE_2D, texture.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.texture = texture
        
    def update(self):
        pass

        
