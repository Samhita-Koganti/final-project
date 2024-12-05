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

# define snake properties
snake_color = (0, 255, 0) # green
snake_size = 20
snake_x = window_width // 2
snake_y = window_height // 2
snake_speed = 5

# draw snake
snake = pygame.Rect(snake_x, snake_y, snake_size, snake_size)

# quit game and clean up resources
pygame.quit()
sys.exit()