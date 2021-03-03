# Pygame Library
import pygame 

# Dynamic Scrolling Background
class BackgroundScroll(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, screenSize):
        """
        Entrée: Taille de l'écran
        Sortie: None
        """
        # Call Sprite Constructor
        pygame.sprite.Sprite.__init__(self)

        # Set Properties
        self.virtual_screen = pygame.Surface(screenSize)
        self.sprite = pygame.image.load("../assets/scroll_bg.png")
        self.position = (0, -2400)
        self.virtual_screen.fill((0,0,0))
        self.virtual_screen.blit(self.sprite, self.position)

    # Scroll (Update Function)
    def update(self, speed, delta):
        """
        Entrée: Vitesse de scroll, temps delta
        Sortie: None
        """
        self.position = (0, self.position[1] + speed*delta)
        self.virtual_screen.fill((94,176,46))
        self.virtual_screen.blit(self.sprite, self.position)

    # Returns Surface
    def surface(self):
        """
        Entrée: None
        Sortie: Background at current state
        """
        return self.virtual_screen