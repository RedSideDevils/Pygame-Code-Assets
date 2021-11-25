import pygame 

class Button:
    def __init__(self, x, y, color, width, height, text = ""):
        self.x = x   
        self.y = y   
        self.color = color
        self.width = width
        self.height = height
        self.text = text 
    
    def draw(self, win, outline = None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text , 1, (0,0,0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height/2 - text.get_height() / 2)))
    
    def isHover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True  
            
        return False   