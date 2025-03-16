import pygame
import constants

class Player:
    def __init__(self, x, y, w, h, image):
        self.image = image
        self.rect = pygame.Rect(x, y, w, h)
        self.vel_y = 0 
        self.gravity_force = constants.GRAVITY_FORCE  
        self.jump_strength = constants.JUMP_STRENGTH 
        self.on_ground = False

    def gravity(self):
        self.vel_y += self.gravity_force  
        self.rect.y += self.vel_y  

        # Collision with the ground
        if self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.rect.bottom = constants.SCREEN_HEIGHT
            self.vel_y = 0  
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_strength  
            self.on_ground = False  
         
    def draw(self,area):
         area.blit(self.image, self.rect)
         pygame.draw.rect(area, constants.RED , self.rect, 1)