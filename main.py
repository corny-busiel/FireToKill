import pygame
from view import view
import asyncio

async def main():
    game = view.View()
    game.__init__()
    while True:
        game.update()    

if __name__ == "__main__":
    asyncio.run(main())