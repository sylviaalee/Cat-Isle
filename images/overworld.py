# cat isle

import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 2732
WINLENGTH = 2048

BGCOLOR = "white"
TEXTCOLOR = "black"

def main():
    global BASICFONT, IMAGESDICT, PLAYERIMAGES # add global things
    
    pygame.init()
    pygame.display.set_caption('Cat Isle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    bg = pygame.image.load("background.png")

    IMAGESDICT = {"background" : pygame.image.load("background.png"), 
                "bush" : pygame.image.load("bush.png"), 
                "cat" : pygame.image.load("cat_sample.png")}

    currentImage = 0
    PLAYERIMAGES = []
    IMAGESDICT = {}

    window = pygame.display.set_mode((WINWIDTH, WINLENGTH))
    while True: # main game loop
        window.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()



# should be at end of file
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()