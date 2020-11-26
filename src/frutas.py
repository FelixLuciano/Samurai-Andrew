from os import path
import random

import pygame
from pygame import image, time, rect
from pygame.sprite import Sprite, spritecollide, collide_mask

from config import *
import scene
import utils



class Fruta (Sprite):
    def __init__ (self, assets):
        # Construtor da classe mãe (Sprite).
        Sprite.__init__(self)

        self.assets = assets
        self.state  = "inteira"
        self.rect = self.image.get_rect()
        self.rect.top = PICTURE_HEIGHT/2
        self.rect.x = random.randint(0, PICTURE_WIDTH-self.rect.width)
        # self

        
        self.speedx = random.randint(-1,2)
        self.speedy = random.randint(2,3)
        

        self.last_frame = 0

    @property
    def state (self):
        return self._state

    @state.setter
    def state (self, value):
        images = self.assets.images[value]

        self._state = value
        self.frames = len(images)
        self.frame = 0


    def sound (self, name):
        sounds = self.assets.sounds[name]
        sound  = utils.random_item(sounds)
        sound.set_volume(PLAYER_VOLUME)

        return sound


    def update_dynamics (self):
        self.rect.x += self.speedx
        self.rect.y -= self.speedy
        self.speedy -= 0.05


    def update_colisions (self):
        if self.rect.top > PICTURE_HEIGHT:
            self.kill()
        
    def update_frame(self):
        now = time.get_ticks()

        if now - self.last_frame > PLAYER_FRAME_DELAY:
            self.frame = (self.frame + 1) % self.frames
            self.last_frame = now


    # Funções chamadas pelo pygame

    # Atualização dos estados do jogador
    def update (self):
        self.update_dynamics()
        self.update_colisions()
        self.update_frame()


    # Atualização do sprite do jogador
    @property
    def image (self):
        image = self.assets.images[self.state][self.frame]

        return image


# class Cursor (Sprite):
#     def __init__ (self, cursor):
#         Sprite.__init__(self)

#         self.cursor = pygame.draw.rect(1,1)