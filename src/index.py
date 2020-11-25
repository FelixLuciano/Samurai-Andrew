import pygame
from pygame import display, mixer, surface, transform, time
from config import *

# Inicializa o processo do jogo e o mixer de som
pygame.init()
mixer.init()

# Inicializa a interface da tela
screen = display.set_mode(SCREEN_SIZE)
display.set_caption("Samurai Andrew")

# Cria a surface de desenho dos gráficos
picture = surface.Surface(PICTURE_SIZE)

# Clock para limitação do FPS
game_clock = time.Clock()

# Importação das fases do jogo
from start_screen import start_screen
from game_screen import game_screen

# Os elementos do jogo são desenhados numa surface em escala menor e ampliados para a resolução do screen
def renderer ():
    # Amplia os desenhos na picture
    screen.blit(transform.scale(picture, SCREEN_SIZE), SCREEN_ORIGIN)

    # Renderiza no display
    pygame.display.flip()

    # Limita a quantidade de quadros por segundos
    game_clock.tick_busy_loop(60)

# Estado do jogo
state = START_SCREEN

while not state == LEAVE_GAME:
    # Tela de inicio de jogo
    if state == START_SCREEN:
        state = start_screen(picture, renderer)

    # Tela de jogo
    elif state == GAME_SCREEN:
        state = game_screen(picture, renderer)

    # Saindo od jogo
    else:
        state = LEAVE_GAME

pygame.quit()
