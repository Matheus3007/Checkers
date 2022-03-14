import pygame
import constant as ct
import board

class Game:
    def __init__(self, scr,debug=False): # Allows the game to be booted in debug mode, which has a different board pattern
        self.selected = None
        self.board = board.Board(debug)
        self.turn = ct.P1_CENTER
        self.valid_moves = {}
        self.screen = scr

    # Updates the board so that the game is not dependent on clock ticks or a loop that runs every frame.
    def Update(self):
        self.board.DrawAll(self.screen)
        self.DrawMoves(self.valid_moves)
        pygame.display.update()


    # Resets the game, called upon completion or when the player presses the 'r' key
    def ResetGame(self):
        self.selcted = None
        self.board = board.Board()
        self.turn = ct.P1_CENTER
        self.valid_moves = {}


    # Selects a piece, if the piece is not already selected, and if the piece belongs to the current player    
    def Select(self, row, col):
        # If something's selected already, try and move selection towards the new square
        if self.selected:
            result = self._Move(row,col)
            if not result:
                self.selected = None
                self.Select(row,col)
        # If nothing's selected, try and select the square
        
        piece = self.board.GetPiece(row,col)
        if piece != 0 and piece.color == self.turn:
            
            self.selected = piece
            piece.selected = True
            self.valid_moves = self.board.GetMoves(piece)
            print(self.valid_moves)
            return True
        self.valid_moves=[] # If the square is empty, or if the piece is not the current player's, clear the valid moves
        return False
        

    def _Move(self, row, col):
        piece = self.board.GetPiece(row,col)
        # If the square is empty, move the piece towards the square
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.MovePieceOnBoard(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.RemovePiece(skipped)
            self.ChangeTurn()
        else:
            return False
        return True

    def DrawMoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, (0,0,0), ((col * ct.SQUARE_SIDE) + int(ct.SQUARE_SIDE/2), (row * ct.SQUARE_SIDE) + int(ct.SQUARE_SIDE/2)), ct.PIECE_RADIUS/5)

    def ChangeTurn(self):
        self.valid_moves = []
        if self.turn == ct.P1_CENTER:
            self.turn = ct.P2_CENTER
        else:
            self.turn = ct.P1_CENTER
        if self.board.finished:
            self.valid_moves = []
            self.ResetGame()
    
    def GetTurn(self):
        return self.turn