from pyglet.gl import *
from pyglet import image
import os
from shelf import shelf

class basketball:
    def __init__(self, radius=40, image_file="bb.jpg"):
        self.radius = radius
        self.image_file = image_file
        self.shelf = shelf()
        self.scale = 1
        self.texture_status = True
        self.load_textures()

        # rotational values
        self.xrot = self.yrot = self.zrot = False
        self.rot = 0.0

    def load_textures(self):
        texture_file = os.getcwd() + os.path.join('/images', self.image_file)
        texture_surface= image.load(texture_file)
        texture = texture_surface.image_data.create_texture(image.Texture)
        glBindTexture(GL_TEXTURE_2D, texture.id)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.texture = texture

    def draw(self):

        # draw the shelf
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        self.shelf.draw()
        glPopMatrix()

        # Enable/Disabling texture
        if self.texture_status:
            glBindTexture(GL_TEXTURE_2D, self.texture.id)
        else:
            glDisable(GL_TEXTURE_2D)

        # draw the bird
        glPushMatrix()
        glScalef(self.scale, self.scale, self.scale)
        glTranslatef(0, 2 * self.radius, 0)
        glRotatef(self.rot, int(self.xrot), int(self.yrot), int(self.zrot))
        quad = gluNewQuadric()
        gluQuadricTexture(quad, GL_TRUE)
        gluSphere(quad, self.radius, 100, 100)
        glPopMatrix()

        # resetting texture status for drawing other objects
        glEnable(GL_TEXTURE_2D)

    def update(self):
        # a bit of a hack, I guess .. weird
        if(self.xrot == False and self.yrot == False and self.zrot == False):
            self.rot += 0.0
        else:
            self.rot += 0.5
