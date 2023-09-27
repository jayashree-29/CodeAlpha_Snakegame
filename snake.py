import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position
snake_x = screen_width // 2
snake_y = screen_height // 2

# Snake initial speed
snake_speed = 15

# Initialize snake direction
direction = "RIGHT"

# Snake initial body
snake_body = []
body_length = 1

# Food initial position
food_x = random.randrange(1, (screen_width // 10)) * 10
food_y = random.randrange(1, (screen_height // 10)) * 10

# Score
score = 0

# Function to display text on the screen
font_style = pygame.font.Font(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 2, screen_height / 2])

# Game over function
def game_over():
    message("Game Over! Your Score: " + str(score), red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
game_over_flag = False
while not game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            elif event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

    # Move the snake
    if direction == "LEFT":
        snake_x -= 10
    elif direction == "RIGHT":
        snake_x += 10
    elif direction == "UP":
        snake_y -= 10
    elif direction == "DOWN":
        snake_y += 10

    # Collision with wall
    if (
        snake_x >= screen_width
        or snake_x < 0
        or snake_y >= screen_height
        or snake_y < 0
    ):
        game_over()

    # Snake body
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > body_length:
        del snake_body[0]

    # Collision with itself
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over()

    # Generate new food and increase score
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(1, (screen_width // 10)) * 10
        food_y = random.randrange(1, (screen_height // 10)) * 10
        body_length += 1
        score += 1

    # Update the screen
    screen.fill(white)
    for segment in snake_body:
        pygame.draw.rect(screen, green, [segment[0], segment[1], 10, 10])
    pygame.draw.rect(screen, red, [food_x, food_y, 10, 10])

    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(snake_speed)

# Quit the game
pygame.quit()
quit()
