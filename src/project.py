import pygame
import sys

pygame.init()

# create game window
window_width = 600
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")

# create game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update game status

    # render graphics

    pygame.display.update()

# quit game and clean up resources
pygame.quit()
sys.exit()