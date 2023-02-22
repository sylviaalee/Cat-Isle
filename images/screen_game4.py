# from overworld3 import *
import pygame

pygame.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))

def game4():
    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('CatMaze', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # background
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0))
    window.blit(text, textRect)

     
    class Maze:
        def __init__(self):
            self.M = 10
            self.N = 8
            maze = [1,1,1,1,1,1,1,1,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,1,1,1,1,1,1,0,1,
                    1,0,1,0,0,0,0,0,0,1,
                    1,0,1,0,1,1,1,1,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,1,1,1,1,1,1,1,1,]

        def draw(self,display_surf,image_surf):
            bx = 0
            by = 0
            for i in range(0,self.M*self.N):
                if self.maze[ bx + (by*self.M) ] == 1:
                    display_surf.blit(image_surf,( bx * 44 , by * 44))
        
                bx = bx + 1
                if bx > self.M-1:
                    bx = 0
                    by = by + 1