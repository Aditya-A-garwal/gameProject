import pygame, numpy, sys, random
from pygame.locals import *
from Tile import *
from Chunk import *
from Translator import *

# Screen variables
displaySize = [800, 600]
lastframerate = framerate = 0

# Camera variables
cam = [0,0]
camInc = [0,0]
speed = currchunk = relx = 0

# Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()

# Create and display window
screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
pygame.display.set_caption("Terraria")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

# Create sample chunk buffer of length 5
chunks = [Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk(), Chunk()]

# Take a chunk and render it
def renderChunk(chnks, camera, display):
    for c in range(0, len(chnks)):
        chunk = chnks[c]
        for i in range(0, 256):
            for j in range(0, 8):
                tile = chunk[i,j]

                coors = arrayToChunk((j, i))
                coors = chunkToGraph(coors, c)

                coors = graphToCamera(coors, camera)
                coors = cameraToScreen(coors, displaySize)

                coors[1] -= tile.area[2]

                if(tile != None): screen.blit(tile.texture, coors, tile.area)

    #pygame.draw.circle(screen, (0,0,0), (0,0), 20)
    #pygame.draw.circle(screen, (255, 255, 255), cameraToScreen(camera, displaySize), 18)
    #pygame.draw.circle(screen, (0, 0, 0), cameraToScreen(camera, displaySize), 2)

'''
# randomely populate chunk with tiles
for i in range(0, 256, 1):
    for j in range(0, 8, 1):
        blockType = random.randint(0, 4)
        if(blockType == 0): myChunk[(i,j)] = Grass()
        elif(blockType == 1): myChunk[(i,j)] = Stone()
        elif(blockType == 3): myChunk[(i,j)] = Bedrock()
'''

# game loop
running = True
while running:

    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False #quit game if user leaves

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:     camInc[1] = 8/prevframerate
            elif event.key == pygame.K_a:   camInc[0] = -8/prevframerate
            elif event.key == pygame.K_s:   camInc[1] = -8/prevframerate
            elif event.key == pygame.K_d:   camInc[0] = 8/prevframerate

        elif event.type == pygame.KEYUP: camInc = [0, 0]

        elif event.type == pygame.VIDEORESIZE:
            pygame.display.Info()
            displaySize = [screen.get_width(), screen.get_height()]

    screen.fill((255, 255, 255))
    renderChunk(chunks, cam, displaySize)

    # framerate calculation
    pygame.display.update()
    frametime = clock.tick(framerate) + 1
    prevframerate = 1000 / frametime

    # Camera movement handling
    speed = 16
    cam[0] += speed * camInc[0]
    cam[1] += speed * camInc[1]

    currchunk = cam[0]//(8*16)
    relx = cam[0] - (16*8*currchunk)

    print(int(cam[0]), int(cam[1]), int(currchunk), int(relx), sep="\t")

    #print('-'*(int(256*noise.pnoise1(x, scale=10, repeat=2**30, octaves=100))+32) + "*")
    #print(128*noise.pnoise1(x, repeat=2**30, octaves=100)+128)
    #print('-'*random.randint(1,17))
