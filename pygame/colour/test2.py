import pygame

pygame.init()

# Set window size
size = (880, 880)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("16x16 8-Bit Colour Grid with 24-Bit RGB Codes")

# Color palettes
bits_2 = [0x00, 0x55, 0xAA, 0xFF]  # 4 values for blue
bits_3 = [0x00, 0x24, 0x48, 0x6D, 0x92, 0xB6, 0xDB, 0xFF]  # 8 values for red and green

# Fill background
screen.fill(0xFFFFFF)

# Set square size
rect_size = 55  # Size of each square in the grid

# Set up font for text rendering
pygame.font.init()
font = pygame.font.SysFont('Arial', 12, bold=True)  # Font and size


def get_contrasting_color(r, g, b):
    """Return a contrasting color with better contrast based on input RGB values."""
    luminance = (299 * r + 587 * g + 114 * b) // 1000
    return (255, 255, 255) if luminance < 128 else (0, 0, 0)


    # Loop through a 16x16 grid
for count in range(0x100):
    col = (count & 0b11110000) >> 4
    row = (count & 0b00001111) 
    print(row,col)
    blue = bits_2[(count & 0b00000011)]
    red = bits_3[(count & 0b11100000) >> 5]
    green = bits_3[(count & 0b00011100) >> 2]
    # for col in range(16):
    #     # Distribute the red and green values smoothly:
    #     red = bits_3[(row ) // 2]   # Change every 2 rows
    #     green = bits_3[(col) // 2]  # Change every 2 columns

    #     # Distribute blue over larger blocks, changing less frequently
    #     blue = bits_2[(row // 4 + col // 4) % 4]  # Change every 4 rows and columns

        # Draw the color combination for each square
    pygame.draw.rect(screen, (red, green, blue), (col * rect_size, row * rect_size, rect_size, rect_size))

        # Create the RGB text to display
    color_code = f"{red:02X}{green:02X}{blue:02X}"
        
        # Get contrasting text color based on cell luminance
    text_color = get_contrasting_color(red, green, blue)
        
        # Render the text with the contrasting color
    text_surface = font.render(color_code, True, text_color)

    # Blit the text to the center of the rectangle
    text_rect = text_surface.get_rect(center=(col * rect_size + rect_size / 2, row * rect_size + rect_size / 2))
    screen.blit(text_surface, text_rect)

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
