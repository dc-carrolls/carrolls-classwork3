import pygame

pygame.init()

# Set window size
size = (880, 880)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("16x16 8-Bit Colour Grid with 24-Bit RGB Codes")

# Color palettes
# bits_2 = [0x00, 0x55, 0x55, 0x55, 0xAA, 0xAA, 0xAA, 0xFF]  # 4 values for blue
bits_2 = [0x00, 0x55, 0xAA, 0xFF]  # 4 values for blue
bits_3 = [0x00, 0x24, 0x48, 0x6D, 0x92, 0xB6, 0xDB, 0xFF]  # 8 values for red and green

# Fill background
screen.fill(0xFFFFFF)

# Set starting position and square size
x = 0
y = 0
rect_size = 55  # Size of each square in the grid

# Set up font for text rendering
pygame.font.init()
font = pygame.font.SysFont('Arial', 12,bold=True)  # Font and size


def get_contrasting_color(r, g, b):
    """Return a contrasting color with better contrast based on input RGB values."""
    
    # Calculate luminance using integer math
    luminance = (299 * r + 587 * g + 114 * b) // 1000
    
    if luminance < 128:
        # If the color is dark, significantly brighten it
        # Ensure we don't exceed 255 by limiting to the max value
        return (min(r + 150, 255), min(g + 150, 255), min(b + 150, 255))
    else:
        # If the color is light, significantly darken it
        return (int(r * 0.3), int(g * 0.3), int(b * 0.3))
    
# Loop through a 16x16 grid
for row in range(16):
    for col in range(16):
        # Use row and col to index into the bits_3 and bits_2 arrays
        red = bits_3[((row//2) % 8)]   # Repeat every 8 rows
        green = bits_3[col // 4 ] # Repeat every 8 columns
        blue = bits_2[col % 4]  # Ensure 4 distinct blue values

        # Draw the color combination for each square
        pygame.draw.rect(screen, (red, green, blue), (x, y, rect_size, rect_size))

        # Create the RGB text to display
        color_code = f"{red:02X}{green:02X}{blue:02X}"
        
        # Get contrasting text color based on cell luminance
        text_color = get_contrasting_color(red, green, blue)
        
        # Render the text with the contrasting color
        text_surface = font.render(color_code, True, text_color)

        # Blit the text to the center of the rectangle
        text_rect = text_surface.get_rect(center=(x + rect_size / 2, y + rect_size / 2))
        screen.blit(text_surface, text_rect)

        # Move to the next cell in the row
        x += rect_size

    # Move to the next row after completing a row of 16 squares
    y += rect_size
    x = 0  # Reset column position for the new row

# Update display
pygame.display.flip()

# Main program loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(60)

# Close pygame window
pygame.quit()
