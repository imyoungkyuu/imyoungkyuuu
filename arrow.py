
from pico2d import *
import math
import json

class Arrow:

    def __init__(self):
        self.image = load_image('res/arrow.png')
        self.x, self.y = 400, 140

        #모든 변수 선언은 여기 self 붙여서
        self.degree = 0
        self.ax, self.ay = 0, 0
        self.LeftButtonDown = False
        self.RightButtonDown = False

    def rad_to_deg(self, radian):
        return radian * 180 / math.pi

    def deg_to_rad(self, degree):
        return degree * math.pi / 180



    def update(self):
        if(self.LeftButtonDown == True):
            if (self.degree < 60 and self.degree >= 0):
                self.degree += 5
                self.ax -= 2
                self.ay -= 2

            elif (self.degree >= -60 and self.degree < 0):
                self.degree += 5
                self.ax -= 2
                self.ay += 2

        elif(self.RightButtonDown == True):
            if (self.degree > -60 and self.degree <= 0):
                self.degree -= 5
                self.ax += 2
                self.ay -= 2

            elif (self.degree > 0 and self.degree <= 60):
                self.degree -= 5
                self.ax += 2
                self.ay += 2


        #print(self.degree)




    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                if (self.LeftButtonDown == False):
                    self.LeftButtonDown = True
                pass

            elif event.key == SDLK_RIGHT:
                if (self.RightButtonDown == False):
                    self.RightButtonDown = True
                pass
            elif event.key == SDLK_SPACE:
                if event.key == SDLK_SPACE:
                    # 각도 계산
                    print(self.degree)
                    print("shoot")
                    pass


        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                if(self.LeftButtonDown == True):
                    self.LeftButtonDown = False
            elif event.key == SDLK_RIGHT:
                if(self.RightButtonDown == True):
                    self.RightButtonDown = False

    def draw(self):

        self.image.rotate_draw(self.deg_to_rad(self.degree), self.x + self.ax, self.y + self.ay)

        #self.image.draw(ax,ay)