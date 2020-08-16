import pygame
pygame.init()
print("Hello world")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Terraria")
pygame.display.set_icon(pygame.image.load("Assets/imgtester.png"))

img = pygame.image.load("Assets/imgtester.png")

def renderTester():
    xCoor = 100
    yCoor = 100
    screen.blit(img, (xCoor, yCoor), (16, 0, 16, 16))

running = True
while running:
    screen.fill((255, 255, 255))
    renderTester()
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN): running = False
    pygame.display.update()
