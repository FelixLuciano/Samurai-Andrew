from random import randint

from config import *
from Element import Element


class Fruit(Element):
  def __init__(self, assets):
    super().__init__(assets, initial_state = "entire")
    
    self.rect.top = PICTURE_HEIGHT / 2
    self.rect.x   = randint(0, PICTURE_WIDTH - self.rect.width)
    self.speedx   = randint(FRUIT_MIN_SPEEDX, FRUIT_MAX_SPEEDX)
    self.speedy   = randint(FRUIT_MIN_SPEEDY, FRUIT_MAX_SPEEDY)


  def update_dynamics(self):
    self.speedy -= 0.05


  def update(self):
    super().update_dynamics()
    self.update_dynamics()
