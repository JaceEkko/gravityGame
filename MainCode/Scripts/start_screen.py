import pygame
pygame.init()

bg = pygame.image.load('spaceback.jpg')
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
#screen.fill(background_color)
#pygame.display.flip()
running = True

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.Font('recharge bd.ttf', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
#whiteStar = pygame.draw.circle(screen, (255,255,255), (0,0), 500)

butt = button((225,225,225),width/3,2*height/3,350,100,'START')

# redraws the window background
def redrawWin():
    screen.blit(bg, [0, 0])
    butt.draw(screen,(0,0,0))
    #whiteStar.draw(screen, (0,0,0))




while running:
    redrawWin()

    #pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if butt.isOver(pos):
                print('clicked the butt')
        if event.type == pygame.MOUSEMOTION:
            if butt.isOver(pos):
                butt.color = (255,0,0)
            else:
                butt.color = (0,255,0)
        x = 20
        y = 20
        for i in range(100):
            redrawWin()
            pygame.draw.circle(screen, (255,255,255), (x,y), 10)
            x += 10
            y += 5
            pygame.time.delay(10)
        pygame.display.update()
