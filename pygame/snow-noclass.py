import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# def addOne(x: int) -> int:
#   return x + 1

# print(addOne(2))

class Snow:
  #Private x as integer
  #Private y as integer
  def __init__(self, my_x, my_y, my_colour):
    self.x = my_x
    self.y = my_y
    self.colour = my_colour
  #end procedure

  def update(self):
    self.y = self.y + 1
    if self.y > 500:
      self.y = 0
      self.x = random.randint(0,700)
  #end procedure

  def draw(self):
    pygame.draw.rect(screen, self.colour, [self.x,self.y,10,10])

#end record



# Create the snow variables
snowflakes=[]
for _ in range(50):
  snowflake = Snow(random.randint(0,700),random.randint(0,700),random.choice([RED,WHITE,GREEN]) )
  snowflakes.append(snowflake)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow")
 
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
    for snow in snowflakes:
      snow.update()



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
 
    # --- Drawing code should go here
    for snow in snowflakes:
      snow.draw()
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()