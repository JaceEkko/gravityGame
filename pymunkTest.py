import pymunk
import pygame
from pymunk.pygame_util import DrawOptions
import time

pygame.init()

win=pygame.display.set_mode((1280,720))
pygame.display.set_caption("Physics Test")
options = DrawOptions

space = pymunk.Space()
space.gravity = 0, -1000

body = pymunk.Body(1, 1666)
body.position = 640, 100
poly = pymunk.Poly.create_box(body)

space.add(body, poly)

def on_draw():
    win.clear()
    space.debug_draw(options)

if __name__=="__main__":
    run = True
    while run:
        pygame.display.update()

#space = pymunk.Space()
#space.gravity = 0, -1000

#body = pymunk.Body(1, 1666)
#body.position = 50, 100

#space.add(body)

#while True:
#    space.step(0.02) #increment through the simulation
#    print(body.position)
#    time.sleep(0.5) #a delay .5 seconds
