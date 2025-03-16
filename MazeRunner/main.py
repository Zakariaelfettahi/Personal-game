import pygame
import constants
from character import Player
pygame.init()

#<----SETTINGS---->
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Maze Runner")
clock = pygame.time.Clock()
 
#<-----VARIABLES---->
#define movement variables
jump = False
crouch = False
 
#<----FUNCTIONS----->
#image scaler function
def scale(img, scale):
     return pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))

#<----IMAGES---->
#player image
player_image = scale(pygame.image.load("assets/images/characters/elf/idle/0.png").convert_alpha(), constants.SCALE)
 
#<----CHARACTERS---->
# create a player
player = Player(300,600, 70, 120, player_image)
 
 
#<----MAIN_LOOP---->
#main game loop
running = True
while running:
 
    #control speed of the game
    clock.tick(constants.FPS)
 
    screen.fill(constants.BG_COLOR)
 
    #calculate movement
    dx =0
    dy=0
    
    #introduce gravity
    player.gravity()

    #move logic
    if jump:
       player.jump()
    
    
    #draw player
    player.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #take keyboard presses
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_UP:
                jump = True
            if event.key == pygame.K_DOWN:
                crouch = True
        # check if button is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                jump = False
            if event.key == pygame.K_DOWN:
                crouch = False
    pygame.display.update()
pygame.quit()