
from pico2d import *
from arrow import Arrow


class Ball:

    def __init__(self):
        self.image = load_image('res/ball.png')
        self.x = 400
        self.y = 96
        self.ax = 0
        self.ay = 0
        self.shootdegree = 0

    def update(self):
        pass

    def handle_events(self, event):
        pass


    def draw(self):

        self.image.draw(self.x + self.ax, self.y + self.ay)