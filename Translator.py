"""Temporary module to perform translations on coordinates from array to screen"""

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

# Translate coordinates from array-space to chunk-space
def arrayToChunk(coor):
    return [coor[0]*16, coor[1]*16]

# Translate coordinates from chunk-space to absolute-space
def chunkToGraph(coor, chunkNumber):
    return [coor[0]+(chunkNumber*8), coor[1]]

# Translate coordinates from absolute-space to camera-space
def graphToCamera(coor, cameraCoor):
    return [coor[0]-cameraCoor[0], coor[1]-cameraCoor[1]]

# Translate coordinates from camera-space to screen-space
def cameraToScreen(coor, displaySize):
    return [coor[0], displaySize[1]-coor[1]]
