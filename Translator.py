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
    """Translates given coordinates from array to in-chunk

    Requires coordinates as a sequence of length 2
    """
    return [coor[0]*16, coor[1]*16]

# Translate coordinates from chunk-space to absolute-space
def chunkToGraph(coor, chunkIndex):
    """Translates given coordinates from in-chunk to world

    Requires the coordinates as a sequence and the index of the chunk as an int
    """
    return [coor[0]+(chunkIndex*8), coor[1]]

# Translate coordinates from absolute-space to camera-space
def graphToCamera(coor, cameraCoor):
    """Translates given coordinates from world to relative to camera

    Requires the coordinates as a sequence and the coordinates of the camera as a sequence
    """
    return [coor[0]-cameraCoor[0], coor[1]-cameraCoor[1]]

# Translate coordinates from camera-space to screen-space
def cameraToScreen(coor, displaySize):
    """Translates given coordinates from relative to camera to screen

    Requires the coordinates as a sequence and the dimensions of the display area as a sequence
    """
    return [coor[0], displaySize[1]-coor[1]]
