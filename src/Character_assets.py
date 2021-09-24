from os.path import join, dirname, sep, splitext
from path import Path
from glob import glob
import pygame

class Character_assets:
  def __init__(self, path_str):
    self.assets = dict()

    # Encontra os assets dentro das pastas
    path = path_str.split("/")
    modules = Path(dirname(__file__)).glob(join(*path, "**", "**", "*"))

    for path in modules:
      # Separa arquivo das as duas ultimas pastas parentes do caminho
      *directory, dtype, key, filename = path.split(sep)

      # Separa nome e formato do arquivo
      file_split  = splitext(filename)
      name, extension  = file_split

      # Registra pasta do tipo de asset
      if not dtype in self.assets:
        self.assets[dtype] = {}

      # Registra o nome do asset
      if not key in self.assets[dtype]:
        self.assets[dtype][key] = []

      # Lida com arquivos de imagem
      if extension in (".png", ".jpg"):
        asset = pygame.image.load(path).convert_alpha()

      # Lida com arquivos de som
      elif extension in (".ogg", ".wav", ".mp3"):
        asset = pygame.mixer.Sound(path)

      # Registra o asset ou variação do mesmo no escopo do programa
      self.assets[dtype][key].append(asset)


  def get_assets(self):
    return self.assets
