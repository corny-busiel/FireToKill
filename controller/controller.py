import pygame
import sys

class Controller():
    def __init__(self, start_menu):
        self.isPressed = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.isPressedMouse = pygame.mouse.get_pressed()[0]
        self.start_menu = start_menu  
    def event(self):
        
        # Обработка событий на кнопки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Если пользователь закрыл окно, завершаем Pygame и выходим из программы
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Проверяем, что нажата левая кнопка мыши (1)
                    x, y = event.pos  # Получаем координаты клика
                    self.handle_click(x, y)  # Обрабатываем клик
    
    def handle_click(self, x, y):
    # Обработка клика
        for i, item_rect in enumerate(self.start_menu.item_rects):
            if item_rect.collidepoint(x, y) and i < len(self.start_menu.text_menu):
               if i == 0:
                   print(1)
                   print(self.start_menu.item_rects)
               elif i == 1:
                   print(2)
               elif i == 2:
                   print(3)
               elif i == 3:
                   pygame.quit()
                   sys.exit()


                    
