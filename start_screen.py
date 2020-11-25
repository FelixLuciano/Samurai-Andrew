from os import path
import pygame
import random

from config import *


def start_screen (screen, render):
    # Screen Assets
    background_path  = path.join(IMAGES_DIR, "scene", "background.png")
    background_asset = pygame.image.load(background_path).convert()

    logo_path  = path.join(IMAGES_DIR, "game", "logo.png")
    logo_asset = pygame.image.load(logo_path).convert_alpha()

    intro_sount_path = path.join(SOUNDS_DIR, "Intro_musica.ogg")

    samurai_anderu_path = path.join(SOUNDS_DIR, "samurai_aneru.ogg")
    samurai_anderu      = pygame.mixer.Sound(samurai_anderu_path)
    samurai_anderu.set_volume(GAME_VOLUME)

    # Screen Sounds
    pygame.mixer.music.load(intro_sount_path)
    pygame.mixer.music.set_volume(GAME_VOLUME)
    pygame.mixer.music.play()

    samurai_anderu.play()

    screen.blit(background_asset, SCREEN_ORIGIN)
    screen.blit(logo_asset, (117, 11))

    state = START_SCREEN

    while state == START_SCREEN:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se o jogo foi fechado.
            if event.type == pygame.QUIT:
                state = LEAVE_GAME

            # Fecha a tela inicial se alguma tecla for pressionada
            if event.type == pygame.KEYUP:
                state = GAME_SCREEN

        render()

    return state
