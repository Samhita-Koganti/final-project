import pygame
import sys
import random

pygame.init()

# create game window
window_width = 600
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")

# CREATE GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # UPDATE GAME STATUS

    # define snake_body list
    snake_body = []

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

    # increase snake speed based on score
    if score > 0 and score % 5 == 0:
        snake_speed_multiplier += 0.1

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
    
    # detect collisions between snake head and body
    if len(snake_body) > 1 and snake.colliderect(snake_body[i] for i in range(1, len(snake_body))):
        running = False

    # display score
    score_font = pygame.font.Font(None, 24)
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255)) # white
    game_window.blit(score_text, (10, 10)) # text position

    # tracking and displaying high score
    high_score = 0

    # load high score from file
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        pass

    # display high score
    high_score_text = score_font.render("High Score: " + str(high_score), True, (255, 255, 255)) # white
    game_window.blit(high_score_text, (10, 40)) # text position

    # RENDER GRAPHICS

    # display game over message and final score
    game_over_font = pygame.font.Font(None, 48) # font type, font size
    game_over_text = game_over_font.render("Game Over", True, (255, 255, 255)) # white

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render("Final Score: " + str(score), True, (255, 255, 255)) # white

    game_window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - 48))
    game_window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2))

    # implement restart option
    restart_font = pygame.font.Font(None, 24)
    restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255)) # white

    game_window.blit(restart_text, (window_width // 2 - restart_text.get_width() // 2, window_height // 2 + 48))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # restart game
                running = True
                snake_body.clear()
                snake.x - window_width // 2
                snake.y - window_height // 2
                score = 0
        break

    pygame.display.update()

# QUIT GAME AND CLEAN UP RESOURCES
pygame.quit()
sys.exit()