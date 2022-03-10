import pygame
import constant
import piece


class Board:                            # Define the game board as an array of squares
    def __init__(self):
        self.board = []                 # Internal array designed to manage the squares
        self.defineBoard()              # Define the board
    def defineBoard(self):
        for i in range(constant.BOARD_SIZE):
            self.board.append([])
            for j in range(constant.BOARD_SIZE):
                if j % 2 == ((i + 1) % 2):
                    if i < 3:           # Top three rows where there are pieces
                        self.board[i].append(piece.Piece((i, j), constant.P2_CENTER))
                    elif i > 4:         # Bottom three rows where there are pices
                        self.board[i].append(piece.Piece((i, j), constant.P1_CENTER))
                    else:               # Adds blank pieces for control
                        self.board[i].append(0)
                else:                   # If squares where left unnatended add blank piece for debugging later
                    self.board[i].append(0)
    def drawBoard(self, screen):
        screen.fill(constant.PRIMARY_COLOR)
        for i in range(constant.BOARD_SIZE):
            for j in range(i % 2, constant.BOARD_SIZE, 2):  # Draws the light squares on a dark background, beginning with the first square in even rows and in the second square in odd rows
                pygame.draw.rect(screen, constant.SECONDARY_COLOR, (i*constant.SQUARE_SIDE, j*constant.SQUARE_SIDE, constant.SQUARE_SIDE, constant.SQUARE_SIDE))
    
    def drawAll(self, screen):
        self.drawBoard(screen)
        for i in range(constant.BOARD_SIZE):
            for j in range(constant.BOARD_SIZE):
                piece = self.board[i][j]
                if piece != 0:
                    piece.draw(screen)
                    