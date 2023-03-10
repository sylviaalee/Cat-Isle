# cat sweeper
# from overworld3 import *
import pygame, sys
import random
from pygame import mixer
mixer.init()
from pygame.locals import *

def game2():
    pygame.init()

    # GLOBAL
    WIDTH = 10
    HEIGHT = 10
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    trophy2 = False

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
