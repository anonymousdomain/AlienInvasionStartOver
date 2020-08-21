import pygame

class Ship:
    def __init__(self,devo_game):
        # the argument devo_game used to call the instance of alineInvasion 
        self.screen=devo_game.screen
        self.screen_rect=self.screen.get_rect()
        #load the image ship
        self.image=pygame.image.load("image/spaceship.bmp")
        self.rect=self.image.get_rect()
        #postion the ship in midd bottom
        self.rect.midbottom=self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)