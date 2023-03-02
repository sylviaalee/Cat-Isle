# cat maze
# from overworld3 import *
import pygame

pygame.init()
from pygame import mixer
mixer.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('gooddog.ttf', 50)
window = pygame.display.set_mode((WIDTH, HEIGHT))
trophy4 = False

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

game4()