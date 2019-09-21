import math

import pygame
pygame.init()

bg = pygame.image.load('spaceback.jpg')

width, height = 1280,720
win = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
char = pygame.image.load("astronaut.png")

char = pygame.transform.scale(char,(30,50))


class Block(pygame.sprite.Sprite):
    """ This class represents the ball that moves in a circle. """

    def __init__(self, color, width, height):
        """ Constructor that create's the ball's image. """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # The "center" the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        # Current angle in radians
        self.angle = 0

        # How far away from the center to orbit, in pixels
        self.radius = 0

        # How fast to orbit, in radians per frame
        self.speed = 0.05

    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y

        # Increase the angle in prep for the next round.
        self.angle += self.speed

#screen.fill(background_color)
#pygame.display.flip()
right= True
run = True
x = 300
y = 200
width = 40
height = 60
vel = 5
clock = pygame.time.Clock()
isJump = False
jumpCount = 10
up = True
right = True
walkCount = 0

radius = 100
h, k = 400, 200
#circle = pygame.draw.circle(win, (255,255,255),(h,k), radius, 1)

#def redrawGameWindow():
 #  global walkCount
  # win.blit(bg, (0, 0))
   #if walkCount + 1 >= 27:
    #   walkCount = 0
   #if left:
   #    win.blit(walkLeft[walkCount // 3], (x, y))
       #walkCount += 1
   #elif right:
   #    win.blit(walkRight[walkCount // 3], (x, y))
   #    walkCount += 1
   #else:
   #    win.blit(char, (x, y))
   #    walkCount = 0
   #pygame.display.update()
run = True
inOrbit = False
while run:
   clock.tick(27)


   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT] and x > vel:
       x -= vel

   elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
       x += vel


   if not (isJump):
       if keys[pygame.K_SPACE]:
           isJump = True

   else:
       # X Move
       if x <= h+radius and right:
           x += 5
           neg = -1
           if x >= h:
               neg = 1
           if y <= k+radius and up:
              y -= neg * radius**2 - ((x-h)**2)+k
           #print ("x: " + x)
           print (f"X: {x}, Y: {y}")

           #print (y)()
           '''else:
               up = False
           if y <= k + radius and not up:
               y += radius * math.sin(5) + k
           else:
               up = True'''
       else:
           right = False

       '''if x >= h - radius and not right :
           x -= 5
           y += radius*math.sin(5) + k
           if y >= k-radius and not up:
               y -= radius*math.sin(5)+ k
           else:
               up = True
           if y >= k - radius and up:
               y+= radius *math.sin(5)+k
           else:
               up = False
       else:
            right = True'''
       #isJump = False



   win.fill((0,0,0))
   win.blit(bg, (0, 0))
   astro = win.blit(char, (x, y))

   #move_circle(astro)

   pygame.draw.circle(win,(255,255,255),(h,k),radius,1)
   pygame.display.update()
   #redrawGameWindow()
pygame.quit()
