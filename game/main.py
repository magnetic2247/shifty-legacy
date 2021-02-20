import pygame

# Initialize pygame
pygame.init()

# Screen 
screen = pygame.display.set_mode([500, 500])

# Run until user quits
running = True
while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill Screen to reset it
    screen.fill((0,0,0))

    # Update Display
    pygame.display.flip()

# Quit!
pygame.quit()
    