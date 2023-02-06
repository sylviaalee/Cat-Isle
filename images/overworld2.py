import random
import pygame
 
# Global Variables
FPS =60
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1470
HEIGHT = 850
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        global player_image, player_rect
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        #PYGAME SURFACE

        player_image = pygame.image.load("cat_sample.png").convert_alpha()
        player_rect = player_image.get_rect(center = (350, 350))
     

        '''
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        '''
        '''
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
        
        '''
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10
 
 

pygame.init()
pygame.display.set_caption('Cat Isle')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

text = BASICFONT.render('Cat Isle', True, 'brown')
textRect = text.get_rect()
textRect.center = (1470 // 2, 850 // 2)

# load images used
IMAGESDICT = {'background' : pygame.image.load("background.png"), 
            'bush' : pygame.image.load("bush.png"), 
            'cat' : pygame.image.load("cat_sample.png")}

# background
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

RED = (255, 0, 0)
 
all_sprites_list = pygame.sprite.Group()
 
cat = Sprite(RED, 20, 30)
cat.rect.x = 200
cat.rect.y = 300
all_sprites_list.add(cat)


exit = True
clock = pygame.time.Clock()

while exit:
    # window
    window.blit(bg,(0,0))
    cat = pygame.image.load('cat_sample.png')
    window.blit(cat, (cat.rect.x, cat.rect.y)) # create sprite
    window.blit(text, textRect) # create text

    # sprites
    # all_sprites_list.add(cat) # causes error
    all_sprites_list.update()
    all_sprites_list.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cat.rect.x -= 2
    if keys[pygame.K_RIGHT]:
        cat.rect.x += 2
    if keys[pygame.K_DOWN]:
        cat.rect.y -= 2
    if keys[pygame.K_UP]:
        cat.rect.y += 2
 
    all_sprites_list.update()
    window.blit(bg, (0,0))
    window.blit(player_image, player_rect)
    all_sprites_list.draw(window)
    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()