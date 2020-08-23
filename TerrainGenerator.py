import pygame
from Chunk import *
from Tile import *
from opensimplex import OpenSimplex
import random
WALKING_CONSTANT = 0.0075

def populateChunk(chunk, noiseObj, chunkInd):
    coor = chunkInd * CHUNK_WIDTH
    #print(WALKING_CONSTANT, coor)
    for i in range(0, CHUNK_WIDTH):
        height = int((noiseObj.noise2d(x=coor*WALKING_CONSTANT, y=0)+1)*32)  # Value will be from 0 to 64
        coor += 1
        for j in range(96, 95+height): chunk[j,i] = Grass()
