import pygame, numpy, sys, noise, random
from pygame.locals import *
from Tile import *
from Chunk import *

# Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()

# Create and display window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption("Terraria")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

# Set display variables
cameraX = cameraY = 0
xInc = yInc = 0
lastframerate = framerate = 0

# Create a sample chunk
myChunk = Chunk()

def renderChunk(chunk, xOffset, yOffset):
    for i in range(0, 256, 1):
        if (i >= 54 + yOffset/16): break
        for j in range(0, 8, 1):
            if(chunk[(i,j)] != None): screen.blit(chunk[(i,j)].texture, (j*16 + xOffset, i*16 - yOffset), chunk[(i,j)].area)

#def renderTester():
    #grassBlock = Grass()
    #stoneBlock = Stone()
    #bedBlock = Bedrock()
    #screen.blits( (grassBlock.getblit((100, 100)),stoneBlock.getblit((116, 116)),bedBlock.getblit((132, 132))) )
    #screen.blit(grassBlock.texture, (100, 100), grassBlock.area)

# randomely populate chunk with tiles
for i in range(0, 256, 1):
    for j in range(0, 8, 1):
        blockType = random.randint(0, 4)
        if(blockType == 0): myChunk[(i,j)] = Grass()
        elif(blockType == 1): myChunk[(i,j)] = Stone()
        elif(blockType == 3): myChunk[(i,j)] = Bedrock()

# game loop
running = True
while running:

    # event handling loop
    for event in pygame.event.get():
        #quit game if user leaves
        if event.type == pygame.QUIT: running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:     yInc = 8/prevframerate
            elif event.key == pygame.K_a:   xInc = -8/prevframerate
            elif event.key == pygame.K_s:   yInc = -8/prevframerate
            elif event.key == pygame.K_d:   xInc = 8/prevframerate

        elif event.type == pygame.KEYUP: xInc = yInc = 0

    screen.fill((255, 255, 255))
    renderChunk(myChunk, cameraX, cameraY)
    #renderTester()

    # framerate calculation
    pygame.display.update()
    frametime = clock.tick(framerate) + 1
    prevframerate = 1000 / frametime

    # Camera movement handling
    speed = 6
    cameraX, cameraY = cameraX + speed * xInc, cameraY + speed * yInc
    print(int(cameraX), int(cameraY), prevframerate)

    #print('-'*(int(256*noise.pnoise1(x, scale=10, repeat=2**30, octaves=100))+32) + "*")
    #print(128*noise.pnoise1(x, repeat=2**30, octaves=100)+128)
    #print('-'*random.randint(1,17))
