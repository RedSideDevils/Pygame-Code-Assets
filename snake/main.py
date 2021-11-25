import pygame 
from random import randrange

RES = 800 
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1  
snake = [(x,y)]
dx, dy = 0, 0
fps = 5 

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))
   
    #Add Borders
    for i in range(0, RES // 50):
        pygame.draw.rect(sc, pygame.Color('yellow'), (0, i * SIZE, SIZE, SIZE))
        pygame.draw.rect(sc, pygame.Color('yellow'), (i * SIZE, 0, SIZE, SIZE))
        pygame.draw.rect(sc, pygame.Color('yellow'), (i * SIZE, RES - SIZE, SIZE, SIZE))
        pygame.draw.rect(sc, pygame.Color('yellow'), (RES - SIZE, i * SIZE, SIZE, SIZE))
        

    for i, j in snake:
        pygame.draw.rect(sc, pygame.Color('white'), (i, j, SIZE, SIZE))
        
    pygame.draw.rect(sc, pygame.Color('red'), (*apple,SIZE,SIZE))
    
    #snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x,y))
    snake = snake[-length:]
    
    #Eating Apple
    
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length+=1
        fps+=1
        
    #Game Over
    
    if x < SIZE or x > RES - SIZE * 2 or y < SIZE or y > RES - SIZE * 2:
        break;
    
    if len(snake) != len(set(snake)):
        break;
    
    pygame.display.flip()
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
        
    if keys[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}

    if keys[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    
    if keys[pygame.K_d] and dirs['D']:
        dx, dy =  1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
        
        