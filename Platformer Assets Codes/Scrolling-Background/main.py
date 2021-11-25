import pygame
import math, random, sys 
from pygame.locals import *

WIDTH, HEIGHT = RES = 1280, 720
HW, HH = WIDTH / 2, HEIGHT / 2 
AREA = WIDTH*HEIGHT

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption('Background Scrolling')
FPS = 500 

BLACK = (0,0,0,255)
WHITE = (255,255,255,255)

#Config
bg = pygame.image.load('assets/bg.png').convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 2
stagePosX  = 0

startScrollingPosX = HW

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 585
playerVelocityX = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    k = pygame.key.get_pressed()
    
    if k[K_RIGHT]:
        playerVelocityX = 1
    
    elif k[K_LEFT]:
        playerVelocityX = -1
    
    else:
        playerVelocityX = 0
    
    playerPosX += playerVelocityX
    
    if playerPosX > stageWidth - circleRadius:
        playerPosX = stageWidth - circleRadius
    
    if playerPosX < circleRadius:
        playerPosX = circleRadius
    
    if playerPosX < startScrollingPosX:
        circlePosX = playerPosX
    
    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX - stageWidth + WIDTH
    
    else:
        circlePosX = startScrollingPosX
        stagePosX += -playerVelocityX
    
    rel_x = stagePosX % bgWidth
    screen.blit(bg, (rel_x - bgWidth, 0))
    
    if rel_x < WIDTH:
        screen.blit(bg, (rel_x, 0))
    
    pygame.draw.circle(screen, WHITE, (circlePosX,playerPosY - circleRadius), circleRadius, 0)
    
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)