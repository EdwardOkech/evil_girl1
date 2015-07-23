# A simple pygame game
# 23-7-2015
# Edward Okech

import pygame, sys
from pygame.locals import *
from game.settings import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Game')

WHITE = (255, 255, 255)
horn_girl_img = pygame.image.load('res/horn_girl.png')
horn_girlx = 10
horn_girly = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        horn_girlx += 5
        if horn_girlx == 280:
            direction = 'down'
    elif direction == 'down':
        horn_girly += 5
        if horn_girly == 220:
            direction = 'left'
    elif direction == 'left':
        horn_girlx -= 5
        if horn_girlx == 10:
            direction = 'up'
    elif direction == 'up':
        horn_girly -= 5
        if horn_girly == 10:
            direction = 'right'

    DISPLAYSURF.blit(horn_girl_img, (horn_girlx, horn_girly))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
