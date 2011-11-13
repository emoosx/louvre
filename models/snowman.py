from pyglet.gl import *
from pyglet import image
import os
from shelf import Shelf

class Snowman:
    def __init__(self, body_radius=50 ):
        self.body_radius = body_radius
        self.scale = 1 
        label = "Snowman\n----------\n - Lethal\n- Scaling"
        self.shelf = Shelf(label=label)
        # rotational values
        self.xrot = self.yrot = self.zrot = False
        self.rot = 0.0
        
    def draw(self):
        
        # draw the shelf
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        self.shelf.draw()
        glPopMatrix()

        glDisable(GL_TEXTURE_2D)

        # draw the snowman
        glPushMatrix()
        glTranslatef(0, (self.body_radius * self.scale)+20, 0)
        quad = gluNewQuadric()
        gluQuadricNormals(quad, GLU_SMOOTH)
        
        # Main body
        glPushMatrix()
        glColor3f(1, 1, 1)
        gluSphere(quad, self.body_radius * self.scale, 100, 100) 
        
        glTranslatef(0, self.body_radius * 1.5 * self.scale, 0)
        gluSphere(quad, self.body_radius * 0.75 * self.scale, 100, 100)

        glTranslatef(0, self.body_radius * self.scale, 0)
        gluSphere(quad, self.body_radius * 0.5 * self.scale, 100, 100)

        # Nose
        glColor3f(1, 0, 0)
        glTranslatef(0, 0, self.body_radius*0.5 * self.scale)
        gluCylinder(quad, self.body_radius * 0.1 * self.scale, 0.0, 20 * self.scale, 100, 100)

        # Two Eyes
        glColor3f(0, 0, 0)
        glTranslatef(-10 * self.scale, 10 * self.scale, 0)
        gluSphere(quad, self.body_radius * 0.03 * self.scale, 100, 100)

        glTranslatef(20 * self.scale, 0, 0)
        gluSphere(quad, self.body_radius * 0.03 * self.scale, 100, 100)
        glColor3f(1,1, 1)
        glPopMatrix()

        # Hat
        glPushMatrix()
        glColor3f(0, 0, 0)
        glTranslatef(0, self.body_radius * 2.85 * self.scale, 0)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(quad, self.body_radius * 0.4 * self.scale, self.body_radius * 0.4 * self.scale, 45 * self.scale, 100, 100)

        # Hat brim
        glColor3f(0,0,0)
        gluDisk(quad, 17 * self.scale, 38 * self.scale, 100, 100)
        glPopMatrix()

        glPopMatrix()
        glColor3f(1, 1, 1)
        glEnable(GL_TEXTURE_2D)

        
    def update(self):
        pass        
