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

    IMAGESDICT = {"background" : pygame.image.load("background.png"), 
                "bush" : pygame.image.load("bush.png"), 
                "cat" : pygame.image.load("cat_sample.png")}

    currentImage = 0
    PLAYERIMAGES = []