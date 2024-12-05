import pygame
import sys

pygame.init()

# create game window
window_width = 600
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")