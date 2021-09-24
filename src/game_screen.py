from os.path import join
from random import randint
import pygame
from pygame import image
from pygame.sprite import Group
from pygame.mixer  import Sound
from pygame.time import delay

from config import *
from Character_assets import Character_assets
from Player import Player
from Fruit import Fruit
from Cursor import Cursor


# Screen Assets
background_path  = join(IMAGES_DIR, "scene", "background.png")
background_asset = pygame.image.load(background_path).convert()

logo_path  = join(IMAGES_DIR, "game", "logo.png")
logo_asset = pygame.image.load(logo_path).convert_alpha()

platforms_path  = join(IMAGES_DIR, "scene", "platforms.png")
platforms_asset = pygame.image.load(platforms_path).convert_alpha()

ingame_path  = join(IMAGES_DIR, "scene", "in-game.png")
ingame_asset = pygame.image.load(ingame_path).convert()

# Sounds
playing_path  = join(SOUNDS_DIR, "musica_gaming.ogg")
pygame.mixer.music.load(playing_path)
pygame.mixer.music.set_volume(GAME_VOLUME)

# Fonts assets
font_dir = join(FONTS_DIR, 'PressStart2P.ttf')
font = pygame.font.Font(font_dir, FONT_SIZE)

# Assets dos jogadores
samurai_andrew_assets = Character_assets("assets/characters/samurai_andrew")
samurai_andrew = Player(samurai_andrew_assets)

# kunoichi_barbara_assets = Character_assets("assets/characters/kunoichi_barbara")
# kunoichi_barbara = Player(kunoichi_barbara_assets)

# ninja_diego_assets = Character_assets("assets/characters/ninja_diego")
# ninja_diego = Player(ninja_diego_assets)

# Jogador Principal
player = samurai_andrew
player.rect.x = 91
# player.rect.bottom = 0
player.rect.y = 50

apple_assests = Character_assets("assets/characters/apple")
banana_assests = Character_assets("assets/characters/banana")
watermelon_assests = Character_assets("assets/characters/watermelon")

# Assets das frutas
# from characters import melancia as melancia_assests
# from characters import melancia as banana_assests
# from characters import melancia as maca_assests

fruits_assets = (apple_assests, banana_assests, watermelon_assests)

# Cursor
cursor_asset = join(ASSETS_DIR, "game", "images", "game", "cursor.png")
cursor_skin = image.load(cursor_asset).convert_alpha()

cursor = Cursor(cursor_skin)


def game_screen(screen, render):
  # Sprites
  fruits = Group()
  players = Group()

  # Musica da tela de jogo
  pygame.mixer.music.play(loops=-1)

  # Animação de introdução
  for i in range(0, 100, 1):
    screen.blit(background_asset, SCREEN_ORIGIN)
    screen.blit(logo_asset, (117, 11 + 200 * i/100))
    screen.blit(platforms_asset, (41, 103 + 70 * (1 - i/100)))

    render()

  # Adiciona o jogador
  players.add(player)
  player.get_sound("letsgo").play()

  score = 0
  lives = 3
  
  # Inicia jogo
  state = GAME_SCREEN

  while state == GAME_SCREEN:
    #Processa os eventos (mouse, teclado, botão, e os sprites)
    for event in pygame.event.get():
      # Eventos do jogador
      player.event_handdler(event)

      # Eventos do cursor
      cursor.event_handler(event)

      # Verifica se o jogo foi fechado.
      if event.type == pygame.QUIT:
        state = LEAVE_GAME
    
    # Adiciona as fruits voadoras aleatórias
    while len(fruits) <= FRUITS_MAX:
      length = len(fruits_assets)
      random_index = randint(0, length - 1)
      fruit_asset = fruits_assets[random_index]
      fruit = Fruit(fruit_asset)

      fruits.add(fruit)
    
    # Corta as fruits com o cursor
    for fruta in fruits:
      if fruta.rect.collidepoint(cursor.get_position()):
        fruta.kill()
        score += 10

    if not players:
      lives -= 1

      if lives == 0:
        state = OVER_SCREEN
      else:
        players.add(player)
        player.rect.x = 91
        player.rect.bottom = 0

    # Atualiza os Sprites
    fruits.update()
    players.update()

    # Desenha o plano de fundo
    screen.blit(ingame_asset, SCREEN_ORIGIN)

    # Desenha os Sprites
    fruits.draw(screen)
    players.draw(screen)

    score_surface = font.render(str(score), True, WHITE)

    screen.blit(score_surface, SCREEN_ORIGIN)
    live_surface = font.render(str(lives), True, WHITE)
    screen.blit(live_surface, (300,150))
    cursor.draw(screen)
    
    render()

  return state
  
  
  