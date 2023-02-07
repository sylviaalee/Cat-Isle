import pygame

pygame.init()
pygame.font.get_fonts()

# GLOBAL
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 25)
window = pygame.display.set_mode((WIDTH, HEIGHT))

# add caption
pygame.display.set_caption('Cat Isle')

# cat
cat = pygame.image.load('cat_sample.png')
cat = pygame.transform.scale(cat, (400, 300))
x, y = 100, 100

def main_screen():
    # add text
    text = BASICFONT.render('Cat Isle', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 100)

    # window
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    window.blit(bg, (0,0)) # create bg
    window.blit(text, textRect) # create text

    # make portals
    pygame.draw.circle(window, 'aquamarine4', (100, 100), 50)
    pygame.draw.circle(window, 'aquamarine4', (1370, 100), 50)
    pygame.draw.circle(window, 'aquamarine4', (1370, 750), 50)
    pygame.draw.circle(window, 'aquamarine4', (100, 750), 50)

loop = True
while loop:
    window.blit(cat, (x, y)) # spawn cat

    for event in pygame.event.get():
        if event.type == quit:
            loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -130:
        x -= 8
    if keys[pygame.K_RIGHT] and x < 1200:
        x += 8
    if keys[pygame.K_UP] and y > -110:
        y -= 8
    if keys[pygame.K_DOWN] and y < 600:
        y += 8
    if keys[pygame.K_KP_ENTER]:
        pass
    pygame.display.flip()

pygame.quit()