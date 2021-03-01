# Pygame Library
import pygame 

# Dynamic Scrolling Background
class BackgroundScroll(pygame.sprite.Sprite):
    def __init__(self, screenSize):
        self.virtual_screen = pygame.Surface(screenSize)
        self.sprite = pygame.image.load("../assets/scroll_bg.png")
        self.position = (0, -2400)
        self.virtual_screen.fill((0,0,0))
        self.virtual_screen.blit(self.sprite, self.position)

    def update(self, speed, delta):
        self.position = (0, self.position[1] + speed*delta)
        self.virtual_screen.fill((0,0,0))
        self.virtual_screen.blit(self.sprite, self.position)

    def surface(self):
        return self.virtual_screen