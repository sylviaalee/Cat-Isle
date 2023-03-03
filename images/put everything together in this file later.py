import pygame, random, time, screen_game1, screen_game2, screen_game3, screen_game4
from pygame import mixer
pygame.init()
mixer.init()

# GLOBAL VARIABLES
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('gooddog.ttf', 30)
window = pygame.display.set_mode((WIDTH, HEIGHT))
currentImage = 0
PLAYERIMAGES = [pygame.image.load('cat.png'),
                pygame.image.load('cat_w_hat.png'),
                pygame.image.load('cat_w_glasses.png'),
                pygame.image.load('cat_w_clothes.png')]

clock = pygame.time.Clock()

mixer.music.load("music/main_theme.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

# main screen appears at the beginning of the game
SCREEN = "main"

trophy1 = False
trophy2 = False
trophy3 = False
trophy4 = False

# snakecat
def game1():
    # music
    mixer.music.load("music/game1.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    get_trophy = crash_sound = pygame.mixer.Sound("music/get_trophy.mp3")

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
        value = BASICFONT.render("Your Score: " + str(score), True, 'gold')
        window.blit(value, [50, 50])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(window, "brown", [x[0], x[1], snake_block, snake_block])
    
    # message function
    def message(msg, color):
        msg = BASICFONT.render(msg, True, color)
        window.blit(msg, [350, 100])

    def gameLoop():
        global trophy1
        trophy1 = False

        victory = ''
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
            if score >= 2:
                victory = True

            # player wins
            if victory == True:
                trophy1 = True
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(get_trophy)
                window.blit(bg, (0,0))
                message("You Won the Spring Trophy! Congratulations! Press Q to go back to the main screen.", "brown")
                pygame.display.update()
            

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            # go back to main_screen
                            loop()
            # player loses
            while victory == False:
                window.blit(bg, (0,0))
                message("You Lost! Press Q (Quit) to go back to main screen or C to Play Again", "brown")
                #pygame.display.update()
                #game_over = True

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            # go back to main_screen
                            loop()
                        if event.key == pygame.K_c:
                            gameLoop()

            
            #if game_over == True:
               # exit()
            

    gameLoop()

# cat sweeper
def game2():
    # music
    mixer.music.load("music/game2.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('CatSweeper', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # background
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0))
    window.blit(text, textRect)

    grid_color = (128, 128, 128)

    numMine = 9  # Number of mines
    grid_size = 32  # Size of grid (WARNING: make sure to change the images dimension as well)
    border = 16  # Top border
    top_border = 100  # Left, Right, Bottom border
    display_width = grid_size * WIDTH + border * 2  # Display width
    display_height = grid_size * HEIGHT + border + top_border  # Display height
    gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
    timer = pygame.time.Clock()  # Create timer

    # Import files
    spr_emptyGrid = pygame.image.load("game2_images/empty.png")
    spr_flag = pygame.image.load("game2_images/flag.png")
    spr_grid = pygame.image.load("game2_images/Grid.png")
    spr_grid1 = pygame.image.load("game2_images/grid1.png")
    spr_grid2 = pygame.image.load("game2_images/grid2.png")
    spr_grid3 = pygame.image.load("game2_images/grid3.png")
    spr_grid4 = pygame.image.load("game2_images/grid4.png")
    spr_grid5 = pygame.image.load("game2_images/grid5.png")
    spr_grid6 = pygame.image.load("game2_images/grid6.png")
    spr_grid7 = pygame.image.load("game2_images/grid7.png")
    spr_grid8 = pygame.image.load("game2_images/grid8.png")
    spr_grid7 = pygame.image.load("game2_images/grid7.png")
    spr_mine = pygame.image.load("game2_images/mine.png")
    spr_mineClicked = pygame.image.load("game2_images/mineClicked.png")
    spr_mineFalse = pygame.image.load("game2_images/mineFalse.png")


    # Create global values
    grid = []  # The main grid
    mines = []  # Pos of the mines


    # Create function to draw texts
    def drawText(txt, s, yOff=0):
        screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
        rect = screen_text.get_rect()
        rect.center = (WIDTH * grid_size / 2 + border, HEIGHT * grid_size / 2 + top_border + yOff)
        gameDisplay.blit(screen_text, rect)


    # Create class grid
    class Grid:
        def __init__(self, xGrid, yGrid, type):
            self.xGrid = xGrid  # X pos of grid
            self.yGrid = yGrid  # Y pos of grid
            self.clicked = False  # Boolean var to check if the grid has been clicked
            self.mineClicked = False  # Bool var to check if the grid is clicked and its a mine
            self.mineFalse = False  # Bool var to check if the player flagged the wrong grid
            self.flag = False  # Bool var to check if player flagged the grid
            # Create rectObject to handle drawing and collisions
            self.rect = pygame.Rect(border + self.xGrid * grid_size, top_border + self.yGrid * grid_size, grid_size, grid_size)
            self.val = type  # Value of the grid, -1 is mine

        def drawGrid(self):
            # Draw the grid according to bool variables and value of grid
            if self.mineFalse:
                gameDisplay.blit(spr_mineFalse, self.rect)
            else:
                if self.clicked:
                    if self.val == -1:
                        if self.mineClicked:
                            gameDisplay.blit(spr_mineClicked, self.rect)
                        else:
                            gameDisplay.blit(spr_mine, self.rect)
                    else:
                        if self.val == 0:
                            gameDisplay.blit(spr_emptyGrid, self.rect)
                        elif self.val == 1:
                            gameDisplay.blit(spr_grid1, self.rect)
                        elif self.val == 2:
                            gameDisplay.blit(spr_grid2, self.rect)
                        elif self.val == 3:
                            gameDisplay.blit(spr_grid3, self.rect)
                        elif self.val == 4:
                            gameDisplay.blit(spr_grid4, self.rect)
                        elif self.val == 5:
                            gameDisplay.blit(spr_grid5, self.rect)
                        elif self.val == 6:
                            gameDisplay.blit(spr_grid6, self.rect)
                        elif self.val == 7:
                            gameDisplay.blit(spr_grid7, self.rect)
                        elif self.val == 8:
                            gameDisplay.blit(spr_grid8, self.rect)

                else:
                    if self.flag:
                        gameDisplay.blit(spr_flag, self.rect)
                    else:
                        gameDisplay.blit(spr_grid, self.rect)

        def revealGrid(self):
            self.clicked = True
            # Auto reveal if it's a 0
            if self.val == 0:
                for x in range(-1, 2):
                    if self.xGrid + x >= 0 and self.xGrid + x < WIDTH:
                        for y in range(-1, 2):
                            if self.yGrid + y >= 0 and self.yGrid + y < HEIGHT:
                                if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                    grid[self.yGrid + y][self.xGrid + x].revealGrid()
            elif self.val == -1:
                # Auto reveal all mines if it's a mine
                for m in mines:
                    if not grid[m[1]][m[0]].clicked:
                        grid[m[1]][m[0]].revealGrid()

        def updateValue(self):
            # Update the value when all grid is generated
            if self.val != -1:
                for x in range(-1, 2):
                    if self.xGrid + x >= 0 and self.xGrid + x < WIDTH:
                        for y in range(-1, 2):
                            if self.yGrid + y >= 0 and self.yGrid + y < HEIGHT:
                                if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                    self.val += 1


    def gameLoop():
        gameState = "Playing"  # Game state
        mineLeft = numMine  # Number of mine left
        global grid  # Access global var
        grid = []
        global mines
        t = 0  # Set time to 0

        # Generating mines
        mines = [[random.randrange(0, WIDTH),
                random.randrange(0, HEIGHT)]]

        for c in range(numMine - 1):
            pos = [random.randrange(0, WIDTH),
                random.randrange(0, HEIGHT)]
            same = True
            while same:
                for i in range(len(mines)):
                    if pos == mines[i]:
                        pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
                        break
                    if i == len(mines) - 1:
                        same = False
            mines.append(pos)

        # Generating entire grid
        for j in range(HEIGHT):
            line = []
            for i in range(WIDTH):
                if [i, j] in mines:
                    line.append(Grid(i, j, -1))
                else:
                    line.append(Grid(i, j, 0))
            grid.append(line)

        # Update of the grid
        for i in grid:
            for j in i:
                j.updateValue()

        # Main Loop
        while gameState != "Exit":
            # User inputs
            for event in pygame.event.get():
                # Check if player close window
                if event.type == pygame.QUIT:
                    gameState = "Exit"
                # Check if play restart
                if gameState == "Game Over" or gameState == "Win":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            gameState = "Playing"
                            gameLoop()
                else:
                    if event.type == pygame.MOUSEBUTTONUP:
                        for i in grid:
                            for j in i:
                                if j.rect.collidepoint(event.pos):
                                    if event.button == 1:
                                        # If player left clicked of the grid
                                        j.revealGrid()
                                        # Toggle flag off
                                        if j.flag:
                                            mineLeft += 1
                                            j.falg = False
                                        # If it's a mine
                                        if j.val == -1:
                                            gameState = "Game Over"
                                            j.mineClicked = True
                                    elif event.button == 3:
                                        # If the player right clicked
                                        if not j.clicked:
                                            if j.flag:
                                                j.flag = False
                                                mineLeft += 1
                                            else:
                                                j.flag = True
                                                mineLeft -= 1

            # Check if won
            w = True
            for i in grid:
                for j in i:
                    j.drawGrid()
                    if j.val != -1 and not j.clicked:
                        w = False
            if w and gameState != "Exit":
                gameState = "Win"

            # Draw Texts
            if gameState != "Game Over" and gameState != "Win":
                t += 1
            elif gameState == "Game Over":
                drawText("Game Over!", 50)
                drawText("R to restart", 35, 50)
                for i in grid:
                    for j in i:
                        if j.flag and j.val != -1:
                            j.mineFalse = True
            else:
                you_won()
            # Draw time
            s = str(t // 15)
            screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))
            gameDisplay.blit(screen_text, (border, border))
            # Draw mine left
            screen_text = pygame.font.SysFont("Calibri", 50).render(mineLeft.__str__(), True, (0, 0, 0))
            gameDisplay.blit(screen_text, (display_width - border - 50, border))

            pygame.display.update()  # Update screen

            timer.tick(15)  # Tick fps

    def you_won():
        # play animation
        drawText("You WON!", 50)
        drawText("C to go back to main screen", 35, 50)

    gameLoop()
    pygame.quit()
    quit()

# flappy cat
def game3():
    global trophy3

    trophy3 = False

    # music
    mixer.music.load("music/game3.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # creating an object of the Clock() class of the pygame.time module  
    game_clock = pygame.time.Clock()  
    
    # defining the fps for the game  
    game_fps = 60  
    
    # defining the width and height of the game screen  
    SCREEN_WIDTH = 1470  
    SCREEN_HEIGHT = 850  
    
    # using the set_mode() function of the pygame.display module to set the size of the screen  
    display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    
    # setting the title of the application using the set_caption() function  
    pygame.display.set_caption('Flappy Cat')  
    
    # defining the font style  
    fontStyle = pygame.font.Font('gooddog.ttf', 50)  
    
    # defining the font color  
    black = (0, 0, 0)  
    
    # declaring and initializing the game variables  
    baseScroll = 0  
    scrollSpeed = 4  
    birdFlying = False  
    gameOver = False  
    pipeGap = 150  
    pipeFrequency = 1450 # milliseconds  
    lastPipe = pygame.time.get_ticks() - pipeFrequency  
    playerScore = 0  
    passPipe = False  
    victory = False
    
    # loading images  
    background = pygame.image.load('game3_images/game3_background.png')  
    background = pygame.transform.scale(background,(SCREEN_WIDTH, SCREEN_HEIGHT))
    base = pygame.image.load('game3_images/base.png')
    base = pygame.transform.scale(base, (1800, 300)) 
    button = pygame.image.load('game3_images/restart.png')  
    
    # defining a function to draw the text on the screen  
    def drawText(text, fontStyle, textColor, x_coordinate, y_coordinate):  
        # using the render() function to render the text as image  
        image = fontStyle.render(text, True, textColor)  
    
        # using the blit() function to display the image on the screen  
        display_screen.blit(image, (x_coordinate, y_coordinate))  
    
    # defining a function to reset the game  
    def resetGame():  
        # calling the empty() function to remove all the sprites  
        pipeGroup.empty()  
        # describing the coordinates for the rectangle placement  
        bird.rect.x = 200  
        bird.rect.y = int(SCREEN_HEIGHT / 2)  
        # setting the player score to 0  
        playerScore = 0  
        # returning the score  
        return playerScore  
    
    # creating a class of the pygame's Sprite() class to display the bird  
    class FlappyBird(pygame.sprite.Sprite):  
        # defining an initializing function  
        def __init__(self, x_coordinate, y_coordinate):  
            pygame.sprite.Sprite.__init__(self)  
    
            # creating an empty list  
            self.image_list = []  
            # setting the index and counter value to 0  
            self.index = 0  
            self.counter = 0  
    
            # iterating through the range of 1 to 4  
            for i in range(1, 4):  
                # loading the sprite bird images from the directory  
                # using the load() function of the pygame.image module  
                image = pygame.image.load(f'game3_images/bird_{i}.png')  
                
                # using the append() function to add the image to the list  
                self.image_list.append(image)  
    
            # setting the current image  
            self.image = self.image_list[self.index]  
            
            # creating a rectangle to place the bird image  
            self.rect = self.image.get_rect()  
    
            # setting the position of the bird  
            self.rect.center = [x_coordinate, y_coordinate]  
    
            # defining the initial velocity of the bird  
            self.velocity = 0  
            self.pressed = False  
        
        # defining a function to handle the animation  
        def update(self):  
            # if the bird is flying then run this code  
            if birdFlying == True:  
                # adding gravity to the bird  
                # incrementing the velocity of the bird  
                self.velocity += 0.5  
    
                # if the velocity of the bird is greater than 8.5  
                # then set the final value to 8.5  
                if self.velocity > 8.5:  
                    self.velocity = 8.5  
                # if the rectangle's bottom is less than 576  
                # then increment its y-axis value by velocity's integer value   
                if self.rect.bottom < 576:  
                    self.rect.y += int(self.velocity)  
    
            # if the game is not over then run this code  
            if gameOver == False:  
                # if the mouse button is clicked  
                if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:  
                    # setting the pressed variable value to True  
                    self.pressed = True  
                    # setting the velocity to -10  
                    self.velocity = -10  
    
                # if the mouse button is released  
                if pygame.mouse.get_pressed()[0] == 0:  
                    # setting the pressed variable value to False  
                    self.pressed = False  
    
                # updating the counter by 1  
                self.counter += 1  
                # defining a variable to display the sprite cooldown  
                flapCooldown = 5  
    
                # if the counter value is greater than the cooldown  
                # value set the counter value to 0  
                if self.counter > flapCooldown:  
                    self.counter = 0  
                    
                    # updating the index value by 1  
                    self.index += 1  
    
                    # if the index value is greater than or equal to the  
                    # length of the list, set the index value to 0  
                    if self.index >= len(self.image_list):  
                        self.index = 0  
    
                # updating the current image  
                self.image = self.image_list[self.index]  
                
                # rotating the bird  
                self.image = pygame.transform.rotate(self.image_list[self.index], self.velocity * -2)  
            # if the game is over  
            else:  
                # rotating the bird to -90  
                self.image = pygame.transform.rotate(self.image_list[self.index], -90)  
    
    # creating a class of the pygame's Sprite() class to display the pipes  
    class Pipe(pygame.sprite.Sprite):  
        # defining an initializing function  
        def __init__(self, x_coordinate, y_coordinate, position):  
            pygame.sprite.Sprite.__init__(self)  
            # loading the sprite pipe image from the directory  
            # using the load() function of the pygame.image module  
            self.image = pygame.image.load('game3_images/pipe.png')  
            
            # creating a rectangle to place the pipe image  
            self.rect = self.image.get_rect()  
    
            # position 1 is from the top, -1 is from the bottom  
            if position == 1:  
                self.image = pygame.transform.flip(self.image, False, True)  
                self.rect.bottomleft = [x_coordinate, y_coordinate - int(pipeGap / 2)]  
            if position == -1:  
                self.rect.topleft = [x_coordinate, y_coordinate + int(pipeGap / 2)]  
    
        # defining a function to handle pipes animation and memory  
        def update(self):  
            # setting the scroll speed of the pipes  
            self.rect.x -= scrollSpeed  
    
            # destroying the pipes once they left the screen to release the memory  
            if self.rect.right < 0:  
                self.kill()  
    
    # defining a class to display the button  
    class Button():  
        # defining an initializing function  
        def __init__(self, x_coordinate, y_coordinate, image):  
            # defining some variables  
            self.image = image  
            self.rect = self.image.get_rect()  
            self.rect.topleft = (x_coordinate, y_coordinate)  
        # defining a function to draw the image on the screen  
        def draw(self):  
            # setting the initial action to false  
            action = False  
    
            # getting mouse position  
            position = pygame.mouse.get_pos()  
    
            # checking if mouse is over the button  
            if self.rect.collidepoint(position):  
                if pygame.mouse.get_pressed()[0] == 1:  
                    action = True  
                    
            # drawing button  
            display_screen.blit(self.image, (self.rect.x, self.rect.y))  
    
            # returning the action  
            return action  
    
    # creating the objects of the Group() class of the pygame.sprite module  
    birdGroup = pygame.sprite.Group()  
    pipeGroup = pygame.sprite.Group()  
    
    # creating an object of the FlappyBird() class with  
    bird = FlappyBird(200, int(SCREEN_HEIGHT / 2))  
    
    # using the add() function to add the object of the FlappyBird() class to the group  
    birdGroup.add(bird)  
    
    # creating the restart button instance  
    restartButton = Button(590, 100, button)  
    
    # declaring a variable and initializing its value with True  
    game_run = True  
    
    # using the while loop  
    while game_run:  
        # setting the fps of the game  
        game_clock.tick(game_fps)  
    
        # drawing the background  
        display_screen.blit(background, (0, 0))  
    
        # drawing the bird  
        birdGroup.draw(display_screen)  
    
        # calling the update() function  
        birdGroup.update()  
    
        # drawing the pipes  
        pipeGroup.draw(display_screen)  
    
        # drawing the base  
        display_screen.blit(base, (baseScroll, 576))  
    
        # checking the score  
        if len(pipeGroup) > 0:  
            # checking if the bird is over the pipe and passed the left side of it but not the right size  
            if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.left and birdGroup.sprites()[0].rect.left < pipeGroup.sprites()[0].rect.right and passPipe == False:  
                # setting the boolean value to true  
                passPipe = True  
    
            # checking if the bird has passed the left side of the pipe  
            if passPipe == True:  
                # checking if the bird has passed the right side of the pipe  
                if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.right:  
                    # incrementing the score by 1  
                    playerScore += 1  
                    # setting the boolean value back to false  
                    passPipe = False  
    
        # calling the drawText() function to display the calculated score on the screen  
        drawText(str(playerScore), fontStyle, black, int(725), 15)  
    
        # looking for collision  
        if pygame.sprite.groupcollide(birdGroup, pipeGroup, False, False) or bird.rect.top < 0:  
            gameOver = True  
    
        # checking if bird has hit the ground  
        if bird.rect.bottom >= 576:  
            gameOver = True  
            birdFlying = False  

        # check if player has score of 10 or higher
        if playerScore >= 1:
            victory = True
        
        if victory == True:
            gameOver = True

        # checking if the game is not over  
        if gameOver == False and birdFlying == True:  
            # generating new pipes  
            timeNow = pygame.time.get_ticks()  
            if timeNow - lastPipe > pipeFrequency:  
                pipeHeight = random.randint(-100, 100)  
                bottomPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipeHeight, -1)  
                topPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipeHeight, 1)  
                pipeGroup.add(bottomPipe)  
                pipeGroup.add(topPipe)  
                lastPipe = timeNow  
    
            # scrolling the base  
            baseScroll -= scrollSpeed  
            if abs(baseScroll) > 70:  
                baseScroll = 0  
                
            # calling the update() function  
            pipeGroup.update()  
    
        # checking if the game over and reset  
        if gameOver == True:  
            if victory:
                trophy3 = True
                winning_screen = pygame.image.load("game3_images/winning_screen.png")
                display_screen.blit(winning_screen, (590, 100))
            elif restartButton.draw() == True:  
                gameOver = False  
                playerScore = resetGame()  
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                SCREEN = 'main'
                loop()
        
    
        # using the for loop to iterate through the events of the game  
        for event in pygame.event.get():  
            # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
            if event.type == pygame.QUIT:  
                game_run = False  
            # setting the variable value to True if the event's type is equivalent to pygame's MOUSEBUTTONDOWN constant, the bird is not flying and game is not over  
            if event.type == pygame.MOUSEBUTTONDOWN and birdFlying == False and gameOver == False:  
                birdFlying = True  
    
        # using the update() function of the pygame.display module to update the events of the game  
        pygame.display.update()  
    
    # using the quit() function to quit the game  
    pygame.quit()

# cat maze
def game4():
    # music
    mixer.music.load("music/game4.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('CatMaze', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # background
    bg = pygame.image.load("game4_images/game4_background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0))
    window.blit(text, textRect)

     
    class Player:
        x = 44
        y = 44
        speed = 1
    
        def moveRight(self):
            self.x = self.x + self.speed
    
        def moveLeft(self):
            self.x = self.x - self.speed
    
        def moveUp(self):
            self.y = self.y - self.speed
    
        def moveDown(self):
            self.y = self.y + self.speed

    class Maze:
        def __init__(self):
            self.M = 10
            self.N = 8
            self.maze = [1,1,1,1,1,1,1,1,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,1,1,1,1,1,1,0,1,
                    1,0,1,0,0,0,0,0,0,1,
                    1,0,1,0,1,1,1,1,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,1,1,1,1,1,1,1,1,]

        def draw(self,display_surf,image_surf):
            bx = 0
            by = 0
            for i in range(0,self.M*self.N):
                if self.maze[ bx + (by*self.M) ] == 1:
                    display_surf.blit(image_surf,( bx * 10 , by * 10))
        
                bx = bx + 1
                if bx > self.M-1:
                    bx = 0
                    by = by + 1

    class App:    
        # windowWidth = 800
        # windowHeight = 600
        player = 0
    
        def __init__(self):
            self.running = True
            self.display_surf = None
            self.image_surf = None
            self.block_surf = None
            self.player = Player()
            self.maze = Maze()
            self.windowWidth = WIDTH
            self.windowHeight = HEIGHT
    
        def on_init(self):
            pygame.init()
            self.display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
            
            pygame.display.set_caption('Moggie Maze')
            self.running = True
            self.image_surf = pygame.image.load("FISHY.png").convert()
            self.block_surf = pygame.image.load("game4_images/block.png").convert()
            self.image_surf = pygame.transform.scale(self.image_surf,(50, 50))
            self.block_surf = pygame.transform.scale(self.block_surf,(50, 50))
    
        def on_event(self, event):
            if event.type == pygame.QUIT:
                self.running = False
    
        def on_loop(self):
            pass
        
        def on_render(self):
            self.display_surf.fill((0,0,0))
            self.display_surf.blit(self.image_surf,(self.player.x,self.player.y))
            self.maze.draw(self.display_surf, self.block_surf)
            pygame.display.flip()
    
        def on_cleanup(self):
            pygame.quit()
    
        def on_execute(self):
            if self.on_init() == False:
                self.running = False
    
            while(self.running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.player.moveLeft()
                        elif event.key == pygame.K_RIGHT:
                            self.player.moveRight()
                        elif event.key == pygame.K_UP:
                            self.player.moveUp()
                        elif event.key == pygame.K_DOWN:
                            self.player.moveDown()
                        elif event.key == pygame.K_ESCAPE:
                            self.running = False
        
                self.on_loop()
                self.on_render()
            self.on_cleanup()
    
    if __name__ == "__main__" :
        theApp = App()
        theApp.on_execute()

def collected_all_trophies():
    pass        

# function for MAIN SCREEN
def main_screen():
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
    bush = pygame.transform.scale(bush, (250, 250))

    # trees
    tree = pygame.image.load('tree.png')
    tree = pygame.transform.scale(tree, (250, 250))

    # trophy case
    trophy_case = pygame.image.load('trophy_case.png')
    trophy_case = pygame.transform.scale(trophy_case, (450, 325))

    # display bg, text, bushes, trees
    window.blit(bg, (0,0))
    window.blit(text, textRect) # create text

    # bushes
    window.blit(bush, (75, 225))
    window.blit(bush, (900, 75))
    window.blit(bush, (385, 525))

    # trees
    window.blit(tree, (275, 75))
    window.blit(tree, (1125, 400))
    window.blit(tree, (850, 520))

    # trophy case
    window.blit(trophy_case, (870, 575))

    # spawn cat
    window.blit(cat, (x, y))

def loop():
    global SCREEN, x, y, cat, currentImage, PLAYERIMAGES
    SCREEN = "main"
    # create cat
    cat = pygame.image.load('cat.png')
    cat = pygame.transform.scale(cat, (400, 300))
    x, y = 530, 110 
    
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
            game3()

        if SCREEN == "game4":
            screen_game4.game4()
        
        # quit?
        for event in pygame.event.get():
            if event.type == quit:
                loop = False

        # trophy won?
        if trophy1 and SCREEN == 'main':
            trophy = pygame.image.load('game1_spring.png')
            trophy = pygame.transform.scale(trophy, (65, 65))
            window.blit(trophy, (970, 697))
        if trophy2 and SCREEN == 'main':
            trophy = pygame.image.load('game2_summer.png')
            trophy = pygame.transform.scale(trophy, (65, 65))
            window.blit(trophy, (1034, 697))
        if trophy3 and SCREEN == 'main':
            trophy = pygame.image.load('game3_fall.png')
            trophy = pygame.transform.scale(trophy, (65, 65))
            window.blit(trophy, (1093, 697))
        if trophy4 and SCREEN == 'main':
            trophy = pygame.image.load('game4_winter.png')
            trophy = pygame.transform.scale(trophy, (65, 65))
            window.blit(trophy, (1153, 697))
            
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
        if keys[pygame.K_p]:
                # Change the player image to the next one.
                currentImage += 1
                if currentImage >= len(PLAYERIMAGES):
                    # After the last player image, use the first one.
                    currentImage = 0

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
        if trophy1 and trophy2 and trophy3 and trophy4:
            collected_all_trophies()

        # update display every frame
        pygame.display.flip()

    def terminate():
        pygame.quit()

    terminate()

loop()