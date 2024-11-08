import pygame 
# -- Global Constants 

# -- Colours 
BLACK = (0x00,0x00,0x00) 
GREEN = (0x00,0xFF,0x00)
RED   = (0xFF,0x00,0x00)

# -- Initialise PyGame 
pygame.init() 
# -- Blank Screen

size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Moving Rectangle") 
# -- Exit game flag set to false 
done = False 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()
x_pos = 0
y_pos = 200
### -- Game Loop 
while not done: 
  # -- User input and controls 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      done = True 
    #End If 
  #Next event 
  # -- Game logic goes after this comment 
  if x_pos > 680:
    x_pos = -40
  else:
    x_pos = x_pos + 3
  if y_pos > 480:
    y_pos = -40
  else:
    y_pos = y_pos + 3
  # end if
  # -- Screen background is BLACK 
  screen.fill (GREEN) 
  # -- Draw here 
  pygame.draw.rect(screen, RED, (x_pos,y_pos,40,40))  
  # -- flip display to reveal new position of objects 
  pygame.display.flip() 
  # - The clock ticks over 
  clock.tick(60) 
#End While - End of game loop 
pygame.quit()