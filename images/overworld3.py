import pygame

pygame.init()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

# add text
pygame.display.set_caption('Cat Isle')
text = BASICFONT.render('Cat Isle', True, 'brown')
textRect = text.get_rect()
textRect.center = (1470 // 2, 100)

# window
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

# cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 100, 100

loop = True
while loop:
    window.blit(bg, (0,0)) # create bg
    window.blit(cat, (x, y)) # spawn cat
    window.blit(text, textRect) # create text

    # make portals
    pygame.draw.circle(window, 'red', (50, 50), 50)

    for event in pygame.event.get():
        if event.type == quit:
            loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 8
    if keys[pygame.K_RIGHT]:
        x += 8
    if keys[pygame.K_UP]:
        y -= 8
    if keys[pygame.K_DOWN]:
        y += 8
    pygame.display.flip()

pygame.quit()