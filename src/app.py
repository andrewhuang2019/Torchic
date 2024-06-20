import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Rectangle")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up rectangle properties
rect_x = 50
rect_y = 50
rect_width = 50
rect_height = 50
rect_speed_x = 5
rect_speed_y = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the rectangle
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bounce the rectangle off the edges
    if rect_x < 0 or rect_x + rect_width > width:
        rect_speed_x = -rect_speed_x
    if rect_y < 0 or rect_y + rect_height > height:
        rect_speed_y = -rect_speed_y

    # Clear the screen
    screen.fill(black)

    # Draw the rectangle
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
pygame.quit()
sys.exit()