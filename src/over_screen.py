from os.path import join
from random import randint
import pygame
from pygame import image
from pygame.time import delay

from config import *


def over_screen(screen, render):
    # Screen Assets
    game_over_path  = join(IMAGES_DIR, "game", "game_over.png")
    game_over_asset = image.load(game_over_path).convert()

    screen.blit(game_over_asset, SCREEN_ORIGIN)

    render()

    delay(2000)

    return LEAVE_GAME

