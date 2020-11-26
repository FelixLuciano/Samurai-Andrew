from os.path import join
from pygame import image
from pygame.mixer  import Sound

from config import *
from player import *
from scene import *
from frutas import *
from cursor import *



# Assets dos jogadores
from characters import samurai_andrew as andrew_assets
samurai_andrew = Player(andrew_assets)

from characters import kunoichi_barbara as barbara_assets
kunoichi_barbara = Player(barbara_assets)

from characters import ninja_diego as diego_assets
ninja_diego = Player(diego_assets)

# Jogador Principal
player = samurai_andrew
player.rect.x = 91
player.rect.bottom = 70

# Assets das frutas
from characters import melancia as melancia_assests
melancia_cortadas = Fruta(melancia_assests)

from characters import melancia as banana_assests
banana_cortadas = Fruta(banana_assests)

from characters import melancia as maca_assests
maca_cortadas = Fruta(maca_assests)

# Cursor
cursor_asset = join(ASSETS_DIR, "images", "game", "cursor.png")
cursor_skin = image.load(cursor_asset).convert_alpha()

cursor = Cursor(cursor_skin)
