import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF



pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow")


rows = 500
cols = 3   
arr = [[0 for i in range(cols)] for j in range(rows)]  
  
#arr[3][1] = 1 #assign value at row, column  
   
for row in range(rows):  
     arr[row][0] = random.randint(0,size[0]-1) #x vale
     arr[row][1] = random.randint(0,size[1]-1)
     arr[row][2] = 1
#next row       
#print(arr)  

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    for row in range(rows):
        if arr[row][1] > size[1]:
            arr[row][1] = 0
            arr[row][0] = random.randint(0,size[0]-1)
        else:
            arr[row][1] = arr[row][1] + 1

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
 
    # --- Drawing code should go here
    for row in range(rows):
        pygame.draw.rect(screen, WHITE, (arr[row][0],arr[row][1],5,5))  

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()