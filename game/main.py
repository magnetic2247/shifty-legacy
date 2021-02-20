# Pygame Library
import pygame
pygame.init()

# FPS Cap
clock = pygame.time.Clock()

# Sprites Classes
from sprites import *

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Assets
# Background Scroll
bg = BackgroundScroll("../assets/bg.png", (SCREEN_WIDTH, SCREEN_HEIGHT))

# Car :D
car1 = Car("../assets/black_car.png", (340, 350))
car2 = Car("../assets/blue_car.png", (410, 350))
car2.update_position_index(4)

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

    # Draw Road
    bg.update(10, deltaTime)
    screen.blit(bg.virtual_screen, (0,0))
    
    # Draw Cars
    car1.update(deltaTime)
    car2.update(deltaTime)
    screen.blit(car1.surface, car1.actual_pos)
    screen.blit(car2.surface, car2.actual_pos)

    # Draw Dashes
    screen.blit(car1.dash.surface, (10, 10))

    # Update Display
    pygame.display.flip()

# Quit!
pygame.quit()
    