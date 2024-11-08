def interpolate_8bit_color(start_color, end_color, steps, position):
    """ Interpolate between two 8-bit colors. """
    start_r, start_g, start_b = (start_color >> 5) & 0x7, (start_color >> 2) & 0x7, start_color & 0x3
    end_r, end_g, end_b = (end_color >> 5) & 0x7, (end_color >> 2) & 0x7, end_color & 0x3

    # Linear interpolation for each component
    r = int(start_r + (end_r - start_r) * (position / steps))
    g = int(start_g + (end_g - start_g) * (position / steps))
    b = int(start_b + (end_b - start_b) * (position / steps))

    # Combine back into an 8-bit color (3 bits red, 3 bits green, 2 bits blue)
    return (r << 5) | (g << 2) | b

# Define the 8-bit corner colors
top_left = 0b00000000    # Black
top_right = 0b11100000   # Red
bottom_left = 0b00000011 # Blue
bottom_right = 0b11111111 # White

# Grid size
grid_size = 16

# Generate the 16x16 grid of interpolated colors
grid = []
for y in range(grid_size):
    row = []
    # Interpolate between top-left to bottom-left for this row's left color
    left_color = interpolate_8bit_color(top_left, bottom_left, grid_size-1, y)
    # Interpolate between top-right to bottom-right for this row's right color
    right_color = interpolate_8bit_color(top_right, bottom_right, grid_size-1, y)

    for x in range(grid_size):
        # Interpolate between the left and right colors for each column
        color = interpolate_8bit_color(left_color, right_color, grid_size-1, x)
        row.append(color)
    
    grid.append(row)

# 'grid' now contains the 16x16 grid of 8-bit colors
print(grid)