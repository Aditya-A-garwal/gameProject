import pygame, numpy, sys, random
from pygame.locals import *
from Tile import *
from Chunk import *
from Renderer import *
from opensimplex import OpenSimplex

# Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()

# Screen variables
displaySize = [pygame.display.Info().current_w//2, pygame.display.Info().current_h//2]
prevFramerate = framerate = 0

# Camera variables
cam = [0,chunkHeight*16/2]
camInc = [0,0]
speed = currchunk = 0

# Create and display window
screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
pygame.display.set_caption("Hello World!")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

# Create chunk buffer and chunk-position buffer
chunkBuffer = []
chunkPos = []

# Create sample chunk buffer of length 7
chunks = [Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk()]

#Create noise object
gen = OpenSimplex()
noiseCoor = 0

# game loop
running = True
while running:

    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False #quit game if user leaves

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:     camInc[1] = 1
            elif event.key == pygame.K_a:   camInc[0] = -1
            elif event.key == pygame.K_s:   camInc[1] = -1
            elif event.key == pygame.K_d:   camInc[0] = 1

        elif event.type == pygame.KEYUP: camInc = [0, 0]

        elif event.type == pygame.VIDEORESIZE:
            pygame.display.Info()
            displaySize = [screen.get_width(), screen.get_height()]

    screen.fill((200, 200, 200))
    render(chunks, cam, displaySize, screen)

    # framerate calculation
    pygame.display.update()
    frameTime = clock.tick(framerate) + 1
    prevFramerate = 1000 / frameTime

    # Camera movement handling

    speed = 128 #Number of pixels to move per-second
    cam[0] += speed/prevFramerate * camInc[0]
    cam[1] += speed / prevFramerate * camInc[1]
    if(cam[1] > chunkHeight*16 or cam[1] < 0): cam[1] -= speed / prevFramerate * camInc[1]

    currChunk = cam[0]//(8*16)

    #print(int(cam[0]), int(cam[1])//16, int(currChunk), int(prevFramerate), sep="\t")
    print('-'*(int(gen.noise2d(x=noiseCoor, y=0)*64)+64))
    noiseCoor+=0.075
