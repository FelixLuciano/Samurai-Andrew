import pygame
from pygame.sprite import Sprite
from pygame.mouse import get_pos

from config import *

class Cursor (Sprite):
    def __init__ (self, skin):
        Sprite.__init__(self)

        self.image = skin
        self.rect = skin.get_rect()
        self.is_pressed = False

    @property
    def position (self):
        x = self.rect.centerx
        y = self.rect.centery

        return x, y

    def event_handler (self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = get_pos()[0] * PICTURE_WIDTH / SCREEN_WIDTH
                y = get_pos()[1] * PICTURE_HEIGHT / SCREEN_HEIGHT

                self.rect.centerx = x
                self.rect.centery = y
                self.is_pressed = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_pressed = False

        elif event.type == pygame.MOUSEMOTION:
            x = get_pos()[0] * PICTURE_WIDTH / SCREEN_WIDTH
            y = get_pos()[1] * PICTURE_HEIGHT / SCREEN_HEIGHT

            self.rect.centerx = x
            self.rect.centery = y

    def draw(self, screen):
        screen.blit(self.image, self.position)
