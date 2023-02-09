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

    # message function
    def message(msg, color):
        msg = BASICFONT.render(msg, True, color)
        window.blit(msg, [WIDTH/2, HEIGHT/2])

    # background
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    game_over = False

    while not game_over:
        window.blit(bg, (0,0))
        window.blit(text, textRect)
        x1, y1 = 200, 200
        pygame.draw.rect(window, 'brown', [x1, y1, 10, 10])

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over = True

    while game_over:
        message('You Lost... smh', 'brown')

    def Your_score(score):
        pass

    def our_snake(snack_block, snake_list):
        pass

    def gameLoop():
        pass