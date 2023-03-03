# cat maze
from pygame import *
import pygame 
import math
import random as rand
from abc import ABC, abstractmethod 
from pygame.locals import *

pygame.init()
from pygame import mixer
mixer.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('gooddog.ttf', 50)
window = pygame.display.set_mode((WIDTH, HEIGHT))
trophy4 = False

def game4():
    # music
    mixer.music.load("music/game4.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('HangCat?', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # background
    bg = pygame.image.load("game4_images/game4_background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0))
    window.blit(text, textRect)


game4()