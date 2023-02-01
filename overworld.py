# cat isle

import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 2732
WINDLENGTH = 2048

BGCOLOR = "white"
TEXTCOLOR = "black"

def main():
    global BASICFONT, IMAGESDICT, PLAYERIMAGES # add global things
    
    pygame.init()
    pygame.display.set_caption('Cat Isle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    IMAGESDICT = {}


    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()



