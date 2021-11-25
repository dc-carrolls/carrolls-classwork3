import pygame
import random
# -- Global Constants


# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# Invader class

class Invader(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.x_speed = 1
        self.y_speed = 0
    #end procedure

    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed
        if self.rect.x > 640 - 10:
            self.y_speed = 20
            self.x_speed = -1
        elif self.rect.x < 0:
            self.y_speed = 20
            self.x_speed = 1            
        else:
            self.y_speed = 0
        #endif
    #end procedure
#end class

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 640 / 2
        self.rect.y = 480 - 40
        self.speed = 0
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
        
all_sprites_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
invaders_x_pos_tpl = range(40, 520, 40)
invaders_y_pos_tpl = range(40, 220, 40)

for y_pos in invaders_y_pos_tpl:
    for x_pos in invaders_x_pos_tpl:
        my_invader = Invader(x_pos, y_pos)
        invader_group.add(my_invader)
        all_sprites_group.add(my_invader)

my_player = Player()
all_sprites_group.add(my_player)

# -- Initialise PyGame 
pygame.init()

# -- Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# -- Title of new window
pygame.display.set_caption("My Space Invaders")

# -- Exit game flag set to false
done = False


# -- Manage how fast scren refreshes
clock = pygame.time.Clock()


# -- Game loop

while not done:
    # - user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_player.set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                my_player.set_speed(3)
            #end if
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                my_player.set_speed(0)
            #end if
        #end if               
    #Next event


    # -- Game logic here
    all_sprites_group.update()
    
    # -- Screen background is black
    screen.fill(BLACK)

    # -- Draw here

    all_sprites_group.draw(screen)
    # -- flip

    pygame.display.flip()
    clock.tick(60)


## -- end of game loop
#EndWhile
    
pygame.quit()


