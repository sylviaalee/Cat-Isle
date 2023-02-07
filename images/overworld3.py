import pygame

# GLOBAL
WIDTH = 1470
HEIGHT = 850

pygame.init()
pygame.display.set_caption('Cat Isle')

# window
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

# cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (300, 350))
x, y = 100, 100

loop = True
while loop:
    window.blit(bg, (0,0))
    window.blit(cat, (x, y))

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