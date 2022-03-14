import board
import constant
import pygame
from EventControllers import *
from pygame.locals import *

import game as g

pygame.init()

# Creates a new screen on which we'll draw the board
screen = pygame.display.set_mode((constant.BOARD_WIDTH, constant.BOARD_HEIGTH))
game = g.Game(screen,True)
gameOn = True
while gameOn:
    game.Update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = GetPosFromMouse(pos)
            game.Select(row, col)

        # Check for KEYDOWN event
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == KEYDOWN:
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE or event.key == K_ESCAPE:
                gameOn = False
            elif event.key == K_r:
                game.ResetGame()
