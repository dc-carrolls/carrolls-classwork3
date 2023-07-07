'Main Game Module'
from time import *
import pygame

class Invader(pygame.sprite.Sprite):
    x_dir = 1
    x_speed = 1
    y_offset = 0
    screen_size = None # Need to set this attribute when screen size is set
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(Colour.BLUE)
        self.rect = self.image.get_rect()
        self.y_orig_pos = y_pos 
        self.rect.x = x_pos
        self.rect.y = y_pos
    #end procedure

    def update(self):            
        if self.rect.x > self.__class__.screen_size[0] - 10:
            self.__class__.y_offset = self.__class__.y_offset + 5
            self.__class__.x_dir = -1
        elif self.rect.x < 0:
            self.__class__.y_offset = self.__class__.y_offset + 5
            self.__class__.x_dir = 1            
        #endif
        self.rect.x = self.rect.x + self.__class__.x_dir * self.__class__.x_speed
        self.rect.y = self.y_orig_pos + self.__class__.y_offset
    #end procedure
#end class

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(Colour.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 640 / 2
        self.rect.y = 480 - 40
        self.speed = 0
        self.lives = 3
        self.bullets = 1000
        self.score = 0
    #end procedure
        
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x > 640 - 10:
            self.rect.x = 640 - 10
        elif self.rect.x < 0:
            self.rect.x = 0
        #endif
    #end procedure

    def set_speed(self,my_speed):
        self.speed = my_speed
    #end procedure

    def get_speed(self):
        return self.speed
    #end function
#end class

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, colour, height, width, x_pos, y_pos, my_player):
        super().__init__()
        my_player.bullets = my_player.bullets - 1 
        self.colour = colour
        self.height = height
        self.width = width
        self.speed = 2
        self.image = pygame.Surface((self.height,self.width))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
    def update(self):
        self.rect.y = self.rect.y - self.speed
    #    if self.rect.y < 0:

        #endif
    #end procedure

    def set_speed(self,my_speed):
        self.speed = my_speed
    #end procedure

    def get_speed(self):
        return self.speed
    #end function
#end class


class Level:
  def __init__(self):
    sprite_group_list = []
  #end constructor

  def update(self):
    for sprite_group in self.sprite_group_list:
      sprite_group.update()
    #next sprite_group
  #end procedure
#end class


class Level1(Level):
  def __init__(self):
     super().__init__()
     

class Colour:
  'Static Colour Class'
  BLACK :tuple[int, int, int] = (0, 0, 0)
  WHITE :tuple[int, int, int] = (255, 255, 255)
  GREEN :tuple[int, int, int] = (0, 255, 0)
  RED   :tuple[int, int, int] = (255, 0, 0)
#end class

class Game:
  'Static Game Class'
  lives :int = 5
  score :int = 0
  screen_size :tuple[int, int] = (700, 500)
  screen = None
  caption :str = "My Static Game"
  game_over :bool = False
  clock = None

  @classmethod
  def run(cls, seconds :int):
    'main game method for starting game'
    pygame.init()

    # Set the width and height of the screen [width, height]
   
    cls.screen = pygame.display.set_mode(cls.screen_size)
    pygame.display.set_caption(cls.caption)
    cls.clock = pygame.time.Clock()

    while not cls.game_over:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.game_over = True
    
        # --- Game logic should go here
    
        # --- Screen-clearing code goes here
    
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
    
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        cls.screen.fill(Colour.WHITE)
    
        # --- Drawing code should go here
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        cls.clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

  #end procedure
#end class


if __name__ == "__main__":
  Game.run(1)
else:
  print('loading',__name__ ,'as module')
#end if
