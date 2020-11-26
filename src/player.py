from os import path

import pygame
from pygame import image, time
from pygame.transform import flip
from pygame.sprite import Sprite

from config import *
import scene
import utils


class Player (Sprite):
    def __init__ (self, assets):
        # Construtor da classe mãe (Sprite).
        Sprite.__init__(self)

        self.assets = assets
        self.flip   = 1
        self.state  = "standing"
        self.rect = self.image.get_rect()

        
        self.speedx = 0
        self.speedy = 0
        self.jumps = 0

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

    def event_handdler (self, event):
        if event.type == pygame.KEYDOWN:
            self.keydown(event.key)

        if event.type == pygame.KEYUP:
            self.keyup(event.key)


    def keydown (self, key):
        if key == ord('a'):
            if self.flip > 0:
                self.flip *= -1

            self.speedx = -PLAYER_RUNNING_SPEED

        if key == ord('d'):
            if self.flip < 0:
                self.flip *= -1

            self.speedx = PLAYER_RUNNING_SPEED

        if key == ord('w'):
            if self.jumps == 0:
                self.speedy = PLAYER_JUMPING_SPEED
                self.state = "jumping"
                
            elif self.jumps <= PLAYER_DOUBLE_JUMPING_LIMIT and self.speedx:
                self.speedy = PLAYER_DOUBLE_JUMPING_SPEED
                self.speedx = PLAYER_DASHING_SPEED * self.flip
                self.sound("special").play()

            self.jumps += 1

    def keyup (self, key):
        if key == ord('a'):
            self.speedx = 0
            self.state = "standing"

        if key == ord('d'):
            self.speedx = 0
            self.state = "standing"

    def update_dynamics (self):
        self.rect.x += self.speedx
        self.rect.y -= self.speedy
        self.speedy -= GRAVITY


    def update_colisions (self):
        # Colisão com as plataformas
        for platform in scene.platforms:
            if platform.colliderect(self.rect):
                # Jogador cstava caindo sobre a plataforma
                if self.speedy < 0:
                    # Jogador colide com a plataforma
                    self.rect.bottom = platform.top
                    self.speedy = 0
                    self.jumps = 0

                    # Jogador parado sobre uma plataforma
                    if self.speedx == 0 and not self.state == "standing":
                        self.state = "standing"

                    # Jogador correndo sobre uma plataforma
                    elif not self.speedx == 0 and not self.state == "running":
                        self.state = "running"

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

        # Manda o jogador pra cima quando cair do mapa
        if self.rect.top > SCREEN_HEIGHT * 1.2:
            self.kill()
    # Atualização do sprite do jogador
    @property
    def image (self):
        image = self.assets.images[self.state][self.frame]

        if self.flip < 0:
            return flip(image, True, False)

        return image
