import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Ball:
    def __init__(self,my_x,my_y,my_colour):
        self.x = my_x
        self.y = my_y
        self.height = 50
        self.width = 50
        self.colour = my_colour
    #end procedure 

    def draw(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.height,self.width])
    #end procedure

    def update(self):
        self.x = self.x + 1
    #end procedure
#end class

# my_ball = Ball(10,10,RED)
# my_ball2 = Ball(100,100,GREEN)

my_balls =  []
my_balls.append(Ball(10,10,RED))
my_balls.append(Ball(100,100,GREEN))


 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
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
    for ball in my_balls:
        ball.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    #pygame.draw.rect(screen,RED,[my_ball.x,my_ball.y,my_ball.height,my_ball.width])
    for ball in my_balls:
        ball.draw()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()