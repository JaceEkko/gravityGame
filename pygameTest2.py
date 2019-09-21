#What to start with

import pygame
pygame.init()

sWidth = 1280
sHeight = 720
win=pygame.display.set_mode((sWidth, sHeight))

pygame.display.set_caption("First Game")

bg = pygame.image.load('bg1.jpg')
ast1 = pygame.image.load('a1.png')

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velX=0
        self.velY=0
        self.isJump=False
        self.jumpCount = 10

class asteroid(object):
    def __init__(self, x, y, radius, forceCap):
        self.x=x
        self.y=y
        self.radius=radius
        self.force=0
        self.forceAdd=(forceCap/10)
        self.forceCap=forceCap

    def draw(self, win):
        win.blit(ast1, (self.x - self.radius/2, self.y- self.radius/2))#pygame.draw.circle(win, (0,255,0), (self.x, self.y), int(round(self.radius/2)))
        pygame.draw.circle(win, (0,255,255), (self.x, self.y), self.radius, 1)

def inRange(xP, yP, xA, yA, gRange):
    xB = False
    yB = False
    within = False
    if(xP > xA - gRange and xP < xA + gRange):
        xB = True
    if(yP > yA - gRange and yP < yA + gRange):
        yB = True
    if xB and yB:
        within = True
    return within

ax = 200
ay = 200

#Main Loop
man = player(10,10,64,64)
asterLst = [asteroid(400,400,200, 10), asteroid(800,400,200, 20)]

def reDrawGameWindow():
    win.blit(bg, (0,0))#win.fill((0,0,255))
    pygame.draw.rect(win, (255,0,0), (man.x,man.y,man.width,man.height))#draws a rectangle in the window, you can also draw circles, etc.
    for a in asterLst:
        a.draw(win)#aster.draw(win)
    pygame.display.update()

run = True
while run:
    pygame.time.delay(5)#include a delay to make things not run too fast

    mCoords = pygame.mouse.get_pos()

    man.x += man.velX
    man.y += man.velY
    for event in pygame.event.get():#this loop knows all the events that could happen in pygame
        if event.type == pygame.QUIT: #you hit the close button, end game
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            man.velX = (mCoords[0] - man.x)/100
            man.velY = (mCoords[1] - man.y)/100

        
    #print(pygame.mouse.get_pos())
      

##    keys = pygame.key.get_pressed()#this is a list of all the keys
##    if keys[pygame.K_LEFT] and man.x > 0:
##        man.x -= man.vel
##    if keys[pygame.K_RIGHT] and man.x < sWidth - man.width:
##        man.x += man.vel
    
##    if keys[pygame.K_UP] and man.y > 0:
##        man.y -= man.vel + a.force
##    if keys[pygame.K_DOWN] and man.y < sHeight - man.height:
##        man.y += man.vel + a.force
##    if keys[pygame.K_SPACE]:
##        man.isJump=True
    
    #gravity
    for a in asterLst:
        man.y += a.force
        man.x += a.force
        a.draw(win)
        if inRange(man.x, man.y, a.x, a.y, a.radius):
            if man.y < a.y and a.force < a.forceCap:
                a.force += a.forceAdd
            elif man.y > a.y and a.force > -a.forceCap:
                a.force -= a.forceAdd
            if man.x < a.x and a.force < a.forceCap:
                a.force += a.forceAdd
            elif man.x > a.x and a.force > -a.forceCap:
                a.force -= a.forceAdd
         #else:
            #if a.force > 0:
                #a.force -= a.forceAdd

##    if keys[pygame.K_UP] and man.y > 0:
##        man.y -= man.vel + a.force
##    if keys[pygame.K_DOWN] and man.y < sHeight - man.height:
##        man.y += man.vel + a.force
##    if keys[pygame.K_SPACE]:
##        man.isJump=True
            
        
    reDrawGameWindow()
    pygame.display.update()
    
pygame.quit() #closes everything
