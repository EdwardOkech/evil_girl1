# The game main settings file
# 23-7-2015
# Edward Okech

import pygame, sys
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
# Game's global color virables
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)


# Game sprites
horn_girl_img = pygame.image.load('res/horn_girl.png')
boy_img = pygame.image.load('res/boy.png')
cat_girl_img = pygame.image.load('res/cat_girl.png')
pink_girl_img = pygame.image.load('res/pink_girl.png')
princess_img = pygame.image.load('res/princess.png')
gem_orange_img = pygame.image.load('res/Gem Orange.png')
gem_blue_img = pygame.image.load('res/Gem Blue.png')
gem_green_img = pygame.image.load('res/Gem Green.png')


FPS = 30
fpsClock = pygame.time.Clock()
size = width, height = 640, 480
horn_girl_size = (101,171)
boy_size = 20
princess_size = 20
pink_girl_size = 20
blue_gem_size = 20
green_gem_size = 20
orange_gem_size = 20

#game data structure
horn_girl_rect = pygame.Rect(300, 100,horn_girl_size)


DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('EVIL GIRL 1.0')


horn_girlx = 10
horn_girly = 10
direction = 'right'

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Welcome to Tedd\'s game', True, GREEN, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
