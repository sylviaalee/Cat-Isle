import pygame
import screen_game1
import screen_game2
import screen_game3
import screen_game4

pygame.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))

# add text
pygame.display.set_caption('Cat Isle')
text = BASICFONT.render('Cat Isle', True, 'brown')
textRect = text.get_rect()
textRect.center = (1470 // 2, 850 // 2)

# window
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

# cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 100, 100

loop = True
while loop:
    window.blit(bg, (0,0))
    window.blit(cat, (x, y))
    window.blit(text, textRect) # create text

    for event in pygame.event.get():
        if event.type == quit:
            loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -130:
        x -= 8
    if keys[pygame.K_RIGHT] and x < 1200:
        x += 8
    if keys[pygame.K_UP] and y > -110:
        y -= 8
    if keys[pygame.K_DOWN] and y < 600:
        y += 8
    pygame.display.flip()

pygame.quit()