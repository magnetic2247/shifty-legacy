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

# Assets
# Road
mark = pygame.Surface((15,50))
mark_pos = (10, 10)
mark.fill((255, 255, 255))

# Car :D
car = pygame.transform.scale2x(pygame.image.load("../assets/blue_car.png"))

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
    mark_pos = (10, mark_pos[1]+20*deltaTime)
    screen.blit(mark, mark_pos)
    
    # Car
    screen.blit(car, (SCREEN_WIDTH/2 - car.get_width()/2, SCREEN_HEIGHT/2 - car.get_height()/2))

    # Update Display
    pygame.display.flip()

# Quit!
pygame.quit()
    