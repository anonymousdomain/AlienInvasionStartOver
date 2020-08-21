import pygame


class Ship:
    def __init__(self, devo_game):
        # the argument devo_game used to call the instance of alineInvasion
        self.screen = devo_game.screen
        self.settings=devo_game.settings
        self.screen_rect = self.screen.get_rect()
        # load the image ship
        self.image = pygame.image.load("image/spaceship.bmp")
        self.rect = self.image.get_rect()
        # postion the ship in midd bottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.right_move = False
        self.left_move = False
        self.upper_move = False
        self.down_move = False
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def update(self):
        if self.right_move and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.left_move and self.rect.left>0:
            self.x-=self.settings.ship_speed
        if self.upper_move and self.rect.top>=0:
            self.y-=self.settings.ship_speed
        if self.down_move and self.rect.bottom< self.screen_rect.bottom:
            self.y+=self.settings.ship_speed
        self.rect.x=self.x
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
