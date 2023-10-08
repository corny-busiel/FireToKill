import pygame
from view import view  # Импорт класса View
import asyncio
from controller import controller

async def main():
    # Создаем экземпляр класса View
    game = view.View()
    controllers = controller.Controller()
    
    
    while True:
        controllers.event()
        game.update()  # Обновляем игру в цикле

if __name__ == "__main__":
    asyncio.run(main())