import pygame

pygame.init()
pygame.display.set_caption('Cat Isle')

# window
window = pygame.display.set_mode((500, 500))
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg,(500, 500))

# cat
x, y = 100, 100
cat = pygame.image.load('cat_sample.png')
window.blit(cat, (x, y))