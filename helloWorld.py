import pygame, numpy, sys, random
from pygame.locals import *
from opensimplex import OpenSimplex

from Tile import *
from Chunk import *
from Renderer import *
from TerrainGenerator import *

# Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()

# Screen variables
displaySize = [pygame.display.Info().current_w, pygame.display.Info().current_h]
prevFramerate = framerate = 0

# Camera variables
cam = [0,CHUNK_HEIGHT*16/2]

# Player variable
player = [0,CHUNK_HEIGHT*16/2]
playerInc = [0,0]
speed = currchunk = 0
movementDict = {pygame.K_w: 1, pygame.K_a: -1,pygame.K_s: -1, pygame.K_d: 1}

# Create and display window
screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
pygame.display.set_caption("Hello World!")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

# Create chunk buffer and chunk-position buffer
chunkBuffer = []
chunkPos = []

# Create sample chunk buffer of length 7
chunks = [Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk()]
for c in range(0, len(chunks)): populateChunk(chunks[c], OpenSimplex(), c)

#Create noise object
gen = OpenSimplex()
noiseCoor = 0

# game loop
running = True
while running:

    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #quit game if user leaves
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:     playerInc[1] = 1
            elif event.key == pygame.K_a:   playerInc[0] = -1
            if event.key == pygame.K_s:     playerInc[1] = -1
            elif event.key == pygame.K_d:   playerInc[0] = 1

            if event.key == pygame.K_ESCAPE:
                displaySize[0] = 800
                displaySize[1] = 600
                pygame.display.set_mode(displaySize, pygame.RESIZABLE)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:     playerInc[1] = 0
            elif event.key == pygame.K_a:   playerInc[0] = 0
            if event.key == pygame.K_s:     playerInc[1] = 0
            elif event.key == pygame.K_d:   playerInc[0] = 0

        elif event.type == pygame.VIDEORESIZE:
            pygame.display.Info()
            displaySize = [screen.get_width(), screen.get_height()]

    screen.fill((135,206,250))
    render(chunks, cam, player, displaySize, screen)

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
    cam[0] += (player[0]-cam[0])/12
    cam[1] += (player[1]-cam[1])/12
    currChunk = cam[0]//(8*16)

##    print(int(cam[0]), int(cam[1])//16, int(currChunk), int(prevFramerate), sep="\t")
    #print('-'*(int(gen.noise2d(x=noiseCoor, y=0)*64)+64))
pygame.display.quit()
