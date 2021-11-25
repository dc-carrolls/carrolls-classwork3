import pygame
import random
# -- Global Constants


# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)


# Invader class

class Invader(pygame.sprite.Sprite):
    x_dir = 1
    x_speed = 1
    y_offset = 0
    screen_size = None # Need to set this attribute when screen size is set
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
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
        self.image.fill(YELLOW)
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

 
        
all_sprites_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
# Group of each bullet
bullet_group = pygame.sprite.Group()
invaders_x_pos_tpl = range(40, 480, 40)
invaders_y_pos_tpl = range(40, 220, 40)

for y_pos in invaders_y_pos_tpl:
    for x_pos in invaders_x_pos_tpl:
        my_invader = Invader(x_pos, y_pos)
        invader_group.add(my_invader)
        all_sprites_group.add(my_invader)

init_invader_len = len(invader_group)

my_player = Player()
all_sprites_group.add(my_player)

# -- Initialise PyGame 
pygame.init()

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)

# -- Blank Screen
size = (640, 480)
Invader.screen_size = size
screen = pygame.display.set_mode(size)

# -- Title of new window
pygame.display.set_caption("My Space Invaders")

# -- Exit game flag set to false
done = False
#game_over = False

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
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(RED, 2, 2, my_player.rect.x + 4, my_player.rect.y, my_player)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
            #end if
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                my_player.set_speed(0)
            #end if
        #end if               
    #Next event


    # -- Game logic here
    all_sprites_group.update()

    player_hit_list = pygame.sprite.spritecollide(my_player, invader_group, True)
    for _ in player_hit_list:
        my_player.lives = my_player.lives - 1

    for bullet in bullet_group:

        # See if it hit a block
        invader_hit_list = pygame.sprite.spritecollide(bullet, invader_group, True)

        # For each block hit, remove the bullet and add to the score
        for _ in invader_hit_list:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)
            my_player.score += 5
            

        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)

    # Change speed
    curr_invader_len = len(invader_group)
    if (init_invader_len - curr_invader_len) > 6:
        init_invader_len = curr_invader_len
        Invader.x_speed += 1
    #end if
    
    # -- Screen background is black
    screen.fill(BLACK)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("Lives: " + str(my_player.lives) + " Bullets: " + str(my_player.bullets) + " Score: " + str(my_player.score),True,WHITE)
     
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [0, 0])

    # -- Draw here

    all_sprites_group.draw(screen)
    # -- flip

    pygame.display.flip()
    clock.tick(60)


## -- end of game loop
#EndWhile
    
pygame.quit()


