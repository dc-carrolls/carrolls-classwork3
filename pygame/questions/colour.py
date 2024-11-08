import pygame

# Initialize PyGame
pygame.init()

# Set up the window dimensions
width, height = 600, 400
window = pygame.display.set_mode((width, height))

# Define some initial parameters
x1 = 0  # Starting x position of the square
x2 = -width
y = height // 2 - 25  # Centered vertically
square_size = 50  # Size of the square
speed = 1  # Speed of the square

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color gradient (you will complete this)
    for i in range(height):
        # Calculate the color based on i
        color_value = int((i / height) * 255)
        pygame.draw.line(window, (color_value, color_value, color_value), (0, i), (width, i))

    # Move the square (you will complete this)
    x1 += speed
    x2 += speed
    if x1 > x2:
        if x1 > width:
            x1 = -width
    else:
        if x2 > width:
            x2 = -width

    # Draw the square (already implemented)
    pygame.draw.rect(window, (255, 0, 0), (x1, y, square_size, square_size))
    pygame.draw.rect(window, (255, 0, 0), (x2, y, square_size, square_size))

    # Update the display
    pygame.display.update()

    # Ensure the square wraps around the screen (you will complete this)
    clock.tick(60)
# Quit PyGame
pygame.quit()
