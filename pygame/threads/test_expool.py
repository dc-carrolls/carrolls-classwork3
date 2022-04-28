import concurrent.futures
import pygame
from time import sleep
from random import randint
 

def task(limit): 
  print('start task') 
  x = 0
  while x < limit:
    x += 1
  print('end task')
  return "result"




if __name__ == '__main__':

# Define some colors
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  GREEN = (0, 255, 0)
  RED = (255, 0, 0)

  run_task = True
  x_pos = 0

  executor = concurrent.futures.ProcessPoolExecutor()
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
        


      if run_task:
        print('running')
        run_task = False
        e = executor.submit(task,100000000)
        x_pos = 0
      elif e.done():
        print(e.result())
        run_task=True 
        
      x_pos += 1


  
      # --- Screen-clearing code goes here
  
      # Here, we clear the screen to white. Don't put other drawing commands
      # above this, or they will be erased with this command.
  
      # If you want a background image, replace this clear with blit'ing the
      # background image.
      screen.fill(WHITE)
  
      # --- Drawing code should go here
      pygame.draw.rect(screen, RED, [x_pos,100,10,10])  

      # --- Go ahead and update the screen with what we've drawn.
      pygame.display.flip()
  
      # --- Limit to 60 frames per second
      clock.tick(60)
  
  # Close the window and quit.
  pygame.quit()


