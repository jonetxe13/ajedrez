import pygame
import numpy as np


SCREEN = pygame.display.set_mode((400, 400))
SCREENSIZE = 500
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
CELLNUMBER = 8
CELLSIZE = 35

gameState = True

pygame.init()

#piezas
alfil0 = pygame.image.load("alfil1.png")
alfil = pygame.transform.scale(alfil0, (150, 75))
caballo0 = pygame.image.load("caballo.png")
caballo = pygame.transform.scale(caballo0, (150, 75))

def piezas():
    # Indicamos la posicion de las "Surface" sobre la ventana
    SCREEN.blit(caballo, (40, 280))
    SCREEN.blit(caballo, (212, 280))
    SCREEN.blit(alfil, (102, 280))
    SCREEN.blit(alfil, (207, 280))
    # se muestran lo cambios en pantalla
    pygame.display.flip()


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
    board()
    piezas()
    pygame.display.update()
