import time
import pygame, sys 
from pygame.locals import *
pygame.init()  
# set up the window 
DISPLAYSURF = pygame.display.set_mode((1000, 800), 0, 32) 
pygame.display.set_caption('Drawing') 
# set up the colors 
BLACK = ( 0, 0, 0) 
WHITE = (255, 255, 255)
RED = (255, 0, 0) 
GREEN = ( 0, 255, 0) 
BLUE = ( 0, 0, 255) 
# draw on the surface object 
DISPLAYSURF.fill(WHITE)
pygame.display.update()


#FUNÇÕES
def rect():#sem uso por enquanto
    pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
def aumentoProg(x, k, n = 1, i = 1):#(intervalo de crescimento, ciclos de crescimento, aumento(soma), inicio)
    while(i<=k):
        pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 10*i, 5*i))
        time.sleep(x)
        i=i+n
        pygame.display.update()

def movX():#Errado
    i = 1
    while(i<=5):
        rect().right = rect().right + 2
        rect().left = rect().left +2
# FIM FUNÇÕES

#EXECUÇÕES
aumentoProg(1,20)
#movX()
#FIM EXECUÇÕES



# run the game loop 
while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
pygame.display.update()
