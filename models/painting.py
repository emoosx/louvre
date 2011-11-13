from pyglet.gl import *
from pyglet import image
import os

class painting:
    def __init__(self, width, height, image_file):
        self.width = width
        self.height = height
        self.image_file = image_file
        self.label_text = """
            Starry Night by
            Van Goh
        """
