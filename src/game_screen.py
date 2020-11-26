from os.path import join
from random import randint
import pygame
from pygame.sprite import Group
from pygame.time import delay

from config import *
from game import *

def game_screen(screen, render):
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

    # Sprites
    frutas = Group()
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
    player.sound("letsgo").play()

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
        
        # Adiciona as frutas voadoras aleatórias
        while len(frutas) <= FRUITS_MAX:
            length = len(frutas_assets)
            numero = random.randint(0, length)

            for i, asset in enumerate(frutas_assets):
                if numero == i:
                    frutas.add(Fruta(asset))
        
        # Corta as frutas com o cursor
        for fruta in frutas:
            if fruta.rect.collidepoint(cursor.position):
                fruta.kill()
                score += 10

        # Atualiza os Sprites
        frutas.update()
        players.update()

        # Desenha o plano de fundo
        screen.blit(ingame_asset, SCREEN_ORIGIN)

        # Desenha os Sprites
        frutas.draw(screen)
        players.draw(screen)

        score_surface = font.render(str(score), True, WHITE)

        screen.blit(score_surface, SCREEN_ORIGIN)

        cursor.draw(screen)
        
        render()

    return state
    
    
  