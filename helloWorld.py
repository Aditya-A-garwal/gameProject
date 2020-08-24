import pygame, numpy, sys, random
from pygame.locals import *
from opensimplex import OpenSimplex

from Tile import *
from Chunk import *
from Renderer import *
from TerrainGenerator import *

from databaseIO import *

# Screen variables
displaySize = [0,0]
prevFramerate = framerate = 0

# Camera variables
cam = [0,CHUNK_HEIGHT*16/2]

# Player variables
player = [0,CHUNK_HEIGHT*16/2]
playerInc = [0,0]
speed = currchunk = 0
movementDict = [{pygame.K_a: -1, pygame.K_d: 1}, {pygame.K_w: 1, pygame.K_s: -1}]

#Create noise object
gen = OpenSimplex()

# Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()
displaySize = [pygame.display.Info().current_w//2, pygame.display.Info().current_h//2]

# Create and display window
screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
pygame.display.set_caption("Hello World!")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

# Create a database object
storage = DBIO("myWorld")

# Create chunk buffer and chunk-position buffer
chunkBuffer = [None, None, None, None, None]
chunkPos = [None, None, None, None, None]

loadChunks(chunkBuffer, chunkPos, 0, storage, gen)

# game loop
running = True
while running:

    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False #quit game if user leaves

        elif event.type == pygame.KEYDOWN:
            if event.key in movementDict[0]: playerInc[0] = movementDict[0][event.key]
            if event.key in movementDict[1]: playerInc[1] = movementDict[1][event.key]

        elif event.type == pygame.KEYUP:
            if event.key in movementDict[0]: playerInc[0] = 0
            if event.key in movementDict[1]: playerInc[1] = 0

        elif event.type == pygame.VIDEORESIZE:
            pygame.display.Info()
            displaySize = [screen.get_width(), screen.get_height()]



    screen.fill((30, 175, 250))
    render(chunkBuffer, chunkPos, cam, player, displaySize, screen)
    loadChunks(chunkBuffer, chunkPos, currChunk, storage, gen)

    # Framerate calculation
    pygame.display.update()
    frameTime = clock.tick(framerate) + 1
    prevFramerate = 1000 / frameTime

    # Player movement handling
    speed = 128  # Number of pixels to move per-second
    player[0] += (speed/prevFramerate) * playerInc[0]
    player[1] += (speed/prevFramerate) * playerInc[1]
    if not(0 < player[1] < (CHUNK_HEIGHT*16)): player[1] -= (speed / prevFramerate) * playerInc[1]

    # Camera movement handling
    cam[0] += (player[0]-cam[0]) * 0.1
    cam[1] += (player[1]-cam[1]) * 0.1
    currChunk = int(cam[0]//(CHUNK_WIDTH*16))



##    print(int(cam[0]), int(cam[1])//16, int(currChunk), int(prevFramerate), sep="\t")
    #print('-'*(int(gen.noise2d(x=noiseCoor, y=0)*64)+64))
pygame.display.quit()
