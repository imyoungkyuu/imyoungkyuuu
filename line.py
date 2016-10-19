from pico2d import *

class Line:
    def __init__(self):
        self.image = load_image('res/line.png')
        self.x = 400
        self.y = 300

    def draw(self):
        self.image.draw(self.x, self.y)