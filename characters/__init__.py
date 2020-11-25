from os.path import join, dirname, sep, splitext
from path import Path
from glob import glob

import pygame

def load_assets(__file):
    # Encontra os assets dentro das pastas
    __modules = Path(dirname(__file)).glob(join("**", "**", "*"))

    # Escopo global para armazenamento dos assets de forma programática
    __l = locals()

    for __module in __modules:
        # Separa arquivo das as duas ultimas pastas parentes do caminho
        *dir, __type, __key, __file = __module.split(sep)

        # Separa nome e formato do arquivo
        __splitext  = splitext(__file)
        __filename  = __splitext[0]
        __extension = __splitext[1]

        # Registra pasta do tipo de asset
        if not __type in __l:
            __l[__type] = {}
            
        # Registra o nome do asset
        if not __key in __l[__type]:
            __l[__type][__key] = []

        # Lida com arquivos de imagem
        if __extension in (".png", ".jpg"):
            __asset = pygame.image.load(__module).convert_alpha()

        # Lida com arquivos de som
        elif __extension in (".ogg", ".wav", ".mp3"):
            __asset = pygame.mixer.Sound(__module)

        # Não lida com arquivos diferentes
        else:
            continue

        # Registra o asset ou variação do mesmo no escopo do programa
        __l[__type][__key].append(__asset)

    return __l
