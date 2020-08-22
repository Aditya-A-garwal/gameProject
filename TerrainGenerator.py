import pygame
from Chunk import *
from Tile import *
from opensimplex import OpenSimplex

walkingConstant = 0.05

def populateChunk(chunk, noiseObj, chunkInd):
    coor = chunkInd * chunkWidth
    for i in range(0, chunkWidth):
        height = int((noiseObj.noise2d(x=coor*walkingConstant, y=0)+1)*32)  # Value will be from 0 to 64
        coor += 1
        for j in range(96, 95+height): chunk[j,i] = Grass()