import random

# Pygame Library
import pygame
from pygame.locals import *
pygame.init()

# Clock
clock = pygame.time.Clock()

# Sprites Classes
from sprites import *

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Assets
# Background Scroll
bg = BackgroundScroll((SCREEN_WIDTH, SCREEN_HEIGHT))

# Cars :D
car1 = Car("../assets/black_car.png", (340, 350))
car2 = Car("../assets/blue_car.png", (410, 350))

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
        if event.type == KEYDOWN:
            if event.key == K_z:
                car1.shift_up()
            if event.key == K_s:
                car1.shift_down()
            if event.key == K_UP:
                car2.shift_up()
            if event.key == K_DOWN:
                car2.shift_down()

    # Fill Screen to reset it
    screen.fill((0,0,0))

    # Draw Road
    bg.update(10, deltaTime)
    screen.blit(bg.surface(), (0,0))
    
    # Draw Cars
    car1.update(deltaTime)
    car2.update(deltaTime)
    screen.blit(car1.surface, car1.actual_pos)
    screen.blit(car2.surface, car2.actual_pos)

    # Draw Dashes
    screen.blit(car1.dash.surface, (10, 10))
    screen.blit(car2.dash.surface, (640, 10))

    # Debug
    if id(car1.dash) == id(car2.dash):
        exit()

    # Update Display
    pygame.display.flip()

# Quit!
pygame.quit()
    