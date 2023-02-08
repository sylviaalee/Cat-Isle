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

def main_screen():
    # add text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('Cat Isle', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # window
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0))
    window.blit(text, textRect) # create text
    pygame.draw.rect(window, "red", pygame.Rect(50, 50, 100, 100))

# cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 200, 200

def terminate():
    pygame.quit()

screen = "main"

loop = True
while loop:
    # switch screens
    if screen == "main":
        main_screen()
    
    if screen == "game1":
        screen_game1.game1()
    
    window.blit(cat, (x, y))
    
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

    # conditions in which screen changes
    if x < 15 and x > -300 and y < 15 and y > -300 and keys[pygame.K_RETURN]:
        screen = "game1"

    # display directions
    if x < 12 and x > -300 and y < 12 and y > -300 and screen == "main":
        game1_instruct = BASICFONT.render('Press ENTER to go to game', True, 'brown')
        rect1 = game1_instruct.get_rect()
        rect1.center = (1470 // 2, 30)
        window.blit(game1_instruct, rect1)

    pygame.display.flip()

terminate()