import random
import pygame
 
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1470
HEIGHT = 850
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
 
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
 
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


# background
bg = pygame.image.load("background.png")
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

# load images used
IMAGESDICT = {'background' : pygame.image.load("background.png"), 
            'bush' : pygame.image.load("bush.png"), 
            'cat' : pygame.image.load("cat_sample.png")}


 
RED = (255, 0, 0)
 
 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
 
 
all_sprites_list = pygame.sprite.Group()
 
playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

# text
text = BASICFONT.render('Cat Isle', True, 'brown')
textRect = text.get_rect()
textRect.center = (1470 // 2, 850 // 2)

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
    window.blit(cat, (0, 0)) # create sprite
    window.blit(text, textRect) # create text

    # sprites
    all_sprites_list.add(object_)
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
        cat.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        cat.moveRight(10)
    if keys[pygame.K_DOWN]:
        cat.moveForward(10)
    if keys[pygame.K_UP]:
        cat.moveBack(10)
 
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()