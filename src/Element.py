from pygame import time
from pygame.transform import flip
from pygame.sprite import Sprite

from config import *
import utils


class Element(Sprite):
  def __init__(self, assets, initial_state = "initial"):
    Sprite.__init__(self)

    self.assets   = assets.get_assets()
    self.flip     = 1
    self.frame    = 0
    self.frames   = 1
    self.last_frame = 0
    self.state    = initial_state
    self.rect     = self.get_image().get_rect()

    self.speedx = 0
    self.speedy = 0

    self.set_state(initial_state)


  def get_state(self):
    return self.state

  def set_state(self, value):
    images = self.assets["images"][value]

    self.state  = value
    self.frames = len(images)
    self.frame  = 0


  def get_image(self):
    image = self.assets["images"][self.get_state()][self.frame]

    if self.flip < 0:
      return flip(image, True, False)

    self.update_frame()

    return image

  @property
  def image (self):
    return self.get_image()


  def get_sound(self, name):
    sounds = self.assets["sounds"][name]
    sound  = utils.random_item(sounds)

    sound.set_volume(PLAYER_VOLUME)

    return sound


  def update_frame(self):
    now = time.get_ticks()

    if now - self.last_frame > PLAYER_FRAME_DELAY:
      self.frame = (self.frame + 1) % self.frames
      self.last_frame = now


  def update_dynamics (self):
    self.rect.x += self.speedx
    self.rect.y -= self.speedy

    if self.rect.top > SCREEN_HEIGHT * 1.2:
        self.kill()
