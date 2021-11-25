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

#Config
x, y = HW, HH
pmx, pmy = x, y
dx, dy = 0, 0
distance = 0

speed = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    mos = pygame.mouse.get_pressed()
    
    if mos[0] and not distance:
        mx, my = pygame.mouse.get_pos()
        
        radians = math.atan2(my - pmy, mx - pmx)
        distance = math.hypot(mx-pmx, my - pmy) / speed
        distance = int(distance)
        
        dx = math.cos(radians) * speed
        dy = math.sin(radians) * speed
        
        pmx, pmy = mx, my
        
    if distance:
        distance -= 1
        x += dx 
        y += dy
    
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 25, 0)
    
    if distance:
        pygame.draw.circle(screen, (255, 0, 0), (pmx, pmy), 5, 0)
    
    print(distance)    
    
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)