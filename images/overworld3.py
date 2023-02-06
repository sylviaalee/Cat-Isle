import pygame

pygame.init()
pygame.display.set_caption('Cat Isle')

# window
window = pygame.display.set_mode((500, 500))
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(500, 500))

# cat
cat = pygame.image.load('cat_sample.png')
x, y = 100, 100

loop = True
while loop:
    window.blit(cat, (x, y))
    window.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == quit:
            loop = False

    pygame.display.flip()

pygame.quit()