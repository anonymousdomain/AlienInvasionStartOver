import pygame
import sys
from settings import Setting
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Setting()
        # initalize the screen
        #self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               #self.settings.screen_height))
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width 
        self.settings.screen_height=self.screen.get_rect().height
        self.ship = Ship(self)
        # set a caption
        pygame.display.set_caption("dev Godof War")

    def run_game(self):
        while True:
            self.ship.update()
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event
                
                )
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
       
        if event.key == pygame.K_RIGHT:
            self.ship.right_move = True
        if event.key == pygame.K_LEFT:
            self.ship.left_move = True
        if event.key == pygame.K_UP:
            self.ship.upper_move = True
            
        if event.key == pygame.K_DOWN:
            self.ship.down_move = True
        if event.key==pygame.K_q:
            sys.exit()

    def _check_keyup_event(self,event):
       
        if event.key == pygame.K_RIGHT:
            self.ship.right_move = False
        if event.key == pygame.K_LEFT:
            self.ship.left_move = False
        if event.key == pygame.K_UP:
            self.ship.upper_move = False
        if event.key == pygame.K_DOWN:
            self.ship.down_move = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
