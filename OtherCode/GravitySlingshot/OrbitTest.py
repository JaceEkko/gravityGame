import pygame
import math
from datetime import timedelta
pygame.init()

win=pygame.display.set_mode((500,500))

pygame.display.set_caption("jsdfghirf")

x=250
y=250
width=40
height=40
x2=250
y2=250
width2=200
height2=200
count = 0
force = 1

right = True
down = True

def inRange(xP, yP, xA, yA, width, height):
    xB = False
    yB = False
    within = False
    if(xP > xA and xP < xA + width):
        xB = True
    if(yP > yA and yP < yA + height):
        yB = True
    if xB and yB:
        within = True
    return within


run=True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if inRange(x, y, x2, y2, width2, height2):
        force += 0.03
    else:
        if force > 0:
            force -= 0.03
            
    if x < x2:
        x += force
    elif x > x2:
        x -= force
    if y < y2:
        y += force
    elif y > y2:
        y -= force

    #X Movement
    if x+width < x2+width2 and right:
        x+=1
##    else:
##        right = False
##        
##    if x > x2 and not right:
##        x-=1
##    else:
##        right = True
        
    #Y Movement
##    if y+height < y2+height2 and down:
##        y+=0.1
##    else:
##        down = False
##    if y > y2 and not down:
##        y-=0.1
##    else:
##        down = True
    

    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (x,y, width,height))
    pygame.draw.rect(win, (255,255,0), (x2,y2,width2, height2 ), 1)
    pygame.display.update()

    

pygame.quit()
##dt = 1  # size of time step
##G = 100 # gravitational constant
##
##class Planet(object):
##    def __init__(self,x,y,radius, vel_x, vel_y):
##        self.x=x
##        self.y=y
##        self.radius = radius
##        self.vel_x=vel_x
##        self.vel_y=vel_y
##
##class Sun(object):
##    def __init__(self,x,y,radius, mass):
##        self.x=x
##        self.y=y
##        self.radius = radius
##        self.mass=mass       
##
##def calcGravity(sun, planet): 
##  'Returns acceleration of planet with respect to the sun' 
##  diff_x = sun.x - planet.x 
##  diff_y = sun.y - planet.y 
##  acceleration = G * sun.mass / (diff_x ** 2 + diff_y ** 2) 
##  accel_x = acceleration * diff_x / (diff_x ** 2 + diff_y ** 2)
##  accel_y = acceleration * diff_y / (diff_x ** 2 + diff_y ** 2)
##  return accel_x, accel_y
##
##def reDrawGameWindow():
##    pygame.draw.circle(win, (0,255,255), (planet.x, planet.y), planet.radius)
##    pygame.draw.circle(win, (255,255,0), (sun.x, sun.y), sun.radius)
##    pygame.display.update()
##
##
##planet = Planet(350, 350, 20, 0,0)
##sun = Sun(500,500, 40, 10)
##while True: 
##  # update position based on velocity 
##  planet.x += int(planet.vel_x * dt) 
##  planet.y += int(planet.vel_y * dt)
##
##  print( planet.vel_x , ", " , planet.vel_y)
##
##  # update velocity based on acceleration
##  accel_x, accel_y = calcGravity(sun, planet)
##  planet.vel_x += accel_x * dt
##  planet.vel_y += accel_y * dt
##
##  reDrawGameWindow()
  
##pygame.quit()
