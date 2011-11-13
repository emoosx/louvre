import pyglet
from pyglet.gl import *

class Text():
    def __init__(self,text='hello world',x=0,y=0, RGB=(0,0,0)) :

        self.label = pyglet.text.Label(
                text,
                font_name = 'Helvetica',
                font_size = 10,
                color = (int(RGB[0]*255),int(RGB[1]*255),int(RGB[2]*255),255),
                x = x,
                y = y, 
                multiline = True, 
                width = 1000, 
                height = 1000, 
                dpi = 500)

    def update(self,text=None):
        # update the text itself
        if text != None:
            self.label.text=text

    def draw(self):
        # draw our 2d text
        glScalef(0.1, 0.1, 0.1) 
        self.label.draw()

