import pygame, random, time, screen_game1, screen_game2, screen_game3, screen_game4

pygame.init()

# GLOBAL VARIABLES
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

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
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    # bush
    bush = pygame.image.load('bush.png')
    bush = pygame.transform.scale(bush, (300, 250))

    # display bg + text
    window.blit(bg, (0,0))
    window.blit(text, textRect) # create text
    window.blit(bush, (200, 200))

    # add 4 portals
    pygame.draw.circle(window, "aquamarine4", (100, 100), 50)
    pygame.draw.circle(window, "aquamarine4", (1370, 100), 50)
    pygame.draw.circle(window, "aquamarine4", (1370, 750), 50)
    pygame.draw.circle(window, "aquamarine4", (100, 750), 50)
    
    # spawn cat
    window.blit(cat, (x, y))

# create cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 200, 200

# game 1
def game1():
    clock = pygame.time.Clock()

    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('SnakeCat', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # background
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    # snake
    snake_block = 20
    snake_speed = 20

    game_over = False

    def your_score(score):
        pass

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(window, "brown", [x[0], x[1], snake_block, snake_block])
    
    # message function
    def message(msg, color):
        msg = BASICFONT.render(msg, True, color)
        window.blit(msg, [WIDTH / 2, 100])

    def gameLoop():
        game_over = False
        game_close = False

        foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

        x1 = WIDTH / 2
        y1 = HEIGHT / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        while not game_over:

            while game_close == True:
                window.blit(bg, (0,0))
                message("You Lost! Press Q-Quit or C-Play Again", "brown")
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                            SCREEN = "main"
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            window.blit(bg, (0,0))
            window.blit(text, textRect)
            pygame.draw.rect(window, 'pink', [foodx, foody, snake_block, snake_block])

            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]
 
            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True
    
            our_snake(snake_block, snake_list)

            pygame.display.update()

            if (x1 + 10) > foodx and foodx > (x1 - 10) and (y1 + 10) > foody and foody > (y1 - 10):
                foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
                length_of_snake += 1
            clock.tick(snake_speed)
        
            while game_close == True:
                window.blit(bg, (0,0))
                message("You Lost! Press Q-Quit to go back to main screen or C-Play Again", "brown")
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            main_screen()
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

        # game over
        message('You Lost... smh', 'brown')
        pygame.display.update()
        time.sleep(2)
        game_over = True

    gameLoop()

loop = True
while loop:
    # switch screens
    if SCREEN == "main":
        main_screen()
    
    if SCREEN == "game1":
        game1()

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

    # update display every frame
    pygame.display.flip()

def terminate():
    pygame.quit()

terminate()