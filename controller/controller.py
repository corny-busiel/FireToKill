import pygame
import sys

class Controller():
    def __init__(self):
        self.isPressed = False
        
    def event(self):
        # Обработка событий на кнопки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Если пользователь закрыл окно, завершаем Pygame и выходим из программы
                pygame.quit()
                sys.exit()
