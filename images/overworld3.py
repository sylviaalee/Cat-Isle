import pygame
import screen_game1
import screen_game2
import screen_game3
import screen_game4

pygame.init()

# GLOBAL VARIABLES
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))

# function for MAIN SCREEN
def main_screen():
    # add text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('Cat Isle', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # create bg
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    # display bg + text
    window.blit(bg, (0,0))
    window.blit(text, textRect) # create text

    # add 4 portals
    pygame.draw.circle(window, "aquamarine4", (100, 100), 50)
    pygame.draw.circle(window, "aquamarine4", (1370, 100), 50)
    pygame.draw.circle(window, "aquamarine4", (1370, 750), 50)
    pygame.draw.circle(window, "aquamarine4", (100, 750), 50)

# create cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 200, 200

# main screen appears at the beginning of the game
screen = "main"

loop = True
while loop:
    # switch screens
    if screen == "main":
        main_screen()
    
    if screen == "game1":
        screen_game1.game1()

    if screen == "game2":
        screen_game2.game2()

    if screen == "game3":
        screen_game3.game3()

    if screen == "game4":
        screen_game4.game4()
    
    # spawn cat
    window.blit(cat, (x, y))
    
    # quit?
    for event in pygame.event.get():
        if event.type == quit:
            loop = False

    # key pressed?
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -130:
        x -= 8
    if keys[pygame.K_RIGHT] and x < 1220:
        x += 8
    if keys[pygame.K_UP] and y > -110:
        y -= 8
    if keys[pygame.K_DOWN] and y < 615:
        y += 8

    # display directions if cat is on portal
    if x < 12 and x > -300 and y < 12 and y > -300 and screen == "main":
        game1_instruct = BASICFONT.render('Press ENTER to go to game', True, 'brown')
        rect1 = game1_instruct.get_rect()
        rect1.center = (1470 // 2, 30)
        window.blit(game1_instruct, rect1)

    if x < 200 and x > 1300 and y < 100 and y > -2000 and screen == "main":
        game2_instruct = BASICFONT.render('Press ENTER to go to game', True, 'brown')
        rect2 = game2_instruct.get_rect()
        rect2.center = (1470 // 2, 30)
        window.blit(game2_instruct, rect2)

    if x < 12 and x > -300 and y < 12 and y > -300 and screen == "main":
        game3_instruct = BASICFONT.render('Press ENTER to go to game', True, 'brown')
        rect3 = game3_instruct.get_rect()
        rect3.center = (1470 // 2, 30)
        window.blit(game3_instruct, rect3)

    if x < 12 and x > -300 and y < 12 and y > -300 and screen == "main":
        game4_instruct = BASICFONT.render('Press ENTER to go to game', True, 'brown')
        rect4 = game4_instruct.get_rect()
        rect4.center = (1470 // 2, 30)
        window.blit(game4_instruct, rect4)

    # conditions in which screen changes
    if x < 15 and x > -300 and y < 15 and y > -300 and keys[pygame.K_RETURN]:
        screen = "game1"
    
    if x < 15 and x > -300 and y < 15 and y > -300 and keys[pygame.K_RETURN]:
        screen = "game2"

    if x < 15 and x > -300 and y < 15 and y > -300 and keys[pygame.K_RETURN]:
        screen = "game3"

    if x < 15 and x > -300 and y < 15 and y > -300 and keys[pygame.K_RETURN]:
        screen = "game4"
    

    # update display every frame
    pygame.display.flip()

def terminate():
    pygame.quit()

terminate()