import pygame, numpy, sys, random
from pygame.locals import *
from Tile import *
from Chunk import *
from Renderer import *

# Screen variables
displaySize = [800, 600]
lastframerate = framerate = 0

# Camera variables
cam = [0,0]
camInc = [0,0]
speed = currchunk = 0

# Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()

# Create and display window
screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
pygame.display.set_caption("Hello World!")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

# Create chunk buffer and chunk-position buffer
chunkBuffer = []
chunkPos = []

# Create sample chunk buffer of length 7
chunks = [Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk()]

# game loop
running = True
while running:

    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False #quit game if user leaves

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:     camInc[1] = 8/prevFramerate
            elif event.key == pygame.K_a:   camInc[0] = -8/prevFramerate
            elif event.key == pygame.K_s:   camInc[1] = -8/prevFramerate
            elif event.key == pygame.K_d:   camInc[0] = 8/prevFramerate

        elif event.type == pygame.KEYUP: camInc = [0, 0]

        elif event.type == pygame.VIDEORESIZE:
            pygame.display.Info()
            displaySize = [screen.get_width(), screen.get_height()]

    screen.fill((255, 255, 255))
    render(chunks, cam, displaySize, screen)

    # framerate calculation
    pygame.display.update()
    frameTime = clock.tick(framerate) + 1
    prevFramerate = 1000 / frameTime

    # Camera movement handling
    speed = 16
    cam[0] += speed * camInc[0]
    cam[1] += speed * camInc[1]

    currChunk = cam[0]//(8*16)

    print(int(cam[0]), int(cam[1]), int(currChunk), int(prevFramerate), sep="\t")
