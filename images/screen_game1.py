#from overworld3 import *
import pygame

pygame.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))
BODYCOLOR = "0D6C8C5"

def game1():
    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('SnakeCat', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # background
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0))
    window.blit(text, textRect)
    x, y = 200, 200
    pygame.draw.rect(window, 'brown', [x, y, 10, 10])

    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        game_over = True