import pygame

class View():
    
    def __init__(self):
        # Инициализация Pygame
        pygame.init()
        
        # Задаем цвет фона (черный)
        self.background = (0, 0, 0)
        
        # Задаем размер экрана
        self.width = 1200
        self.height = 800
        
        # Создаем окно Pygame
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        # Задаем заголовок окна
        pygame.display.set_caption("Fire to Kill")
        
    def update(self):
        # Заполняем экран цветом фона
        self.screen.fill(self.background)
        
        # Отображаем изменения на экране
        pygame.display.flip()