import pygame
from view import view  # Импорт класса View
import asyncio

async def main():
    # Создаем экземпляр класса View
    game = view.View()

    while True:
        game.update()  # Обновляем игру в цикле

if __name__ == "__main__":
    asyncio.run(main())