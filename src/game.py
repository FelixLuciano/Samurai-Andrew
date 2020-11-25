from os import path
from pygame import image
from pygame.mixer  import Sound

from config import *
from player import *
from scene import *

from characters import samurai_andrew as andrew_assets
samurai_andrew = Player(andrew_assets)

from characters import kunoichi_barbara as barbara_assets
kunoichi_barbara = Player(barbara_assets)

from characters import ninja_diego as diego_assets
ninja_diego = Player(diego_assets)


# from frutas import frutas as frutas_assests
# frutas_cortadas = Frutas(frutas_assests)

player = samurai_andrew
player.rect.x = 91
player.rect.bottom = 70


