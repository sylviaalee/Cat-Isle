from overworld3 import *

def game1():
    # text
    text = BASICFONT.render('Cat Isle', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)
    
    # window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))