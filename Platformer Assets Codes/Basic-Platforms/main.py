import pygame
import math, random, sys 
from pygame.locals import *

WIDTH, HEIGHT = RES = 800, 800
HW, HH = WIDTH / 2, HEIGHT / 2 
AREA = WIDTH*HEIGHT

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption('Direction Distance')
FPS = 120 

BLACK = (0,0,0,255)
WHITE = (255,255,255,255)

platform_y = HEIGHT - 50

collision_map = pygame.Surface((WIDTH, HEIGHT))
HIT = WHITE
MISS = BLACK
pygame.draw.line(collision_map, WHITE, (0, platform_y), (WIDTH, platform_y), 1)

player_x = HW
player_y = 0

falling_velocity = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    keys = pygame.key.get_pressed()
    

    # if player_y <= platform_y and player_y + falling_velocity >= platform_y:
    #     player_y = platform_y
    # else:
    #     player_y += falling_velocity
        
    collision = False
    
    for collision_y  in range(player_y, player_y + falling_velocity):
        color = collision_map.get_at((int(player_x), int(collision_y)))
        
        if color == HIT:
            collision = True
            player_y = collision_y
            break;
    
    if not collision:
        player_y += falling_velocity
        
    pygame.draw.circle(screen, WHITE, (player_x, player_y - 25), 25, 0)
    pygame.draw.line(screen, WHITE, (0, platform_y), (WIDTH, platform_y), 1)
    
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)