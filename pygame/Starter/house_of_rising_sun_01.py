import pygame 
# -- Global Constants 

# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
# -- Initialise PyGame 
pygame.init() 
# -- Blank Screen

size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Mr Carroll's Game") 
# -- Exit game flag set to false 
done = False 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()
circle_x_pos = 640
### -- Game Loop 
while not done: 
  # -- User input and controls 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      done = True 
    #End If 
  #Next event 
  # -- Game logic goes after this comment 
  if circle_x_pos < -40:
    circle_x_pos = 680
  else:
    circle_x_pos = circle_x_pos - 1
  # end if
  # -- Screen background is BLACK 
  screen.fill (BLACK) 
  # -- Draw here 
  pygame.draw.rect(screen, BLUE, (220,165,200,150)) 
  pygame.draw.circle(screen, YELLOW, (circle_x_pos,100),40,0) 
  # -- flip display to reveal new position of objects 
  pygame.display.flip() 
  # - The clock ticks over 
  clock.tick(60) 
#End While - End of game loop 
pygame.quit()