
import random
from pico2d import *

class Block:
    def __init__(self):
        self.image = load_image('res/block.png')
        self.x = random.randint(60, 740)
        self.y = 470

    def update(self):
        pass

    def draw(self):

        self.image.draw(self.x,self.y)