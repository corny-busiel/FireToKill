import pygame

class View():
    
    def __init__(self):
        self.initialization = pygame.init
        self.background = (0, 0 , 0)
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name = pygame.display.set_caption("Fire to Kill")
        
    def update(self):
        self.screen.fill(self.background)
        self.flip = pygame.display.flip()