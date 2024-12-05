import pygame
import sys
import random

pygame.init()

# create game window
window_width = 600
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")

# define snake_body list
snake_body = []

# create game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update game status

    # detect collisions between snake and food
    if snake.colliderect(food):
        # update snake length and score
        snake_size += 1
        score += 1

        # place food at new random position
        food.x = random.randint(0, window_width - food_size)
        food.y = random.randint(0, window_height - food_size)

    # update snake length
    snake_body.append(pygame.Rect(snake.x, snake.y, snake_size, snake_size))
    if len(snake_body) > snake_size:
        del snake_body[0]

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

# snake movement
snake_dx = 0
snake_dy = 0

# snake control
snake_speed_multiplier = 1

# update snake position
snake.x += snake_dx * snake_speed * snake_speed_multiplier
snake.y += snake_dy * snake_speed * snake_speed_multiplier

# check if snake hits window boundaries
if snake.x < 0 or snake.x + snake_size > window_width or snake.y < 0 or snake.y + snake_size > window_height:
    # game over logic
    running = False

# define food properties
food_color = (255, 0, 0) # red
food_size = 20

# place food at random position
food_x = random.randint(0, window_width - food_size)
food_y = random.randint(0, window_height - food_size)

# draw food
food = pygame.Rect(food_x, food_y, food_size, food_size)

# quit game and clean up resources
pygame.quit()
sys.exit()