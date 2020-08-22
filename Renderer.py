import pygame
from pygame.locals import *
from Tile import *
from Chunk import *

'''
Translations

    From                        To

1   array-space                 chunk-space
    coordinates in the array    coordinates in the chunk

2   chunk-space                 world-space
    coordinates in the chunk    coordinates in the world (absolute coordinates)

3   world-space                 camera-space
    coordinates in the world    coordinates relative to camera

4   camera-space                screen-space
    coordinates in the array    coordinates on the display
'''


# Take a chunk and render it
def render(chunks, cameraCoors, displaySize, surface):
    """Renders given chunks onto given surface

    Requires chunks, cameraCoors, displaySize as sequences as surface as pygame.Surface
    """

    arrayToChunk = lambda coor: [coor[0] * 16, coor[1] * 16]  # From array-space to chunk-space
    chunkToGraph = lambda coor, chunkInd: [coor[0] + (chunkInd * 8 * 16), coor[1]]  # From chunk-space to absolute-space
    graphToCamera = lambda coor, camCoor: [coor[0] - camCoor[0], coor[1] - camCoor[1]]  # From absolute-space to camera-space
    cameraToScreen = lambda coor, dispSize: [coor[0] + dispSize[0]/2, dispSize[1]/2 - coor[1]]  # From camera-space to screen-space

    rects = []
    for c in range(0, len(chunks)):
        for i in range(int(cameraCoors[1]/16-displaySize[1]/42), int(cameraCoors[1]/16+displaySize[1]/32)):
            for j in range(0, chunkWidth):
                if (chunks[c][i, j] != None):
                    coors = arrayToChunk((j, i))
                    coors = chunkToGraph(coors, c)
                    coors = graphToCamera(coors, cameraCoors)
                    coors[1] += chunks[c][i, j].area[2] # Fix rendering offset to render from top-left instead of bottom-left
                    coors = cameraToScreen(coors, displaySize)

                    rects.append(surface.blit(chunks[c][i,j].texture, coors, chunks[c][i,j].area))
    return rects