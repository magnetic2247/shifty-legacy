# Pygame library
import pygame 

class Car(pygame.sprite.Sprite):
    # Class Properties
    surface = None
    pos = (0,0)
    speed = 0

    # Constructor
    def __init__(self, asset_location):
        super(Car, self).__init__()
        self.surface = pygame.transform.scale2x(pygame.image.load(asset_location))

class BackgroundScroll(pygame.sprite.Sprite):
    # Class properties
    surface = None
    pos = (0,0)

    # Constructor
    def __init__(self, asset_location):
        super(BackgroundScroll, self).__init__()
        self.surface = pygame.image.load(asset_location)

