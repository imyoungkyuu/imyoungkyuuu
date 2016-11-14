

from pico2d import *

from ball import Ball
from block import Block
from line import Line
from arrow import Arrow
from bonusball import Bonusball

ball = None
arrow = None
block = None
line = None


def enter():
    open_canvas()

    global ball, line, block, arrow

    ball = Ball()
    line = Line()
    block = Block()
    arrow = Arrow()
    pass

def exit():
    close_canvas()



    pass

def update():
    global block, ball, arrow

    block.update()
    arrow.update()
    ball.update()
    pass

def draw():
    global line, block, arrow, ball

    line.draw()
    block.draw()
    arrow.draw()
    ball.draw()
    pass



def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            exit()
        ball.handle_events(event)
        arrow.handle_events(event)



def main():
    enter()

    while (1):
        clear_canvas()

        handle_events()
        update()
        draw()

        update_canvas()

    exit()



if __name__ == '__main__':
    main()