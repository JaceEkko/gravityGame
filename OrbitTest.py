import pygame
import math
pygame.init()

win=pygame.display.set_mode((500,500))

pygame.display.set_caption("jsdfghirf")

##def move_coords(angle, radius, coords):
##    theta = math.radians(angle)
##    return int(coords[0] + radius * math.cos(theta)), int(coords[1] + radius * math.sin(theta))
class PClass(object):
    def __init__(self, x, y, radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.vel_x=0
        self.vel_y=0
class SClass(object):
    def __init__(self, x, y, radius, mass):
        self.x=x
        self.y=y
        self.radius=radius
        self.mass=mass
def calcGravity(sun, planet): 
  'Returns acceleration of planet with respect to the sun' 
  diff_x = sun.x - planet.x 
  diff_y = sun.y - planet.y 
  acceleration = G * sun.mass / (diff_x ** 2 + diff_y ** 2) 
  accel_x = acceleration * diff_x / (diff_x ** 2 + diff_y ** 2)
  accel_y = acceleration * diff_y / (diff_x ** 2 + diff_y ** 2)
  return accel_x, accel_y

#x=250
#y=250
#radius=2
#angle = 0
dt = 0.01  # size of time step
G = 100 # gravitational constant
planet=PClass(150,150,30)
sun=SClass(250,250,50,10000)

run=True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.circle(win, (0,255,0), (planet.x,planet.y), planet.radius)
    pygame.draw.circle(win, (255,255,0), (sun.x,sun.y), sun.radius)
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
