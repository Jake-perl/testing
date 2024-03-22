import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DOT_SIZE = 20
DOT_SPEED = 5
DOT_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)

# Function to create a new random position for the dot
def get_random_position():
    x = random.randint(0, SCREEN_WIDTH - DOT_SIZE)
    y = random.randint(0, SCREEN_HEIGHT - DOT_SIZE)
    return x, y

# Function to check if the dot is clicked
def is_dot_clicked(dot_pos, click_pos):
    dot_x, dot_y = dot_pos
    click_x, click_y = click_pos
    return (dot_x <= click_x <= dot_x + DOT_SIZE) and (dot_y <= click_y <= dot_y + DOT_SIZE)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chase the Dot")

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
dot_position = get_random_position()
while running:
    screen.fill(BG_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_dot_clicked(dot_position, pygame.mouse.get_pos()):
                dot_position = get_random_position()

    # Draw the dot
    pygame.draw.rect(screen, DOT_COLOR, (dot_position[0], dot_position[1], DOT_SIZE, DOT_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
