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
            while victory == True:
                trophy1 = True
                window.blit(bg, (0,0))
                message("You Won the Spring Trophy! Congratulations! Press Q to go back to the main screen.", "brown")          
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            # go back to main_screen
                            mixer.music.load("music/main_theme.mp3")
                            mixer.music.set_volume(0.2)
                            mixer.music.play()
                            loop()
            # player loses
            while victory == False:
                window.blit(bg, (0,0))
                message("You Lost! Press Q (Quit) to go back to main screen or C to Play Again", "brown")
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            # go back to main_screen
                            loop()
                        if event.key == pygame.K_c:
                            gameLoop()

    gameLoop()

# cat sweeper
def game2():
    # music
    mixer.music.load("music/game2.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    import pygame
    import sys
    import time
    from solver import Cell, Sudoku

    pygame.init()

    # Set size of game and other constants
    cell_size = 50
    minor_grid_size = 1
    major_grid_size = 3
    buffer = 5
    button_height = 50
    button_width = 125
    button_border = 2
    width = cell_size*9 + minor_grid_size*6 + major_grid_size*4 + buffer*2
    height = cell_size*9 + minor_grid_size*6 + \
        major_grid_size*4 + button_height + buffer*3 + button_border*2
    size = width, height
    white = 255, 255, 255
    black = 0, 0, 0
    gray = 200, 200, 200
    green = 0, 175, 0
    red = 200, 0, 0
    inactive_btn = 51, 255, 255
    active_btn = 51, 153, 255

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Sudokat')

    class RectCell(pygame.Rect):
        '''
        A class built upon the pygame Rect class used to represent individual cells in the game.
        This class has a few extra attributes not contained within the base Rect class.
        '''

        def __init__(self, left, top, row, col):
            super().__init__(left, top, cell_size, cell_size)
            self.row = row
            self.col = col


    def create_cells():
        '''Creates all 81 cells with RectCell class.'''
        cells = [[] for _ in range(9)]

        # Set attributes for for first RectCell
        row = 0
        col = 0
        left = buffer + major_grid_size
        top = buffer + major_grid_size

        while row < 9:
            while col < 9:
                cells[row].append(RectCell(left, top, row, col))

                # Update attributes for next RectCell
                left += cell_size + minor_grid_size
                if col != 0 and (col + 1) % 3 == 0:
                    left = left + major_grid_size - minor_grid_size
                col += 1

            # Update attributes for next RectCell
            top += cell_size + minor_grid_size
            if row != 0 and (row + 1) % 3 == 0:
                top = top + major_grid_size - minor_grid_size
            left = buffer + major_grid_size
            col = 0
            row += 1

        return cells


    def draw_grid():
        '''Draws the major and minor grid lines for Sudoku.'''
        # Draw minor grid lines
        lines_drawn = 0
        pos = buffer + major_grid_size + cell_size
        while lines_drawn < 6:
            pygame.draw.line(screen, black, (pos, buffer),
                            (pos, width-buffer-1), minor_grid_size)
            pygame.draw.line(screen, black, (buffer, pos),
                            (width-buffer-1, pos), minor_grid_size)

            # Update number of lines drawn
            lines_drawn += 1

            # Update pos for next lines
            pos += cell_size + minor_grid_size
            if lines_drawn % 2 == 0:
                pos += cell_size + major_grid_size

        # Draw major grid lines
        for pos in range(buffer+major_grid_size//2, width, cell_size*3 + minor_grid_size*2 + major_grid_size):
            pygame.draw.line(screen, black, (pos, buffer),
                            (pos, width-buffer-1), major_grid_size)
            pygame.draw.line(screen, black, (buffer, pos),
                            (width-buffer-1, pos), major_grid_size)


    def fill_cells(cells, board):
        '''Fills in all the numbers for the game.'''
        font = pygame.font.Font(None, 36)

        # Fill in all cells with correct value
        for row in range(9):
            for col in range(9):
                if board.board[row][col].value is None:
                    continue

                # Fill in given values
                if not board.board[row][col].editable:
                    font.bold = True
                    text = font.render(f'{board.board[row][col].value}', 1, black)

                # Fill in values entered by user
                else:
                    font.bold = False
                    if board.check_move(board.board[row][col], board.board[row][col].value):
                        text = font.render(
                            f'{board.board[row][col].value}', 1, green)
                    else:
                        text = font.render(
                            f'{board.board[row][col].value}', 1, red)

                # Center text in cell
                xpos, ypos = cells[row][col].center
                textbox = text.get_rect(center=(xpos, ypos))
                screen.blit(text, textbox)


    def draw_button(left, top, width, height, border, color, border_color, text):
        '''Creates a button with a border.'''
        # Draw the border as outer rect
        pygame.draw.rect(
            screen,
            border_color,
            (left, top, width+border*2, height+border*2),
        )

        # Draw the inner button
        button = pygame.Rect(
            left+border,
            top+border,
            width,
            height
        )
        pygame.draw.rect(screen, color, button)

        # Set the text
        font = pygame.font.Font(None, 26)
        text = font.render(text, 1, black)
        xpos, ypos = button.center
        textbox = text.get_rect(center=(xpos, ypos))
        screen.blit(text, textbox)

        return button


    def draw_board(active_cell, cells, game):
        '''Draws all elements making up the board.'''
        # Draw grid and cells
        draw_grid()
        if active_cell is not None:
            pygame.draw.rect(screen, gray, active_cell)

        # Fill in cell values
        fill_cells(cells, game)


    def visual_solve(game, cells):
        '''Solves the game while giving a visual representation of what is being done.'''
        # Get first empty cell
        cell = game.get_empty_cell()

        # Solve is complete if cell is False
        if not cell:
            return True

        # Check each possible move
        for val in range(1, 10):
            # Allow game to quit when being solved
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Place value in board
            cell.value = val

            # Outline cell being changed in red
            screen.fill(white)
            draw_board(None, cells, game)
            cell_rect = cells[cell.row][cell.col]
            pygame.draw.rect(screen, red, cell_rect, 5)
            pygame.display.update([cell_rect])
            time.sleep(0.05)

            # Check if the value is a valid move
            if not game.check_move(cell, val):
                cell.value = None
                continue

            # If all recursive calls return True then board is solved
            screen.fill(white)
            pygame.draw.rect(screen, green, cell_rect, 5)
            draw_board(None, cells, game)
            pygame.display.update([cell_rect])
            if visual_solve(game, cells):
                return True

            # Undo move is solve was unsuccessful
            cell.value = None

        # No moves were successful
        screen.fill(white)
        pygame.draw.rect(screen, white, cell_rect, 5)
        draw_board(None, cells, game)
        pygame.display.update([cell_rect])
        return False


    def check_sudoku(sudoku):
        '''
        Takes a complete instance of Soduku and 
        returns whether or not the solution is valid.
        '''
        # Ensure all cells are filled
        if sudoku.get_empty_cell():
            raise ValueError('Game is not complete')

        # Will hold values for each row, column, and box
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        # Check all rows, columns, and boxes contain no duplicates
        for row in range(9):
            for col in range(9):
                box = (row // 3) * 3 + col // 3
                value = sudoku.board[row][col].value

                # Check if number already encountered in row, column, or box
                if value in row_sets[row] or value in col_sets[col] or value in box_sets[box]:
                    return False

                # Add value to corresponding set
                row_sets[row].add(value)
                col_sets[col].add(value)
                box_sets[box].add(value)

        # All rows, columns, and boxes are valid
        return True


    def play():
        '''Contains all the functionality for playing a game of Sudoku.'''
        easy = [
            [0, 0, 0, 9, 0, 0, 0, 3, 0],
            [3, 0, 6, 0, 2, 0, 0, 4, 0],
            [2, 0, 4, 0, 0, 3, 1, 0, 6],
            [0, 7, 0, 0, 5, 1, 0, 8, 0],
            [0, 3, 1, 0, 6, 0, 0, 5, 7],
            [5, 0, 9, 0, 0, 0, 6, 0, 0],
            [4, 1, 0, 0, 0, 2, 0, 7, 8],
            [7, 6, 3, 0, 0, 5, 4, 0, 0],
            [9, 2, 8, 0, 0, 4, 0, 0, 1]
        ]
        game = Sudoku(easy)
        cells = create_cells()
        active_cell = None
        solve_rect = pygame.Rect(
            buffer,
            height-button_height - button_border*2 - buffer,
            button_width + button_border*2,
            button_height + button_border*2
        )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Handle mouse click
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()

                    # Reset button is pressed
                    if reset_btn.collidepoint(mouse_pos):
                        game.reset()

                    # Solve button is pressed
                    if solve_btn.collidepoint(mouse_pos):
                        screen.fill(white)
                        active_cell = None
                        draw_board(active_cell, cells, game)
                        reset_btn = draw_button(
                            width - buffer - button_border*2 - button_width,
                            height - button_height - button_border*2 - buffer,
                            button_width,
                            button_height,
                            button_border,
                            inactive_btn,
                            black,
                            'Reset'
                        )
                        solve_btn = draw_button(
                            width - buffer*2 - button_border*4 - button_width*2,
                            height - button_height - button_border*2 - buffer,
                            button_width,
                            button_height,
                            button_border,
                            inactive_btn,
                            black,
                            'Stuck?'
                        )
                        pygame.display.flip()
                        visual_solve(game, cells)

                    # Test if point in any cell
                    active_cell = None
                    for row in cells:
                        for cell in row:
                            if cell.collidepoint(mouse_pos):
                                active_cell = cell

                    # Test if active cell is empty
                    if active_cell and not game.board[active_cell.row][active_cell.col].editable:
                        active_cell = None

                # Handle key press
                if event.type == pygame.KEYUP:
                    if active_cell is not None:

                        # Input number based on key press
                        if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                            game.board[active_cell.row][active_cell.col].value = 0
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            game.board[active_cell.row][active_cell.col].value = 1
                        if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            game.board[active_cell.row][active_cell.col].value = 2
                        if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            game.board[active_cell.row][active_cell.col].value = 3
                        if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            game.board[active_cell.row][active_cell.col].value = 4
                        if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            game.board[active_cell.row][active_cell.col].value = 5
                        if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            game.board[active_cell.row][active_cell.col].value = 6
                        if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                            game.board[active_cell.row][active_cell.col].value = 7
                        if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            game.board[active_cell.row][active_cell.col].value = 8
                        if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                            game.board[active_cell.row][active_cell.col].value = 9
                        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            game.board[active_cell.row][active_cell.col].value = None

            screen.fill(white)

            # Draw board
            draw_board(active_cell, cells, game)

            # Create buttons
            reset_btn = draw_button(
                width - buffer - button_border*2 - button_width,
                height - button_height - button_border*2 - buffer,
                button_width,
                button_height,
                button_border,
                inactive_btn,
                black,
                'Reset'
            )
            solve_btn = draw_button(
                width - buffer*2 - button_border*4 - button_width*2,
                height - button_height - button_border*2 - buffer,
                button_width,
                button_height,
                button_border,
                inactive_btn,
                black,
                'Stuck?'
            )

            # Check if mouse over either button
            if reset_btn.collidepoint(pygame.mouse.get_pos()):
                reset_btn = draw_button(
                    width - buffer - button_border*2 - button_width,
                    height - button_height - button_border*2 - buffer,
                    button_width,
                    button_height,
                    button_border,
                    active_btn,
                    black,
                    'Reset'
                )
            if solve_btn.collidepoint(pygame.mouse.get_pos()):
                solve_btn = draw_button(
                    width - buffer*2 - button_border*4 - button_width*2,
                    height - button_height - button_border*2 - buffer,
                    button_width,
                    button_height,
                    button_border,
                    active_btn,
                    black,
                    'Stuck?'
                )

            # Check if game is complete
            if not game.get_empty_cell():
                if check_sudoku(game):
                    # Set the text
                    font = pygame.font.Font(None, 36)
                    text = font.render('Solved! You have won the Summer Trophy! Press Q to go to Main Screen.', 1, green)
                    textbox = text.get_rect(center=(solve_rect.center))
                    screen.blit(text, textbox)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_q]:
                        SCREEN = 'main'
                        mixer.music.load("music/main_theme.mp3")
                        mixer.music.set_volume(0.2)
                        mixer.music.play()
                        loop()
            # Update screen
            pygame.display.flip()
    play()

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
                mixer.music.load("music/main_theme.mp3")
                mixer.music.set_volume(0.2)
                mixer.music.play()
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

# cat hang
def game4():
    # music
    mixer.music.load("music/game4.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()

    # text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('HangCat', True, 'brown')
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
            
            pygame.display.set_caption('CatMaze')
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
    window = pygame.display.set_mode((WIDTH, HEIGHT))
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
            game2()

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