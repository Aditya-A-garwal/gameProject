import pygame
from Chunk import *
from Tile import *
from opensimplex import OpenSimplex
import random
walkingConstant = 0.02*random.random()*2.5

def populateChunk(chunk, noiseObj, chunkInd):
    coor = chunkInd * chunkWidth + random.randrange(5,15)
    print(walkingConstant, coor)
    for i in range(0, chunkWidth):
        height = int((noiseObj.noise2d(x=coor*walkingConstant, y=(random.randint(0,2)/75))+1)*32)  # Value will be from 0 to 64
        coor += 1
        for j in range(96, 95+height): chunk[j,i] = Grass()
