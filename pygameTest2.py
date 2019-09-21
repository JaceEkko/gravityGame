#What to start with

import pygame
pygame.init()

sWidth = 600
sHeight = 600
win=pygame.display.set_mode((sWidth, sHeight))

pygame.display.set_caption("First Game")

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=3
        self.isJump=False
        self.jumpCount = 10

class asteroid(object):
    def __init__(self, x, y, radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.force=0
        self.forceAdd=1

    def draw(self, win):
        pygame.draw.circle(win, (0,255,0), (self.x, self.y), int(round(self.radius/2)))
        pygame.draw.circle(win, (0,255,255), (self.x, self.y), self.radius, 1)

def inRange(xP, yP, xA, yA, gRange):
    xB = False
    yB = False
    within = False
    if(xP >= xA - gRange and xP <= xA + gRange):
        xB = True
    if(yP >= yA - gRange and yP <= yA + gRange):
        yB = True
    if xB and yB:
        within = True
    return within

ax = 200
ay = 200

#Main Loop
man = player(200,410,64,64)
aster = asteroid(300,200,120)

def reDrawGameWindow():
    win.fill((0,0,255))
    pygame.draw.rect(win, (255,0,0), (man.x,man.y,man.width,man.height))#draws a rectangle in the window, you can also draw circles, etc.
    aster.draw(win)
    pygame.display.update()

run = True
while run:
    pygame.time.delay(10)#include a delay to make things not run too fast
    
    for event in pygame.event.get():#this loop knows all the events that could happen in pygame
        if event.type == pygame.QUIT: #you hit the close button, end game
            run = False

    keys = pygame.key.get_pressed()#this is a list of all the keys
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
    if keys[pygame.K_RIGHT] and man.x < sWidth - man.width:
        man.x += man.vel

    if not(man.isJump):
        if keys[pygame.K_UP] and man.y > 0:
            man.y -= man.vel
        if keys[pygame.K_DOWN] and man.y < sHeight - man.height:
            man.y += man.vel
        if keys[pygame.K_SPACE]:
            man.isJump=True
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1

        else:
            man.isJump = False
            man.jumpCount = 10

    #gravity
    if inRange(man.x, man.y, aster.x, aster.y, aster.radius):
        aster.force += 0.01
    else:
        if aster.force > 0:
            aster.force -= 0.01
        
    if man.x < aster.x:
        man.x += aster.force
    elif man.x > aster.x:
        man.x -= aster.force
    if man.y < aster.y:
        man.y += aster.force
    elif man.y > aster.y:
        man.y -= aster.force

    reDrawGameWindow()
    pygame.display.update()
    
pygame.quit() #closes everything
