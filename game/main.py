import pygame
import constant
import board
from pygame.locals import *
pygame.init()

# Creates a new screen on which we'll draw the board
screen = pygame.display.set_mode((constant.BOARD_WIDTH, constant.BOARD_HEIGTH))
newBoard = board.Board()

gameOn = True
while gameOn:
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
             
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False
    newBoard.drawAll(screen)
    pygame.display.update()