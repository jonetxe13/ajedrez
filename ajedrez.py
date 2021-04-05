import pygame
import numpy as np


SCREEN = pygame.display.set_mode((600, 600))
SCREENSIZE = 500
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
CELLNUMBER = 8
CELLSIZE = 60

gameState = True

pygame.init()

#piezas
alfil = pygame.image.load("alfil1.png")
alfilB = pygame.transform.scale(alfil, (CELLSIZE, CELLSIZE))
caballo = pygame.image.load("caballo.png")
caballoB = pygame.transform.scale(caballo, (CELLSIZE, CELLSIZE))

def piezas():
    # Indicamos la posicion sobre la ventana
    SCREEN.blit(caballoB, (CELLSIZE*2, CELLSIZE*8))
    SCREEN.blit(caballoB, (CELLSIZE*7, CELLSIZE*8))
    SCREEN.blit(alfilB, (CELLSIZE*3, CELLSIZE*8))
    SCREEN.blit(alfilB, (CELLSIZE*6, CELLSIZE*8))
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
