import pygame
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Lunacy")
astronaut = pygame.image.load('astronaut.png')
bg = pygame.image.load('bg2.jpg')
ast = [pygame.image.load('a1.png'), pygame.image.load('a2.png'), pygame.image.load('a3.png')]
x = 50
y = 50
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
   global walkCount
   win.blit(bg, (0, 0))
   redrawGameWindow()

run = True
while run:
    pass
pygame.quit()
