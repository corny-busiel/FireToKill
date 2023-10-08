import pygame

class Menu():
    
    def __init__(self, screen):
        # Инициализация объекта меню
        self.screen = screen
        self.background = (70, 70, 70)  # Цвет фона меню
        self.color = (255, 255, 255)    # Цвет текста
        self.size_font = 80             # Размер шрифта
        self.font = pygame.font.Font(None, self.size_font)
        self.text_menu = ["Новая игра", "Продолжить", "Настройки", "Выход"]  # Элементы меню
        self.item_rect = None
        
    def menu_draw(self, width, height):
        # Отрисовка меню
        
        # Отрисовка заголовка меню
        title_text = self.font.render("Меню", True, self.color, self.background)
        title_rect = title_text.get_rect(center=(width // 2, height // 5))
        self.screen.blit(title_text, title_rect)
        
        # Отрисовка элементов меню
        height_text = height // 3
        for item in self.text_menu:
            item_text = self.font.render(item, True, self.color)
            self.item_rect = item_text.get_rect(center=(width // 2, height_text))
            self.screen.blit(item_text, self.item_rect)
            height_text += 100  # Увеличиваем вертикальное смещение для следующего элемента
