import pygame
import numpy as np
import tablero

SCREEN = pygame.display.set_mode((400, 400))
SCREENSIZE = 500
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
CELLNUMBER = 8
CELLSIZE = 35

gameState = True

pygame.init()

def board():
    for x in range(1, CELLNUMBER+1, 2):
        for y in range(1, CELLNUMBER+1, 2):
            pygame.draw.rect(SCREEN, BLACK, [x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE])
            
    for x in range(2, CELLNUMBER+1, 2):
        for y in range(2, CELLNUMBER+1, 2):
            pygame.draw.rect(SCREEN, BLACK, [x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE])

    for x in range(1, CELLNUMBER+2):
        for y in range(1, CELLNUMBER+2):
            pygame.draw.line(SCREEN, BLACK, (x*CELLSIZE, CELLSIZE), (x*CELLSIZE, CELLSIZE*(CELLNUMBER+1)))
            pygame.draw.line(SCREEN, BLACK, (CELLSIZE, y*CELLSIZE), (CELLSIZE*(CELLNUMBER+1), y*CELLSIZE))


while gameState:
    SCREEN
    SCREEN.fill(WHITE)
    tablero.board()
    pygame.display.update()

for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        gameState = False