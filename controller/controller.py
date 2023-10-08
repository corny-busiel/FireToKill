import pygame
import sys

class Controller():
    def __init__(self):
        self.isPressed = False
        
    def event(self, start_menu):
        
        # Обработка событий на кнопки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Если пользователь закрыл окно, завершаем Pygame и выходим из программы
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if start_menu.item_rect.collidepoint(x, y) and "Выход" in start_menu.text_menu:
                        pygame.quit()
                        sys.exit()