from pyglet.gl import *
from pyglet import image
from pyglet.window import key
import os
import random

class pygletApp(pyglet.window.Window):
    def __init__(self):
        super(pygletApp, self).__init__(resizable=True, width=800, height=600, vsync=False)

        glEnable(GL_DEPTH_TEST)

    def update(self):
        self.dispatch_events()
        
    def on_key_press(self, sym, mod):
        if sym == key.ESCAPE:
            self.has_exit = True
        if sym == key.ENTER:
            self.set_fullscreen(not self.fullscreen)
    
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def main():
    louvre = pygletApp()
    
    while not louvre.has_exit:
        louvre.update()
        louvre.draw()
        louvre.flip()

    louvre.close()

if __name__ == '__main__':
    main()
