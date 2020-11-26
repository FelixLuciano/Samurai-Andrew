from os import path
import random

import pygame
from pygame import image, time, rect
from pygame.sprite import Sprite, spritecollide, collide_mask

from config import *
import scene
import utils


class Mouse (Sprite):
    def __init__()