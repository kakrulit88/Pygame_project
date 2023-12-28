import pygame
import sys
from level import Level
from hud import *

SIZE = HEIGHT, WIDTH = 1280, 720
FPS = 60


class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('game')
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game_start = Game()
