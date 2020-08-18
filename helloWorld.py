import pygame, numpy, sys, noise, random
from pygame.locals import *
from Tile import *

#Initialize pygame and start clock
pygame.init()
clock = pygame.time.Clock()

#Create and display window
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Terraria")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

#Set display variables
cameraX = cameraY = 0
xInc = yInc = 0
framerate = 0

grassBlock = Grass()
stoneBlock = Stone()
bedBlock = Bedrock()

def renderTester():
    screen.blits( (grassBlock.getBlit((100, 100)),stoneBlock.getBlit((116, 116)),bedBlock.getBlit((132, 132))) )
    #screen.blit(grassBlock.texture, (100, 100), grassBlock.area)

running = True
while running:

    #print('-'*(int(256*noise.pnoise1(x, scale=10, repeat=2**30, octaves=100))+32) + "*")
    #print(128*noise.pnoise1(x, repeat=2**30, octaves=100)+128)
    #print('-'*random.randint(1,17))

    screen.fill((255, 255, 255))
    renderTester()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:     yInc = 8/currFramerate
            elif event.key == pygame.K_a:   xInc = -8/currFramerate
            elif event.key == pygame.K_s:   yInc = -8/currFramerate
            elif event.key == pygame.K_d:   xInc = 8/currFramerate

        elif event.type == pygame.KEYUP: xInc = yInc = 0

    pygame.display.update()
    frameTime = clock.tick(framerate)
    currFramerate = 1000/frameTime

    cameraX, cameraY = cameraX+xInc, cameraY+yInc
    print(int(cameraX), int(cameraY), currFramerate)
    #print("FPS:", 1000/frameTime)