# Pygame Library
import pygame 
from pygame.locals import *

# Clock
clock = pygame.time.Clock()

# Classes
from bgscroll import *
from cars import *

# Main Class
class Main:
    # Properties
    car1 = Car("../assets/black_car.png")
    car2 = Car("../assets/blue_car.png")
    screen = None
    bg = None

    # Constructor
    def __init__(self, scr_width, scr_height):
        pygame.init()
        self.screen = pygame.display.set_mode([scr_width, scr_height])
        self.bg = BackgroundScroll((scr_width, scr_height))
        self.start()

    # Start
    def start(self):
        # Main Loop
        getTicksLastFrame = 0
        running = True
        while running:
            # Delta Time
            t = pygame.time.get_ticks()
            deltaTime = (t - getTicksLastFrame) / 100
            getTicksLastFrame = t

            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit
                    running = False
                if event.type == KEYDOWN: # Key Pressed
                    if event.key == K_ESCAPE: # Escape, quit game
                        running = False
                    if event.key == K_LSHIFT: # Shift Car 1
                        self.car1.shift_up()
                    if event.key == K_UP: # Shift Car 2
                        self.car2.shift_up()

            # Fill Screen to reset it
            self.screen.fill((0,0,0))

            # Draw Road
            bg.update(10, deltaTime)
            self.screen.blit(self.bg.surface(), (0,0))

            # Draw Cars
            self.screen.blit(self.car1.sprite, (50,50))
            self.screen.blit(self.car2.sprite, (10,10))

            # Flip Display
            pygame.display.flip()

        # Quit
        pygame.quit()


