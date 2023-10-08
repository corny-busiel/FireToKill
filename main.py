import pygame
from view import view, menu  # Импорт класса View
import asyncio
from controller import controller

async def main():
    # Создаем экземпляр класса View
    game = view.View()
    start_menu = menu.Menu(game.screen)
    controllers = controller.Controller(start_menu)
      
    while True:
        controllers.event()
        game.screen.fill(game.background)
        start_menu.menu_draw(game.width, game.height)
        
        
        
        
        
        pygame.display.flip()

if __name__ == "__main__":
    asyncio.run(main())