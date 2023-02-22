# from overworld3 import *
import pygame, random, time
pygame.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))
BODYCOLOR = "0D6C8C5"
SCREEN = "game1"

clock = pygame.time.Clock()

def game1():
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