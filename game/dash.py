# Pygame library
import pygame

# Dash Display
class Dash(pygame.sprite.Sprite):
    # Properties
    surface = pygame.Surface((150,40))
    font = None

    # Constructor
    def __init__(self):
        # Call Sprite Constructor
        pygame.sprite.Sprite.__init__(self)

    # Update 
    def update(self, rpm, gear, text=" "):
        # Font
        if self.font == None:
            self.font = pygame.font.Font("../assets/font.ttf", 10)

        # Reset Dash
        self.surface.fill((0,255,0))
        self.surface.set_colorkey((0,255,0))

        # Display RPM
        self.surface.blit(
            self.font.render(str(rpm)+" RPM", False, (0,0,0)),
            (0,0)
        )
        # Display Gear
        self.surface.blit(
            self.font.render("Gear "+str(gear), False, (0,0,0)),
            (0,15)
        )
        # Display Text for Debug
        self.surface.blit(
            self.font.render(text, False, (0,0,0)),
            (0,30)
        )
