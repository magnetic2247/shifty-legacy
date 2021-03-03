import time

# Pygame Library
import pygame 
from pygame.locals import *

# Clock
clock = pygame.time.Clock()
clock.tick(30)

# Classes
from bgscroll import *
from cars import *
from dash import *

# Main Class
class Main:
    # Car1 Properties
    car1 = Car("../assets/black_car.png")
    dash1 = Dash()
    car1_pos = (340,400)

    # Car2 Properties
    car2 = Car("../assets/blue_car.png")
    dash2 = Dash()
    car2_pos = (410,400)

    # Main Class Properties
    screen = None
    bg = None
    race_distance = 1
    race = True

    # Constructor
    def __init__(self):
        """
        Entrée: None
        Sortie: None
        """
        pygame.init()
        print(id(self.dash1) == id(self.dash2))
        self.screen = pygame.display.set_mode([800,600])
        self.bg = BackgroundScroll((800,600))
        self.start()

    # Start
    def start(self):
        """
        Entrée: None
        Sortie: None
        """
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
                    if event.key == K_RSHIFT: # Shift Car 2
                        self.car2.shift_up()

            # Race distance
            self.race_distance += int(100*deltaTime)
            if self.race_distance >= 26480:
                self.race = False

            # Race going
            if self.race:
                # Increment RPM
                if self.car1.rpm < 6500:
                    self.car1.rpm += 5
                if self.car2.rpm < 6500:
                    self.car2.rpm += 5

                # Calculate Car Positions
                if self.car1.good_shifts > self.car2.good_shifts: # Driver1 has shifted better! Driver2 is Trash!
                    self.car1_pos = (340,390)
                    self.car2_pos = (410,400)
                elif self.car2.good_shifts > self.car1.good_shifts: # Driver2 has shifted better! Driver1 is Trash!
                    self.car1_pos = (340,400)
                    self.car2_pos = (410,390)
                else: # Both Drivers are Trash
                    self.car1_pos = (340,400)
                    self.car2_pos = (410,400)

                # Fill Screen to reset it
                self.screen.fill((0,0,0))

                # Draw Road
                self.bg.update(10, deltaTime)
                self.screen.blit(self.bg.surface(), (0,0))

                # Draw Cars
                self.screen.blit(self.car1.sprite, self.car1_pos)
                self.screen.blit(self.car2.sprite, self.car2_pos)

                # Draw Dashes
                self.dash1.update(self.car1.rpm, self.car1.gear, "Shifts " + str(self.car1.good_shifts))
                self.screen.blit(self.dash1.surface, (0,10))
                self.dash2.update(self.car2.rpm, self.car2.gear, "Shifts " + str(self.car2.good_shifts))
                self.screen.blit(self.dash2.surface, (725,10))

            else: # Race Finished
                # Find out who won
                if self.car1.good_shifts > self.car2.good_shifts: # Driver1 has shifted better! Driver2 is Trash!
                    final_screen = pygame.image.load("../assets/p1.png")
                elif self.car2.good_shifts > self.car1.good_shifts: # Driver2 has shifted better! Driver1 is Trash!
                    final_screen = pygame.image.load("../assets/p2.png")
                else: # Both Drivers are Trash
                    final_screen = pygame.image.load("../assets/tie.png")

                # Fill Screen to reset it
                self.screen.fill((0,0,0))

                # Show Winner
                self.screen.blit(final_screen, (0,0))

            # Flip Display
            pygame.display.flip()

        # Quit
        pygame.quit()


