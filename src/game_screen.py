from os import path
from random import randint
import pygame
from pygame.time import delay

from config import *
from game import *


def game_screen(screen, render):
    # Screen Assets
    background_path  = path.join(IMAGES_DIR, "scene", "background.png")
    background_asset = pygame.image.load(background_path).convert()

    logo_path  = path.join(IMAGES_DIR, "game", "logo.png")
    logo_asset = pygame.image.load(logo_path).convert_alpha()

    platforms_path  = path.join(IMAGES_DIR, "scene", "platforms.png")
    platforms_asset = pygame.image.load(platforms_path).convert_alpha()

    ingame_path  = path.join(IMAGES_DIR, "scene", "in-game.png")
    ingame_asset = pygame.image.load(ingame_path).convert()

    # Sounds
    playing_path  = path.join(SOUNDS_DIR, "musica_gaming.ogg")
    pygame.mixer.music.load(playing_path)
    pygame.mixer.music.set_volume(GAME_VOLUME)

    # Sprites
    all_frutas = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    

    # Musica da tela de jogo
    pygame.mixer.music.play(loops=-1)

    # Animação de introdução
    for i in range(0, 100, 1):
        screen.blit(background_asset, SCREEN_ORIGIN)
        screen.blit(logo_asset, (117, 11 + 200 * i/100))
        screen.blit(platforms_asset, (41, 103 + 70 * (1 - i/100)))

        render()


    # Adiciona o jogador
    all_sprites.add(player)
    player.sound("letsgo").play()
    
    
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
        
        # Adiciona as frutas voadoras
        while len(all_frutas) <= 15:
            numb = random.randint(0,2)
            if numb == 0:
                all_frutas.add(Fruta(maca_assests))
            if numb == 1:
                all_frutas.add(Fruta(banana_assests))
            if numb == 2:
                all_frutas.add(Fruta(melancia_assests))
        
        # Corta as frutas com o cursor
        for fruta in all_frutas:
            if fruta.rect.collidepoint(cursor.position):
                fruta.kill()

        # Atualiza os Sprites
        all_frutas.update()
        all_sprites.update()

        # Desenha o plano de fundo
        screen.blit(ingame_asset, SCREEN_ORIGIN)

        # Desenha os Sprites
        all_sprites.draw(screen)
        all_frutas.draw(screen)

        cursor.draw(screen)
        
        render()

    return state
    
    
  