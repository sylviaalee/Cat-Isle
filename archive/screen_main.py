import pygame

pygame.init()

# GLOBAL VARIABLES
WIDTH = 1470
HEIGHT = 850
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
SCREEN = "main"

# function for MAIN SCREEN
def main():
    # music
    # pygame.mixer.music.load('theme.wav')

    # add text
    pygame.display.set_caption('Cat Isle')
    text = BASICFONT.render('Cat Isle', True, 'brown')
    textRect = text.get_rect()
    textRect.center = (1470 // 2, 850 // 2)

    # create bg
    bg = pygame.image.load("background2.jpeg")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    # bush
    bush = pygame.image.load('bush.png')
    bush = pygame.transform.scale(bush, (300, 250))

    # display bg + text
    window.blit(bg, (0,0))
    window.blit(text, textRect) # create text
    window.blit(bush, (200, 200))
    
    # spawn cat
    window.blit(cat, (x, y))

    loop = True
    while loop:

        # key pressed?
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > -130:
            x -= 20
        if keys[pygame.K_RIGHT] and x < 1220:
            x += 20
        if keys[pygame.K_UP] and y > -110:
            y -= 20
        if keys[pygame.K_DOWN] and y < 615:
            y += 20

        # update display every frame
        pygame.display.flip()

    # create cat
    cat = pygame.image.load('cat_sample.png')
    cat = pygame.transform.scale(cat, (400, 300))
    x, y = 200, 200