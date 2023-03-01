# from overworld3 import *
import pygame, random, time
pygame.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('gooddog.ttf', 30)
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
    bg = pygame.image.load("game1_images/game1_background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    # snake
    snake_block = 20
    snake_speed = 15

    def your_score(score):
        value = BASICFONT.render("Your Score: " + str(score), True, 'yellow')
        window.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(window, "brown", [x[0], x[1], snake_block, snake_block])
    
    # message function
    def message(msg, color):
        msg = BASICFONT.render(msg, True, color)
        window.blit(msg, [350, 100])

    def gameLoop():
        game_over = False

        food = pygame.image.load('FISHY.png')
        food = pygame.transform.scale(food, (100, 100))

        foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

        x1 = WIDTH / 2
        y1 = HEIGHT / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        while not game_over:
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
            
            # if player hits border
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                victory = False
            x1 += x1_change
            y1 += y1_change
            window.blit(bg, (0,0))
            window.blit(text, textRect)
            window.blit(food, (foodx, foody))

            # snake head
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # if player collides with head of snake
            for x in snake_list[:-1]:
                if x == snake_head:
                    victory = False
    
            # update snake + score
            our_snake(snake_block, snake_list)
            your_score(length_of_snake - 1)
            score = length_of_snake - 1

            pygame.display.update()

            # food
            if (x1 + 70) > foodx and foodx > (x1 - 25) and (y1 + 25) > foody and foody > (y1 - 50):
                foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
                length_of_snake += 1
            clock.tick(snake_speed)

            # if score is over 15
            if score >= 15:
                victory = True

            # player wins
            if victory == True:
                message("You Won! Congratulations!", "brown")
                pygame.display.update()
                return True

            # player loses
            while victory == False:
                window.blit(bg, (0,0))
                message("You Lost! Press Q (Quit) to go back to main screen or C to Play Again", "brown")
                pygame.display.update()
                return False
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        victory = False
                    if event.key == pygame.K_c:
                        gameLoop()


        # game over
        message('You Lost... smh', 'brown')
        pygame.display.update()
        time.sleep(2)
        game_over = True

    gameLoop()