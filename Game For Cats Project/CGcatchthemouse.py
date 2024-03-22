import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOUSE_SIZE = 40
MOUSE_SPEED = 3
MOUSE_COLOR = (0, 255, 0)
BG_COLOR = (255, 255, 255)

# Function to create a new random position for the mouse
def get_random_position():
    x = random.randint(0, SCREEN_WIDTH - MOUSE_SIZE)
    y = random.randint(0, SCREEN_HEIGHT - MOUSE_SIZE)
    return x, y

# Function to check if the mouse is clicked
def is_mouse_clicked(mouse_pos, click_pos):
    mouse_x, mouse_y = mouse_pos
    click_x, click_y = click_pos
    return (mouse_x <= click_x <= mouse_x + MOUSE_SIZE) and (mouse_y <= click_y <= mouse_y + MOUSE_SIZE)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Mouse")

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
mouse_position = get_random_position()
mouse_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
while running:
    screen.fill(BG_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_mouse_clicked(mouse_position, pygame.mouse.get_pos()):
                mouse_position = get_random_position()
                mouse_direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Move the mouse
    mouse_position = (mouse_position[0] + MOUSE_SPEED * mouse_direction[0], mouse_position[1] + MOUSE_SPEED * mouse_direction[1])

    # Check if the mouse hits the screen boundaries
    if mouse_position[0] <= 0 or mouse_position[0] >= SCREEN_WIDTH - MOUSE_SIZE:
        mouse_direction[0] *= -1
    if mouse_position[1] <= 0 or mouse_position[1] >= SCREEN_HEIGHT - MOUSE_SIZE:
        mouse_direction[1] *= -1

    # Draw the mouse
    pygame.draw.rect(screen, MOUSE_COLOR, (mouse_position[0], mouse_position[1], MOUSE_SIZE, MOUSE_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
