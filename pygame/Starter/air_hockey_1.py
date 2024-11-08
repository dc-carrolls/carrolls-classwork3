import pygame 
import random
# -- Global Constants 

# -- Colours 

BLACK = (0x00,0x00,0x00) 
WHITE = (0xFF,0xFF,0xFF)
RED   = (0xFF,0x00,0x00)
TABLE_CLR = (0x33,0xCC,0xFF)

# -- Initialise PyGame 
pygame.init() 
# -- Blank Screen

screen_size = (640,480) 
screen_x, screen_y = screen_size
screen = pygame.display.set_mode(screen_size) 
# -- Title of new window/screen 
pygame.display.set_caption("Moving Rectangle") 
# -- Exit game flag set to false 
done = False 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

# Initial Values
puck_x_pos = 0
puck_y_pos = 200<<5
puck_x_vel = 150
puck_y_vel = 50
puck_x_dir = 1
puck_y_dir = 1
puck_width = 10<<5
puck_height = 10<<5

font = pygame.font.SysFont('Calibri', 16, False, False)
text = font.render(f"x velocity:{puck_x_vel} y velocity:{puck_y_vel}",True,BLACK)

### -- Game Loop 
while not done: 
  # -- User input and controls 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      done = True 
    #End If 
  #Next event 
  # -- Game logic goes after this comment 
  if puck_x_pos > ((screen_x<<5) - puck_width) or puck_x_pos < 0:
    puck_x_dir = puck_x_dir * -1
    puck_y_vel = random.randint(4,20) * 15

  puck_x_pos = puck_x_pos + puck_x_vel*puck_x_dir
  if puck_y_pos > ((screen_y<<5) - puck_height) or puck_y_pos < 0:
    puck_y_dir = puck_y_dir * -1
    puck_x_vel = random.randint(4,20) * 20

  puck_y_pos = puck_y_pos + puck_y_vel*puck_y_dir
  puck_x_vel-=1
  if puck_x_vel < 40:
    puck_x_vel = 40

  puck_y_vel-=1
  if puck_y_vel < 40:
    puck_y_vel = 40
  text = font.render(f"x velocity:{puck_x_vel} y velocity:{puck_y_vel}",True,BLACK)

   # y_pos = y_pos + y_vel*y_dir
  # end if
  # -- Screen background is BLACK 
  screen.fill (TABLE_CLR) 
  # -- Draw here 
  pygame.draw.rect(screen, RED, (puck_x_pos>>5,puck_y_pos>>5,puck_width>>5,puck_height>>5))  
  screen.blit(text, [5, 5])
  # -- flip display to reveal new position of objects 
  pygame.display.flip() 
  # - The clock ticks over 
  clock.tick(60) 
#End While - End of game loop 
pygame.quit()