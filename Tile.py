import pygame

TILE_TABLE = {1:"grass.png", 2:"stone.png", 3:"bedrock.png"}
TILE_WIDTH = 16

def loadImages():
    for i in range(1, len(TILE_TABLE)+1):
        TILE_TABLE[i] = pygame.image.load("Assets/"+TILE_TABLE[i])

class Tile:

    def __init__(self, code, rect=(0,0,TILE_WIDTH,TILE_WIDTH)):
        self.code = code
        self.rect = rect


class Grass(Tile):

    def __init__(self):
        super().__init__(1)


class Stone(Tile):

    def __init__(self):
        super().__init__(2)


class Bedrock(Tile):

    def __init__(self):
        super().__init__(3)
