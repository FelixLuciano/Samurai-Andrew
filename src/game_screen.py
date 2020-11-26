from os import path
from os.path import join, dirname
import pygame
from pygame.time import delay


from config import *
from game import *
import scene
import random


def game_screen(screen, render):
    cursor_dir = join(dirname(__file__), "characters", "coronga", "images", "cursor", "0.png")
    #cursor_dir = pygame.transform.scale(cursor_dir,(1,1))
    cursor = pygame.image.load(cursor_dir).convert_alpha()
    cursor_rect = cursor.get_rect()
    # cursor = pygame.Rect((0, 0),(1,1))
    # cursor = (0, 0)
    cursor_state = False


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
    

    # Play Screen Sounds
    pygame.mixer.music.play(loops=-1)

    # Animação de introdução
    for i in range(0, 100, 1):
        screen.blit(background_asset, SCREEN_ORIGIN)
        screen.blit(logo_asset, (117, 11 + 200 * i/100))
        screen.blit(platforms_asset, (41, 103 + 70 * (1 - i/100)))

        render()


    all_sprites.add(player)
    player.sound("letsgo").play()
    
    
    state = GAME_SCREEN

    while state == GAME_SCREEN:
        #Processa os eventos (mouse, teclado, botão, e os sprites)
        for event in pygame.event.get():
            # Verifica se o jogo foi fechado.
            if event.type == pygame.QUIT:
                state = LEAVE_GAME

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    cursor_state = True
                    cursor_rect.centerx = pygame.mouse.get_pos()[0] * PICTURE_WIDTH / SCREEN_WIDTH
                    cursor_rect.centery = pygame.mouse.get_pos()[1] * PICTURE_HEIGHT / SCREEN_HEIGHT
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    cursor_state = False

            elif event.type == pygame.MOUSEMOTION:
                if cursor_state:
                    cursor_rect.centerx = pygame.mouse.get_pos()[0] * PICTURE_WIDTH / SCREEN_WIDTH
                    cursor_rect.centery = pygame.mouse.get_pos()[1] * PICTURE_HEIGHT / SCREEN_HEIGHT
                    
            # Eventos do jogador
            player.eventHanddler(event)

        screen.blit(ingame_asset, SCREEN_ORIGIN)
        

        while len(all_frutas) <= 15:
            numb = random.randint(0,2)
            if numb == 0:
                all_frutas.add(Fruta(maca_assests))
            if numb == 1:
                all_frutas.add(Fruta(banana_assests))
            if numb == 2:
                all_frutas.add(Fruta(melancia_assests))
                
        # print(cursor)
        for fruta in all_frutas:
            if fruta.rect.collidepoint(cursor_rect.centerx, cursor_rect.centery):
                print("COLIDIU")
                fruta.kill()
        
        # hit = pygame.sprite.spritecollide(cursor, all_frutas, True)
        # if hit:
        #     print("COLIDIU")
    
        # print(cursor_state, cursor.center)

        screen.blit(cursor, (cursor_rect.x, cursor_rect.y))

        all_frutas.update()
        all_sprites.update()
        all_sprites.draw(screen)
        all_frutas.draw(screen)
        
        render()

    return state
    
    
  