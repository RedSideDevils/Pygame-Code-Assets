import pygame 
from ui import Button

pygame.init()

width, height = RES = 800, 500  

screen = pygame.display.set_mode(RES)
pygame.display.set_caption("UI Demo")

run = True 

def render():
    screen.fill((255,255,255))
    btn.draw(screen, (0,0,0))

btn = Button(150, 225, (0, 255, 0), 250, 100, 'Click Me!')

while run:
    render()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn.isHover(pos):
                print('Button clicked')
        
        if event.type == pygame.MOUSEMOTION:
            if btn.isHover(pos):
                btn.color = (255,0,0)
            else:
                btn.color = (0,255,0)
                  
    pygame.display.update()
    
pygame.quit()