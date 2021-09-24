import pygame
from pygame import image, time

from config import *
import utils
from scene import platforms
from Element import Element


class Player(Element):
  def __init__(self, assets):
    super().__init__(assets, initial_state = "standing")

    self.jumps = 0


  def event_handdler(self, event):
    if event.type == pygame.KEYDOWN:
      self.keydown(event.key)

    if event.type == pygame.KEYUP:
      self.keyup(event.key)


  def keydown(self, key):
    if key == ord('a'):
      self.speedx = -PLAYER_RUNNING_SPEED

      if self.flip > 0:
        self.flip *= -1

    elif key == ord('d'):
      self.speedx = PLAYER_RUNNING_SPEED

      if self.flip < 0:
        self.flip *= -1

    elif key == ord('w'):
      if self.jumps == 0:
        self.speedy = PLAYER_JUMPING_SPEED
        self.state = "jumping"

      elif self.jumps <= PLAYER_DOUBLE_JUMPING_LIMIT and self.speedx:
        self.speedy = PLAYER_DOUBLE_JUMPING_SPEED
        self.speedx = PLAYER_DASHING_SPEED * self.flip
        self.sound("special").play()

      self.jumps += 1


  def keyup(self, key):
    if key == ord('a'):
      self.speedx = 0
      self.state = "standing"

    elif key == ord('d'):
      self.speedx = 0
      self.state = "standing"


  def update_dynamics(self):
    super().update_dynamics()

    self.speedy -= GRAVITY


  def update_colisions_platforms(self, platforms):
    for platform in platforms:
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


  def update(self):
    self.update_dynamics()
    self.update_colisions_platforms(platforms)
