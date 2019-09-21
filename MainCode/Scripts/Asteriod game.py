
import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

bg = pygame.image.load('spaceback.jpg')

width, height = 1280,720
win = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
char = pygame.image.load("astronaut.png")

char = pygame.transform.scale(char,(30,50))
#screen.fill(background_color)
#pygame.display.flip()
run = True
x = 50
y = 460
width = 40
height = 60
vel = 5
clock = pygame.time.Clock()
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
incircle = False
radius = 60
h, k = 400, 200


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

   else:
       left = False
       right = False
       walkCount = 0
   if not (isJump):
       if keys[pygame.K_SPACE]:
           isJump = True

           walkCount = 0
   else:
       if jumpCount >= -5:
           y -= (jumpCount * abs(jumpCount)) * 0.5
           x += 5
           jumpCount -= 1
       else:
           jumpCount = 10
           isJump = False
   if x >= h - radius and x <= h + radius and y >= k-radius and y<= k+ radius:
       incircle = True
   if (incircle):

       y = 200
       x = 340

   win.fill((0,0,0))
   win.blit(bg, (0, 0))
   win.blit(char, (x, y))
   pygame.draw.rect(win,(255,255,255),(0,700, 500,300))
   pygame.draw.rect(win, (255, 255, 255), (550, 700, 500, 300))
   pygame.draw.circle(win,(255,255,255),(1000,550), 20)
   if x >= 0 and x <= 500:
       if y > 700 - height:
           y -= 10
   if x >= 550 and x <= 550+500:
       if y > 700 - height:
           y -= 10
   if x >= 1000 - 20  and x <= 1000+20 and y >= 530 and y <= 570:
       x = 50
       y = 460
       textsurface = myfont.render('YOU WIN', False, (255, 255, 255))
       win.blit(textsurface, (600, 360))
   y += 10
   if y >= 760:
       x = 50
       y = 460
       textsurface = myfont.render('YOU LOSE', False, (255, 255, 255))
       win.blit(textsurface, (600, 360))

   pygame.display.update()
   #redrawGameWindow()
pygame.quit()
#win.blit(char, (x, y))