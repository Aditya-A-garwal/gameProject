import pygame


class Tile:

    def __init__(self, imgpath, offset=(0, 0), area=(16, 16)):
        self.texture = pygame.image.load("Assets/"+imgpath)
        self.area = (offset[0], offset[1], area[0], area[1])
        self.timeval = 0


class Grass(Tile):

    def __init__(self):
        super().__init__("grass.png")


class Stone(Tile):

    def __init__(self):
        super().__init__("stone.png")


class Bedrock(Tile):

    def __init__(self):
        super().__init__("bedrock.png")
