# Pygame Library
import pygame

# Sprites Classes
from sprites import *

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

# Assets
# Background Scroll
bg = BackgroundScroll("../assets/bg.png", (SCREEN_WIDTH, SCREEN_HEIGHT))

# Car :D
car1 = Car("../assets/black_car.png")
car2 = Car("../assets/blue_car.png")

# Run until user quits
getTicksLastFrame = 0
running = True
while running:
    # Delta Time
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 100
    getTicksLastFrame = t

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill Screen to reset it
    screen.fill((0,0,0))

    # Road
    bg.update(10, deltaTime)
    screen.blit(bg.virtual_screen, (0,0))
    
    # Draw Cars
    screen.blit(car1.surface, (340, 400))
    screen.blit(car2.surface, (410, 400))

    # Update Display
    pygame.display.flip()

# Quit!
pygame.quit()
    