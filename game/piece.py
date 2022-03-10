import pygame
import constant
from pygame.locals import *

class Piece:
    def __init__(self, square, color):
        self.row = square[0]
        self.col = square[1]

        self.color = color
        if self.color == constant.P1_CENTER:
            self.colorBorder = constant.P1_BORDER
        else:
            self.colorBorder = constant.P2_BORDER

        self.center_x = 0
        self.center_y = 0

        self.crowned = False

        # Defines direction of piece movement
        if color == constant.P1_CENTER:
            self.dir = -1
        else:
            self.dir =  1
        self.find_center()

    def find_center(self):
        self.center_x = self.col*constant.SQUARE_SIDE + constant.SQUARE_SIDE/2
        self.center_y = self.row*constant.SQUARE_SIDE + constant.SQUARE_SIDE/2

    def crown_piece(self):
        self.crowned = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.colorBorder, (self.center_x, self.center_y), constant.PIECE_RADIUS)
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), constant.PIECE_RADIUS-5)
        if self.crowned:
            pygame.draw.circle(screen, self.colorBorder, (self.center_x, self.center_y), constant.PIECE_RADIUS/2)