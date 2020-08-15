import pygame

print("Hello world")

screen = pygame.display.set_mode((800, 600))

running=True
while running:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            running=False
