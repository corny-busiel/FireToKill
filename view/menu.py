import pygame

class Menu():
    
    def __init__(self, screen):
        self.screen = screen
        self.background = (70, 70, 70)
        self.color = (255, 255, 255)
        self.size_font = 80
        self.font = pygame.font.Font(None, self.size_font)
        self.text_menu = ["Новая игра", "Продолжить", "Настройки", "Выход"]
        
    def menu_draw(self, width, height):
        text = self.font.render("Меню", True, self.color, self.background)
        self.text_rect = text.get_rect(center = (width // 2, height // 5))
        self.screen.blit(text , self.text_rect)
        height_text = height // 3
        for item in self.text_menu:
            items = self.font.render(item, True, self.color)
            self.text_rect = items.get_rect(center = (width // 2, height_text))
            self.screen.blit(items, self.text_rect)
            height_text +=  100