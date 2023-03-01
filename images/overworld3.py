import pygame, random, time, screen_game1, screen_game2, screen_game3, screen_game4
# from pygame import mixer
pygame.init()
# mixer.init()

# GLOBAL VARIABLES
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('gooddog.ttf', 30)
window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

''' music
mixer.music.load("name.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()
'''

# main screen appears at the beginning of the game
SCREEN = "main"

# function for MAIN SCREEN
def main_screen():
    # music
    # pygame.mixer.music.load('theme.wav')

    # add text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('Cat Isle', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # create bg
    bg = pygame.image.load("background2.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    # bushes
    bush = pygame.image.load('bush.png')
    bush1 = pygame.transform.scale(bush, (250, 250))
    bush2 = pygame.transform.scale(bush, (250, 250))
    bush3 = pygame.transform.scale(bush, (250, 250))

    # trees
    tree = pygame.image.load('tree.png')
    tree1 = pygame.transform.scale(tree, (250, 250))
    tree2 = pygame.transform.scale(tree, (250, 250))
    tree3 = pygame.transform.scale(tree, (250, 250))

    # display bg, text, bushes, trees
    window.blit(bg, (0,0))
    window.blit(text, textRect) # create text

    # bushes
    window.blit(bush1, (75, 225))
    window.blit(bush2, (900, 75))
    window.blit(bush3, (385, 525))

    # trees
    window.blit(tree1, (275, 75))
    window.blit(tree1, (1125, 400))
    window.blit(tree1, (850, 520))


    # spawn cat
    window.blit(cat, (x, y))

# create cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 530, 110

def collected_all_trophies():
    pass

loop = True
while loop:
    # switch screens
    if SCREEN == "main":
        main_screen()
    
    if SCREEN == "game1":
        screen_game1.game1()

    if SCREEN == "game2":
        screen_game2.game2()

    if SCREEN == "game3":
        screen_game3.game3()

    if SCREEN == "game4":
        screen_game4.game4()
    
    # quit?
    for event in pygame.event.get():
        if event.type == quit:
            loop = False

    # trophy won?
    if screen_game1.trophy1:
        pass
    if screen_game2.trophy2:
        pass
    if screen_game3.trophy3:
        pass
    if screen_game4.trophy4:
        pass

    # key pressed?
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -130:
        x -= 20
    if keys[pygame.K_RIGHT] and x < 1220:
        x += 20
    if keys[pygame.K_UP] and y > -110:
        y -= 20
    if keys[pygame.K_DOWN] and y < 615:
        y += 20

    # display directions if cat is on portal
    if x < -5 and x > -300 and y < 15 and y > -300 and SCREEN == "main":
        game1_instruct = BASICFONT.render('Press ENTER to go to game 1', True, 'brown')
        rect1 = game1_instruct.get_rect()
        rect1.center = (1470 // 2, 30)
        window.blit(game1_instruct, rect1)

    if x < 2000 and x > 1100 and y < 30 and y > -200 and SCREEN == "main":
        game3_instruct = BASICFONT.render('Press ENTER to go to game 2', True, 'brown')
        rect3 = game3_instruct.get_rect()
        rect3.center = (1470 // 2, 30)
        window.blit(game3_instruct, rect3)    

    if x < 2000 and x > 1100 and y < 2000 and y > 475 and SCREEN == "main":
        game2_instruct = BASICFONT.render('Press ENTER to go to game 3', True, 'brown')
        rect2 = game2_instruct.get_rect()
        rect2.center = (1470 // 2, 30)
        window.blit(game2_instruct, rect2)

    if x < -5 and x > -300 and y < 2000 and y > 475 and SCREEN == "main":
        game4_instruct = BASICFONT.render('Press ENTER to go to game 4', True, 'brown')
        rect4 = game4_instruct.get_rect()
        rect4.center = (1470 // 2, 30)
        window.blit(game4_instruct, rect4)

    # conditions in which screen changes
    if x < -5 and x > -300 and y < 15 and y > -300 and keys[pygame.K_RETURN]:
        SCREEN = "game1"
    
    if x < 2000 and x > 1100 and y < 30 and y > -200 and keys[pygame.K_RETURN]:
        SCREEN = "game2"

    if x < 2000 and x > 1100 and y < 2000 and y > 475 and keys[pygame.K_RETURN]:
        SCREEN = "game3"

    if x < -5 and x > -300 and y < 2000 and y > 475 and keys[pygame.K_RETURN]:
        SCREEN = "game4"

    # collected all trophies?
    if screen_game1.trophy1 and screen_game2.trophy2 and screen_game3.trophy3 and screen_game4.trophy4:
        collected_all_trophies()

    # update display every frame
    pygame.display.flip()

def terminate():
    pygame.quit()

terminate()