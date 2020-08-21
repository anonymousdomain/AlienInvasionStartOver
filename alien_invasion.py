import pygame
import sys
from settings import Setting
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Setting()
        # initalize the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.ship = Ship(self)
        # set a caption
        pygame.display.set_caption("dev Godof War")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        self.ship.rect.x+=1
                    if event.key == pygame.K_LEFT:
                        self.ship.rect.x-=1
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
