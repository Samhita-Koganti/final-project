import pygame
import sys

# create game window
pygame.init()
screen = pygame.dusplay.set_mode((600, 600))
clock = pygame.time.Clock()

# create game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((175,215,70)) # green
    pygame.display.update()
    clock.tick(60)