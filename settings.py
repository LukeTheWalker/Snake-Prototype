from random import *
import pygame
from pygame.locals import *
import time

pygame.init()

size = 50

thicc = 15
border = size-thicc
translation_vector = (0,100)

display_width = 800
display_height = 600
game_display_width =  display_width - translation_vector[0]
game_display_height =  display_height - translation_vector [1]

x = 100
y = 100

gameDisplay = pygame.display.set_mode((display_width,display_height), RESIZABLE)
gameDisplay.fill((0,0,0)) #black in RGB


gameExit = False

x_change = 0
y_change = 0
speed = 0.15

snake_l = 4
direction = 0
snake = [ (randint(-10000, -1),randint(-10000, -1),0) for pieces in range (snake_l)]
t0 = time.clock()
r = randint(0,3)

#head = [pygame.image.load('./snake-graphics/head_left.png'), pygame.image.load('./snake-graphics/head_left.png'),pygame.image.load('./snake-graphics/head_right.png'), pygame.image.load('./snake-graphics/head_up.png'), pygame.image.load('./snake-graphics/head_down.png')]
head = pygame.image.load('./snake-graphics/head_left.png')
vertical_body = pygame.image.load('./snake-graphics/vertical-body.png')
tail=pygame.image.load('./snake-graphics/tail.png')
curva = pygame.image.load('./snake-graphics/curva.png')
food = [pygame.image.load('./snake-graphics/cibo'+ str (i)+'.png')for i in range (4)]
gameicon = pygame.image.load('./snake-graphics/icon.png')
pygame.display.set_icon(gameicon)

        
for i in range (size):
    if (game_display_width + i) % size == 0:
        game_display_width += i

for i in range (size):
    if (game_display_height + i) % size == 0:
        game_display_height += i