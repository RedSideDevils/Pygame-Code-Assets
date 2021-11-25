import pygame 
from pygame.locals import *

pygame.init()

class Player(object):
    def __init__(self, x, y, radius, screen):
        self.x = x 
        self.y = y 
        self.vel = 0
        self.screen = screen
        self.colors = {
            'BLACK' : (0, 0, 0),
            'WHITE' : (255, 255, 255),
            'RED' : (255,0, 0)
        }
        self.radius = radius
        self.jumping = False
        self.jump_offset = 0
        self.jump_height = 80
        self.return_force = 2
           
    def __str__(self):
        return "Player Class: X|{}, Y|{}, VEL|{}".format(self.x, self.y, self.vel)
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[K_RIGHT]:
            self.vel = 1
        
        elif keys[K_LEFT]:
            self.vel = -1

        else:
            self.vel = 0
        
        if keys[K_SPACE] and self.jumping == False and self.jump_offset == 0:
            self.jumping = True
        
        self.x += self.vel
        
    def do_jump(self):
        if self.jumping:
            self.jump_offset += self.return_force
            
            if self.jump_offset >= self.jump_height:
                self.jumping = False
                
        elif self.jump_offset > 0 and self.jumping == False:
            self.jump_offset -= self.return_force
            
    def draw(self):
        pygame.draw.circle(self.screen, self.colors['RED'], (self.x, self.y - self.jump_offset), self.radius)