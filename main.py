import pygame
from debug import debug

pygame.init()

# Display dimensions
display_width = 800
display_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create game display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')

# Game loop
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                debug('up')
            elif event.key == pygame.K_DOWN:
                debug('down')
            elif event.key == pygame.K_LEFT:
                debug('left')
            elif event.key == pygame.K_RIGHT:
                debug('right')

    # Fill display with white
    game_display.fill(white)

    # Draw game objects
    # ...

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
quit()
