# Pygame library
import pygame

# Maths
import maths

# Dash Display
class Dash(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        # Call Sprite Constructor
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.Surface((150,40))
        self.font = pygame.font.Font("../assets/font.ttf", 10)
        self.speed = 0
        self.gear = 1
        self.rpm = 0

    # Update 
    def update(self, speed, rpm, gear):
        # Reset Dash
        self.surface.fill((0,255,0))
        self.surface.set_colorkey((0,255,0))

        # Display Speed
        self.surface.blit(
            self.font.render("Speed: "+str(speed)+" km/h", False, (0,0,0)),
            (0,0)
        )
        # Display RPM
        self.surface.blit(
            self.font.render("RPM: "+str(rpm)+" RPM", False, (0,0,0)),
            (0,15)
        )
        # Display Gear
        self.surface.blit(
            self.font.render("Gear "+str(gear), False, (0,0,0)),
            (0,30)
        )

# Car Class
class Car(pygame.sprite.Sprite):
    # Properties
    surface = None
    dash = None
    gear = 1
    gear_ratios = [3.56,2.53,1.68,1.02]
    rpm = 0
    speed = 0

    # Constructor
    def __init__(self, asset_location, start_position):
        # Call Sprite Constructor
        pygame.sprite.Sprite.__init__(self)

        # Classes
        self.dash = Dash()

        # Load Sprite
        self.surface = pygame.transform.scale(
            pygame.image.load(asset_location), 
            (int(32*1.5), int(62*1.5))
        )

        # Set start position
        self.actual_pos = start_position
        self.target_pos = start_position
        self.start_pos = start_position

    # Update Gearbox
    def update_gearbox(self, delta):
        # Plug in maths functions
        if self.rpm < 6500:
            self.rpm = int(self.rpm+20*5*delta)
        self.speed = maths.speed(self.rpm, self.gear, self.gear_ratios[self.gear-1])

    # Shift Down
    def shift_down(self):
        if self.gear > 1:
            self.gear -= 1

    # Shift Up
    def shift_up(self):
        if self.gear < 4:
            self.gear += 1
            self.rpm = 5000

    # Update Position Index
    def update_position_index(self, index):
        self.target_pos = (self.start_pos[0], self.start_pos[1] + 50*index)

    # Update
    def update(self, delta):
        # Position
        if self.actual_pos != self.target_pos:
            # Target Position under Actual Position
            if self.target_pos[1] > self.actual_pos[1]:
                self.actual_pos = (self.start_pos[0], self.actual_pos[1] + 2*delta)
            # Target Position over Actual Position
            if self.target_pos[1] < self.actual_pos[1]:
                self.actual_pos = (self.start_pos[0], self.actual_pos[1] - 2*delta)

        # Gearbox
        self.update_gearbox(delta)

        # Dash
        self.dash.update(self.speed, self.rpm, self.gear)
        print(self.speed, self.rpm, self.gear)

# Dynamic Scrolling Background
class BackgroundScroll(pygame.sprite.Sprite):
    def __init__(self, screenSize):
        self.virtual_screen = pygame.Surface(screenSize)
        self.sprite = pygame.image.load("../assets/scroll_bg.png")
        self.position = (0, -2400)

    def update(self, speed, delta):
        self.position = (0, self.position[1] + speed*delta)
        self.virtual_screen.fill((0,0,0))
        self.virtual_screen.blit(self.sprite, self.position)

    def surface(self):
        return self.virtual_screen
