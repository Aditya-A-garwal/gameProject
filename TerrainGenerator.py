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

def loadChunks(chunkBuffer, positionBuffer, chunkInd, persistence, noiseObj):
    posInBuff = 0
    for i in range(chunkInd-2, chunkInd+3):
        chunkAtPos = persistence[i]

        if(chunkAtPos == None):
            chunkAtPos = Chunk()
            populateChunk(chunkAtPos, noiseObj, i)
        else:
            pass

        chunkBuffer[posInBuff] = chunkAtPos
        positionBuffer[posInBuff] = i
        posInBuff+=1

class ChunkBuffer:

    def init(self, length, storageObj, chunkInd):

        self.storage = storageObj
        self.currChunk = chunkInd

        self.chunks = []
        self.positions = []

        if(length % 2 != 0):

            for i in range(int(self.currChunk-(length-1)*0.5), int(self.currChunk+1+(length-1)*0.5)):
                self.positions.append(i)
                tempObj = self.storage[i]
                if(tempObj == None):
                    tempObj = Chunk()
                    populateChunk(tempObj)
                self.chunks.append(tempObj)


    def shiftLeft(self):
        for i in range(0, len(self.positions)): self.positions[i] += 1
        self.storage[self.positions[0]] = self.chunks[0]
        for i in range(0, len(self.chunks)-1):
            self.chunks[i] = self.chunks[i+1]
        self.chunks[-1] = self.storage[self.positions[-1]]

    def shiftRight(self):
        for i in range(0, len(self.positions)): self.positions[i] -= 1

        self.storage[self.positions[-1]] = self.chunks[-1]
        for i in range(len(self.chunks), 0, -1):
            self.chunks[i] = self.chunks[i-1]
        self.chunks[0] = self.storage[self.positions[0]]

    def ___getitem__(self, key):
        return self.chunks[key]

    def __setitem__(self, key, value):
        self.chunks[key] = value



