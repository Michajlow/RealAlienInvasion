import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('totalship.bmp')
        # image.load("")
        
        self.rect = self.image.get_rect()
        #translate the picture into rectangle
        self.screen_rect = screen.get_rect()
        #translate screen into rectangle

        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        #pointing the position of the image rectangle on the screen rectangle
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
		
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def center_ship(self):
        self.center = self.screen_rect.centerx

        

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # blit() - shows the object on the screen






