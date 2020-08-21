import pygame
import sys

class AlienInvasion:
    def __init__(self):
        pygame.init()
        #initalize the screen
        self.screen=pygame.display.set_mode((1200,600))
        #set a caption
        pygame.display.set_caption("dev Godof War")
        self.bg_color=(255,255,255)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
if __name__ == "__main__":
    ai=AlienInvasion()
    ai.run_game()