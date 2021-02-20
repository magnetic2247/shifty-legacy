# Pygame library
import pygame 

# Car Class
class Car(pygame.sprite.Sprite):
    # Class Properties
    surface = None
    pos = (0,0)
    speed = 0

    # Constructor
    def __init__(self, asset_location):
        super(Car, self).__init__()
        self.surface = pygame.transform.scale(pygame.image.load(asset_location), (int(32*1.5), int(62*1.5)))

# Dynamic Scrolling Background
class BackgroundScroll(pygame.sprite.Sprite):
    # Class properties
    background1 = None
    background2 = None
    background1_pos = None
    background2_pos = None
    virtual_screen = None

    # Constructor
    def __init__(self, asset_location, background_pos):
        # Initialize Virtual Screen
        self.virtual_screen = pygame.Surface(background_pos)

        # Call Sprite Constructor
        super(BackgroundScroll, self).__init__()

        # Load Surfaces for Background
        self.background1 = pygame.image.load(asset_location)
        self.background2 = pygame.image.load(asset_location)

        # Initialize Positions
        self.background1_pos = (0,0)
        self.background2_pos = (0, -self.virtual_screen.get_height())


    # Update Virtual Screen
    def update(self, speed, delta):
        # Update Position
        self.background1_pos = (0, self.background1_pos[1] + speed*delta)
        self.background2_pos = (0, self.background2_pos[1] + speed*delta)
        if self.background1_pos[1] > self.virtual_screen.get_height():
            self.background1_pos = (0, -self.virtual_screen.get_height())
        elif self.background2_pos[1] > self.virtual_screen.get_height():
            self.background2_pos = (0, -self.virtual_screen.get_height())

        # Redraw Virtual Screen
        self.virtual_screen.fill((0,0,0))
        self.virtual_screen.blit(self.background1, self.background1_pos)
        self.virtual_screen.blit(self.background2, self.background2_pos)

