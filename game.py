# A simple pygame game
# 23-7-2015
# Edward Okech

import pygame, sys, time
from pygame.locals import *
from settings import *
import random

######################Todo evil girl class code.
##class EvilGirl:
##    def __init__(self, screen, boy):
##        self.boy = boy
##        self.screen = screen
##        self.image = pygame.image.load('res/horn_girl.png')
##        self.spawn()
##
##    def spawn(self):
##        collision = True
##
##        while collision:
##            evil_girl_random_x = random.randrange(0, width, evil_girl_size)
##            evil_girl_random_y = random.randrange(0, height, evil_girl_size)
##
##            collision = False
##
##            if evil_girl_random_x and evil_girl_random_y == boy_random_x and boy_random_y:
##                collision = True
##
##        self.position = self.image.get_rect().move(evil_girl_random_x, evil_girl_random_y)
##        self.blit()
##
##    def blit(self):
##        self.screen.blit(self.image, self.position)

horn_girl_stretched_img = pygame.transform.scale(horn_girl_img,(horn_girl_size))
gems = []
for i in range(20):
    gems.append(pygame.Rect(random.randint(0,width - 20), random.randint(0, height - 20), 20, 20))

gem_counter = 0
NEWGEM = 40

move_left = False
move_right = False
move_up = False
move_down = False

MOVESPEED = 6

##################Game sounds
##pick_up_sound = pygame.mixer.Sound('sound1.wav')
##pygame.mixer.music.load('sound2.mid')
##pygame.mixer.music.play(-1,0.0)
##music_playing = True




            
            





while True:
    DISPLAYSURF.fill(WHITE)
##    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    DISPLAYSURF.blit(horn_girl_img, (horn_girlx, horn_girly))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                move_right = False
                move_left = True
            if event.key == K_RIGHT or event.key == ord('d'):
                move_left = False
                move_right = True
            if event.key == K_UP or event.key == ord('w'):
                move_down = False
                move_up = True
            if event.key == K_DOWN or event.key == ord('s'):
                move_up = False
                move_down = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                move_left =False
            if event.key == K_RIGHT or event.key == ord('d'):
                move_right =False
            if event.key == K_UP or event.key == ord('w'):
                move_up =False
            if event.key == K_DOWN or event.key == ord('s'):
                move_down =False
            if event.key == ord('x'):
                horn_girl_rect.top = random.randint(0, height - horn_girl_rect.
            
        

    pygame.display.update()
    fpsClock.tick(FPS)
