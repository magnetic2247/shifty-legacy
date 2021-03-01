# Pygame Library
import pygame

# Car Class
class Car(pygame.sprite.Sprite):
    # Properties
    sprite = None
    good_shifts = 0
    gear = 1
    rpm = 0

    # Constructor
    def __init__(self, asset_location):
        # Call Sprite Constructor
        pygame.sprite.Sprite.__init__(self)

        # Load Sprite
        self.sprite = pygame.transform.scale(
            pygame.image.load(asset_location), 
            (int(32*1.5), int(62*1.5))
        )

    # Self explanatory
    def shift_up(self):
        if 5500 > self.rpm > 6000: # Good Shift
            self.good_shifts += 1
        self.gear += 1
        self.rpm -= 2000
