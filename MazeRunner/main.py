import pygame
import constants
from character import Character
pygame.init()
 
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Maze Runner")
 
#create a clock
clock = pygame.time.Clock()
 
#define movement variables
move_left = False
move_right = False
move_up = False
move_down = False
 
#player image
player_image = pygame.image.load("assets/images/characters/elf/idle/0.png").convert_alpha()
 
 
# create a player
player = Character(100,100, player_image)
 
 
#main game loop
running = True
while running:
 
    #control speed of the game
    clock.tick(constants.FPS)
 
    screen.fill(constants.BG_COLOR)
 
    #calculate movement
    dx=0
    dy=0
 
    #move logic
    if move_down:
        dy = +constants.SPEED
    if move_up:
        dy = -constants.SPEED
    if move_left:
        dx = -constants.SPEED
    if move_right:
        dx = +constants.SPEED
 
    #move player
    player.move(dx,dy)
 
    #draw player
    player.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_down = True
        # check if button is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_down = False
    pygame.display.update()
pygame.quit()