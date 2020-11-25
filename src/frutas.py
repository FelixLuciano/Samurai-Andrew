from os import path
import random

import pygame
from pygame import image, time
from pygame.sprite import Sprite

from config import *
import scene
import utils




class Frutas(Sprite):
    def __init__(self, assets):
        
        Sprite.__init__(self)

        self.state = 'caindo'

        self.assests = assests
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-)
        self.rect.y = random.randint(-100, -FRUTAS_HEIGHT)
        self.speedx = random.randint(-1, 2)
        self.speedy = random.randint(10, 20)

        def update(self):
        # Atualização das frutas
            self.rect.x += self.speedx


        # Mantem dentro da tela
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

    def update_dynamics (self):
        self.rect.x += self.speedx
        self.rect.y -= self.speedy
        self.speedy -= GRAVITY
        
        #Reposiciona as frutas se passarem da tela
        if self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.rect.x = random.randint(0, SCREEN_WIDTH-FRUTAS_WIDTH)
            self.rect.y = random.randint(-100, -FRUTAS_HEIGHT)
            self.speedx = random.randint(-1, 2)
            self.speedy = random.randint(10, 20)
