import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
screen_size = (700, 500)

# Create the window
screen = pygame.display.set_mode(screen_size)

# Set the title
pygame.display.set_caption('Space Invaders')

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load the player image
player_image = pygame.image.load('player.png')
player_rect = player_image.get_rect()

# Load the enemy image
enemy_image = pygame.image.load('enemy.png')
enemy_rect = enemy_image.get_rect()

# Set the enemy starting position
enemy_rect.x = random.randint(0, screen_size[0] - enemy_rect.width)
enemy_rect.y = 0

# Set the player starting position
player_rect.x = screen_size[0] / 2
player_rect.y = screen_size[1] - player_rect.height

# Set the movement speed
move_speed = 5

# Set the game loop flag
running = True

# Start the game loop
while running:
    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the enemy down
    enemy_rect.y += move_speed

    # Check if the enemy has reached the bottom of the screen
    if enemy_rect.y > screen_size[1]:
        # Reset the enemy position
        enemy_rect.x = random.randint(0, screen_size[0] - enemy_rect.width)
        enemy_rect.y = 0

    # Clear the screen
    screen.fill(black)

    # Draw the player and enemy
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
