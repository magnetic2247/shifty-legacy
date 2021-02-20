# Pygame Library
import pygame

# Keys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until user quits
running = True
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill Screen to reset it
    screen.fill((0,0,0))

    # CAR :D
    car = pygame.image.load("../assets/blue_car.png")
    screen.blit(car, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    # Update Display
    pygame.display.flip()

# Quit!
pygame.quit()
    