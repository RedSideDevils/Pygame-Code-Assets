import pygame
from Player import  Player
from pygame.locals import *

WIDTH, HEIGHT = RES = 800, 800
HW, HH = WIDTH / 2, HEIGHT / 2 
AREA = WIDTH*HEIGHT

#Config
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption('Direction Distance')
FPS = 120

#Objects
Player = Player(HW, HH, 25, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    Player.move()
    Player.do_jump()
    Player.draw()
    print(Player) 
    pygame.display.update()
    clock.tick(FPS)
    screen.fill((0,0,0))