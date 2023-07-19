import pygame
import random

pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Snake properties
snake_block = 10
snake_speed = 60

# Colors
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Load background image
background_image = pygame.image.load("background.jpg")  # Add the path to your background image


# Snake function

def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(window, yellow, [block[0], block[1], snake_block, snake_block])


# Function to display the score on the screen

def display_score(score):
    font = pygame.font.SysFont(None, 30)
    score_text = font.render("Score: " + str(score), True, yellow)
    game_window.blit(score_text, (10, 580))


# Main game loop

def game_loop():
    game_over = False
    game_close = False

    # Snake initial position and movement
    snake_x, snake_y = window_width // 2, window_height // 2
    snake_x_change, snake_y_change = 0, 0
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(
        random.randrange(0, window_height - snake_block) / 10.0
    ) * 10.0

    # Score
    score = 0

    while not game_over:

        while game_close:
            # Game over screen
            window.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message1 = font_style.render("Game over!", True, yellow)  # First row of the message
            message2 = font_style.render("Press Q-Quit or R-Play Again", True, yellow)  # Second row of the message

            # Calculate the positions to center the messages on the screen
            message1_x = window_width // 2 - message1.get_width() // 2
            message2_x = window_width // 2 - message2.get_width() // 2
            message_y = window_height // 3

            window.blit(message1, (message1_x, message_y))  # Display the first row of the message
            window.blit(message2,
                        (message2_x, message_y + message1.get_height() + 10))  # Display the second row of the message

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Move the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        # Check for boundaries and collision with the food
        if (
                snake_x >= window_width
                or snake_x < 0
                or snake_y >= window_height
                or snake_y < 0
        ):
            game_close = True
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Draw the background
        game_window.blit(background_image, (0, 0))

        # Draw the food
        pygame.draw.rect(window, yellow, [food_x, food_y, snake_block, snake_block])

        # Draw the snake
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        # Display the score
        display_score(score)

        pygame.display.update()

        # Check if the snake eats the food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(
                random.randrange(0, window_width - snake_block) / 10.0
            ) * 10.0, round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 10

        # Adjust the game speed
        pygame.time.delay(snake_speed)

    pygame.quit()
    quit()


# Run the game loop
game_loop()
