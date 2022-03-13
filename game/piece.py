from turtle import onclick
import pygame
import constant
from pygame.locals import *

class Piece:
    def __init__(self, square, color):
        self.row = square[0]
        self.col = square[1]
        self.selected = False
        self.color = color
        if self.color == constant.P1_CENTER:
            self.colorBorder = constant.P1_BORDER
            self.colorHighlight = constant.P1_HIGHLIGHT
        else:
            self.colorBorder = constant.P2_BORDER
            self.colorHighlight = constant.P2_HIGHLIGHT

        self.center_x = 0
        self.center_y = 0

        self.crowned = False

        # Defines direction of piece movement

        self.FindCenter()

    def FindCenter(self):
        self.center_x = self.col*constant.SQUARE_SIDE + constant.SQUARE_SIDE/2
        self.center_y = self.row*constant.SQUARE_SIDE + constant.SQUARE_SIDE/2

    def CrownPiece(self):
        self.crowned = True

    def DrawPiece(self, screen):
        if self.selected:
            pygame.draw.circle(screen, self.colorHighlight, (self.center_x, self.center_y), constant.PIECE_RADIUS+2)
            pygame.draw.circle(screen, self.colorBorder, (self.center_x, self.center_y), constant.PIECE_RADIUS)
            pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), constant.PIECE_RADIUS-5)
        else:
            pygame.draw.circle(screen, self.colorBorder, (self.center_x, self.center_y), constant.PIECE_RADIUS)
            pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), constant.PIECE_RADIUS-5)
        if self.crowned:
            pygame.draw.circle(screen, self.colorBorder, (self.center_x, self.center_y), constant.PIECE_RADIUS/2)
        

    def select(self):
        self.selected = True
    def movePiece(self, newRow, newCol):
        self.row = newRow
        self.col = newCol
        self.FindCenter()