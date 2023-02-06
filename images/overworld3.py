import pygame

pygame.init()
pygame.display.set_caption('Cat Isle')
x, y = 100, 100
cat = pygame.image.load('cat_sample.png')
window.blit(cat, (x, y))