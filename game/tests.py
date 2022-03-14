import unittest

from board import *
from constant import *
from piece import *

from game import *


# Mainly checks game control flow
class TestBoard(unittest.TestCase):
    def test_DefineBoard(self):
        test_board = Board()
        self.assertIsNotNone(test_board)  ## Checks if the board was created

    def test_PiecePlacement(self):
        test_board = Board()
        self.assertEquals(
            test_board.GetPiece(0, 0), 0
        )  ## Checks if the first square is empty
        self.assertIsNot(
            test_board.GetPiece(0, 1), 0
        )  ## Checks if the first P2 piece is placed
        self.assertIsNot(
            test_board.GetPiece(7, 0), 0
        )  ## Checks if the first P1 piece is placed

    def test_GetPiece(self):  # Checks if pieces were created properly
        test_board = Board()
        test_piece_p1 = Piece([7, 0], P1_CENTER)
        test_piece_p2 = Piece([0, 1], P2_CENTER)

        # Verify colors
        self.assertEquals(test_board.GetPiece(7, 0).color, test_piece_p1.color)
        self.assertEquals(test_board.GetPiece(0, 1).color, test_piece_p2.color)

        # Verify positions
        self.assertEquals(test_board.GetPiece(7, 0).row, test_piece_p1.row)
        self.assertEquals(test_board.GetPiece(7, 0).col, test_piece_p1.col)
        self.assertEquals(test_board.GetPiece(0, 1).row, test_piece_p2.row)
        self.assertEquals(test_board.GetPiece(0, 1).col, test_piece_p2.col)

        # Verify if pieces can be moved in the board

    def test_MovePieceOnBoard(self):
        test_board = Board()
        test_board.MovePieceOnBoard(test_board.GetPiece(0, 1), 3, 4)
        self.assertEquals(test_board.GetPiece(3, 4).color, P2_CENTER)
        self.assertEquals(test_board.GetPiece(3, 4).row, 3)
        self.assertEquals(test_board.GetPiece(3, 4).col, 4)
        self.assertEquals(test_board.GetPiece(0, 1), 0)

        # Verify if pieces can be removed from the board

    def test_RemovePiece(self):
        test_board = Board()
        pieces = []
        pieces.append(test_board.GetPiece(0, 1))
        test_board.RemovePiece(pieces)
        self.assertEquals(test_board.GetPiece(0, 1), 0)

        # Checks if the game calculates a simple move correctly

    def test_GetMovesSimple(self):
        test_board = Board()
        moves = test_board.GetMoves(test_board.GetPiece(5, 2))
        self.assertEquals(moves, {(4, 1): [], (4, 3): []})

        # Checks if the game calculates a double jump correctly

    def test_GetMovesDouble(self):
        test_board = Board(True)
        moves = test_board.GetMoves(test_board.GetPiece(5, 2))
        movelist = []
        for key in moves.keys():
            movelist.append(key)
        self.assertEquals(movelist, [(4, 1), (3, 4), (1, 6)])

        # Mainly checks game logic


class TestGame(unittest.TestCase):
    def test_Game(self):
        screen = pygame.display.set_mode((constant.BOARD_WIDTH, constant.BOARD_HEIGTH))
        test_game = Game(screen)
        self.assertIsNotNone(test_game)

    def test_Turn(self):
        screen = pygame.display.set_mode((constant.BOARD_WIDTH, constant.BOARD_HEIGTH))
        test_game = Game(screen)
        self.assertEquals(test_game.GetTurn(), P1_CENTER)
        test_game.ChangeTurn()
        self.assertEquals(test_game.GetTurn(), P2_CENTER)

    def test_Finish(self):
        test_board = Board(True)
        pieces = [test_board.GetPiece(4, 3), test_board.GetPiece(2, 5)]
        test_board.RemovePiece(pieces)
        self.assertEquals(test_board.finished, True)

        # After resetting a debug game, the board should be a normal one, thus we check if the first piece for P1 is placed.

    def test_Restart(self):
        screen = pygame.display.set_mode((constant.BOARD_WIDTH, constant.BOARD_HEIGTH))
        test_game = Game(screen)
        test_game.ResetGame()
        self.assertNotEqual(test_game.board.GetPiece(7, 0), 0)
