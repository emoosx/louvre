from pyglet.gl import *
from pyglet import image
import os
from utils.text import Text

class Painting:
    def __init__(self, width, height, image_file, label_text):
        self.width = width
        self.height = height
        self.image_file = image_file
        self.label_text = label_text       
        self.label = Text(self.label_text, x = 0, y = 0) 
        self.load_textures()
        self.texture_status = True
    
        self.zrot = False
        self.rot = 0.0
        self.scale = 1
    def draw(self):
        if self.texture_status:
            glBindTexture(GL_TEXTURE_2D, self.texture.id) 
        else:
            glDisable(GL_TEXTURE_2D)
        glPushMatrix()
        glRotatef(self.rot,0, 0, int(self.zrot))
        glScalef(self.scale, self.scale, self.scale)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0);     glVertex3f(-self.width, -self.height, 0);
        glTexCoord2f(1, 0);     glVertex3f(self.width, -self.height, 0);
        glTexCoord2f(1, 1);     glVertex3f(self.width, self.height, 0);
        glTexCoord2f(0, 1);     glVertex3f(-self.width, self.height, 0);
        glEnd()
        glPopMatrix()
        glEnable(GL_TEXTURE_2D)
        glTranslatef(self.width, 0, 0)
        self.label.draw()
        
        

    def load_textures(self):
        texture_file = os.getcwd() + os.path.join('/images', self.image_file)
        texture_surface = image.load(texture_file)
        texture = texture_surface.image_data.create_texture(image.Texture)
        
        glBindTexture(GL_TEXTURE_2D, texture.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.texture = texture
        
    def update(self):
        if self.zrot == False:
            self.rot += 0.0
        else:
            self.rot += 0.2

        
