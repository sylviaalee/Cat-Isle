# cat isle

import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 1470
WINLENGTH = 850

BGCOLOR = "white"
TEXTCOLOR = "black"

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Player(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill('red')
        self.image.set_colorkey('red')
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
  
  


def main():
    
    global BASICFONT, IMAGESDICT, PLAYERIMAGES, window, bg # add global variables
    
    pygame.init()
    pygame.display.set_caption('Cat Isle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    bg = pygame.image.load("background.png")
    window = pygame.display.set_mode((WINWIDTH, WINLENGTH))
    bg = pygame.transform.scale(bg,(WINWIDTH, WINLENGTH))

    IMAGESDICT = {'background' : pygame.image.load("background.png"), 
                'bush' : pygame.image.load("bush.png"), 
                'cat' : pygame.image.load("cat_sample.png")}

    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['cat']]


    all_sprites_list = pygame.sprite.Group()
    
    object_ = Player('red', 20, 30)
    object_.rect.x = 200
    object_.rect.y = 300
    
    all_sprites_list.add(object_)

    all_sprites_list.update()
    all_sprites_list.draw(window)

    result = runGame()


def runGame():
    # add levels and levelNum as parameters later!!

    while True: # main game loop
        window.blit(bg,(0,0))
        cat = pygame.image.load('cat_sample.png')
        window.blit(cat, (0, 0)) # create sprite

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
    
        playerMoveTo = None
        keyPressed = False
        for event in pygame.event.get(): # event handling loop
            if event.type == pygame.QUIT:
            # Player clicked the "X" at the corner of the window.
                terminate()

            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                keyPressed = True
                if event.key == pygame.K_LEFT:
                    playerMoveTo = LEFT
                elif event.key == pygame.K_RIGHT:
                    playerMoveTo = RIGHT
                elif event.key == pygame.K_UP:
                    playerMoveTo = UP
                elif event.key == pygame.K_DOWN:
                    playerMoveTo = DOWN

                elif event.key == pygame.K_ESCAPE:
                    # escape key quits
                    terminate()

                elif event.key == pygame.K_p:
                    # change player image to next one.
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        # after last player image use first one
                        currentImage = 0
                
        pygame.display.update() 

def displayScreen():
    pass

def isBlocked():
    pass

def isGameFinished():
    pass

# should be at end of file
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()