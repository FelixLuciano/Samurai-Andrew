from os import path
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

            # Eventos do jogador
            player.eventHanddler(event)

        screen.blit(ingame_asset, SCREEN_ORIGIN)
        all_sprites.draw(screen)

        all_sprites.update()

        render()

    return STATE
    
    
    # all_melancia = pygame.sprite.Group()
    # all_atk = pygame.sprite.Group()
    # # all_ground = pygame.sprite.Group()
    # groups = {}
    # groups["all_sprites"] = all_sprites
    # groups["all_melancia"] = all_melancia
    # groups["all_atk"] = all_atk
    # # groups["all_ground"] = all_ground
    



    # for i in range(28):
    #     meteor = Meteor(imagem)
    #     all_sprites.add(meteor)
    #     all_melancia.add(meteor)
    # DONE = 0
    # PLAYING = 1
    # EXPLODING = 2
    # state = PLAYING

    # score = 0
    # lives =  3
    #C:\Users\Cliquet\Documents\Desoft\Samurai_Andrew\img\Masterizados


            
        # Verifica se houve colisão entre tiro e meteoro
        # hits = pygame.sprite.groupcollide(all_melancia, all_atk, True, True)
        # for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
        #     # O meteoro e destruido e precisa ser recriado
        #     #assets["destroy_sound"].play()
            
        #     #imagem[hit].play()
        #     m = Meteor(imagem)
        #     all_sprites.add(m)
        #     all_melancia.add(m)

        #     # No lugar do meteoro antigo, adicionar uma explosão.
        #     explosao = Explosion(meteor.rect.center, imagem)
        #     all_sprites.add(explosao)

        #     # Ganhou pontos!
        #     score += 100

        # # Verifica se houve colisão entre nave e meteoro
        # hits = pygame.sprite.spritecollide(player, all_melancia, True)
        # if len(hits) > 0:
        #     # Toca o som da colisão
        #     hit = pygame.mixer.Sound("img/Masterizados/hit00.wav")
        #     hit.play()
        #     player.kill()
        #     lives -= 1
        #     explosao = Explosion(player.rect.center, imagem)
        #     all_sprites.add(explosao)
        #     state = EXPLODING
        #     keys_down = {}
        #     explosion_tick = pygame.time.get_ticks()
        #     explosion_duration = explosao.frame_ticks * len(explosao.cut_anim) + 400

        # if player.rect.top > HEIGHT:
        #     hit = pygame.mixer.Sound("img/Masterizados/hit02.wav")
        #     hit.play()
        #     player.kill()
        #     lives -= 1
        #     player = Jogador(groups, imagem, ground_rects)
        #     all_sprites.add(player)
        #     if lives == 0:
        #         state = DONE

        # elif state == EXPLODING:
        #     now = pygame.time.get_ticks()
        #     if now - explosion_tick > explosion_duration:
        #         if lives == 0:
        #             state = DONE
        #         else:
        #             state = PLAYING
        #             player = Jogador(groups, imagem, ground_rects)
        #             all_sprites.add(player)




        # Se o meteoro passar do final da tela, volta para cima

        #FUNDO DA TEKA
        # screen.fill(BLACK)
        # screen.blit(imagem["b_ground"],(0,0))
        # #screen.blit(imagem["fundo"] ,(200,100))
        # screen.blit(imagem["Casas"],(85,500))

        # #ADD SPRITES
        # #screen.blit(imagem["pilar"],(200,250))

        # #PONTOS
        # text_surface = imagem["score_font"].render("{:08d}".format(score), True, (255, 255, 0))
        # text_rect = text_surface.get_rect()
        # text_rect.midtop = (100,  110)
        # screen.blit(text_surface, text_rect)

        # #VIDA
        # text_surface = imagem["score_font"].render(chr(9829) * lives, True, (110, 30, 120))
        # text_rect = text_surface.get_rect()
        # text_rect.midtop = (100, 700)
        # screen.blit(text_surface, text_rect)
        
# def shoot(self):
#         # Verifica se pode atirar
#         now = pygame.time.get_ticks()
#         # Verifica quantos ticks se passaram desde o último tiro.
#         elapsed_ticks = now - self.last_shot

#         # Se já pode atirar novamente...
#         if elapsed_ticks > self.shoot_ticks:
#             # Marca o tick da nova imagem.
#             self.last_shot = now
#             # A nova bala vai ser criada logo acima e no centro horizontal da nave
#             new_atk = Atk(self.imagem, self.rect.top, self.rect.centerx)
#             self.groups['all_sprites'].add(new_atk)
#             self.groups['all_atk'].add(new_atk)