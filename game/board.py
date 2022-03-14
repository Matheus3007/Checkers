import pygame
import constant
import piece
import pyautogui

class Board:                                    # Define the game board as an array of squares
    def __init__(self, debug=False):
        self.debug=debug
        self.board = []                         # Internal array designed to manage the squares
        if debug:
            self.DefineTestBoard()              # Define the board for debugging purposes
        else:
            self.DefineBoard()                  # Define the board normally

        self.p1_pieces = 0                      # Initialize the amount of pieces for each player
        self.p2_pieces = 0

        for row in range(constant.BOARD_SIZE):         # Counts the amount of pieces for each player
            for col in range(constant.BOARD_SIZE):
                piece = self.GetPiece(row, col)
                if piece != 0:
                    if piece.color==constant.P1_CENTER:
                        self.p1_pieces += 1
                    elif piece.color==constant.P2_CENTER:
                        self.p2_pieces += 1

        self.finished = False                   # Initialize the game as not finished
        print("P1 pieces: " +  str(self.p1_pieces))
        print("P2 pieces: " +  str(self.p1_pieces))
    def DefineBoard(self):
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

                
    def DefineTestBoard(self): # Creates a test board for debugging purposes
        for i in range(constant.BOARD_SIZE):
            self.board.append([])
            for j in range(constant.BOARD_SIZE):
                if j % 2 == ((i + 1) % 2):
                    if (i==4 and j == 3) or (i == 2 and j == 5):           # Top three rows where there are pieces
                        self.board[i].append(piece.Piece((i, j), constant.P2_CENTER))
                    elif i == 5 and j == 2:         # Bottom three rows where there are pices
                        self.board[i].append(piece.Piece((i, j), constant.P1_CENTER))
                    else:               # Adds blank pieces for control
                        self.board[i].append(0)
                else:                   # If squares where left unnatended add blank piece for debugging later
                    self.board[i].append(0)
        pass

    # Function related to drawing the squares on the screen
    def DrawBoard(self, screen):
        screen.fill(constant.PRIMARY_COLOR)
        for i in range(constant.BOARD_SIZE):
            for j in range(i % 2, constant.BOARD_SIZE, 2):  # Draws the light squares on a dark background, beginning with the first square in even rows and in the second square in odd rows
                pygame.draw.rect(screen, constant.SECONDARY_COLOR, (i*constant.SQUARE_SIDE, j*constant.SQUARE_SIDE, constant.SQUARE_SIDE, constant.SQUARE_SIDE))
    
    # Function responsible for drawing pieces onscreen, note that this will be called on every update of the board
    def DrawAll(self, screen):
        self.DrawBoard(screen)
        for i in range(constant.BOARD_SIZE):
            for j in range(constant.BOARD_SIZE):
                piece = self.board[i][j]
                if piece != 0:
                    piece.DrawPiece(screen)

    # Function responsible for piece movement, note that it'll only move pieces on the internal array of the board, thus it'll not move pieces on the screen
    def MovePieceOnBoard(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]     # Swaps the piece with the blank in the new location
        piece.movePiece(row, col)
        if row == 0 or row== constant.BOARD_SIZE-1 and piece.crowned == False: # Crowns pieces on the last line of the board
            piece.CrownPiece()
    
    # Getter related to outputting the piece on the internal board, it can return pieces (represented with a piece class) or 0 (representing a blank square)
    def GetPiece(self, row, col):
        return self.board[row][col]


      # Gets the valid moves for an specific square on the board
    def GetMoves(self, piece):
        moves = {}
        squareLeft = piece.col - 1
        squareRight = piece.col + 1
        row = piece.row
        
        if piece.color == constant.P1_CENTER or piece.crowned:
            moves.update(self._LeftDiagonal(row-1, max(row-3, -1), -1, piece.color, squareLeft))
            moves.update(self._RightDiagonal(row-1, max(row-3, -1), -1, piece.color, squareRight))
        
        if piece.color == constant.P2_CENTER or piece.crowned:
            moves.update(self._LeftDiagonal(row+1, min(row+3, constant.BOARD_SIZE), 1, piece.color, squareLeft))
            moves.update(self._RightDiagonal(row+1, min(row+3, constant.BOARD_SIZE), 1, piece.color, squareRight))

        return moves

    def _LeftDiagonal(self, start, stop, direction, color, left, skipped=[]):
        moves = {}
        last = []
        
        for r in range(start, stop, direction):
            if left < 0:
                break
                
            current = self.board[r][left]
            if current == 0:
                if skipped and not last: # Prevents movement after skipping a piece
                    break 
                elif skipped:
                    moves[(r,left)] = last + skipped

                else:
                    moves[(r,left)] = last
                if last:
                    if direction == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, constant.BOARD_SIZE-1)
                    moves.update(self._LeftDiagonal(r+direction, row, direction, color, left-1, skipped=last))
                    moves.update(self._RightDiagonal(r+direction, row, direction, color, left+1, skipped=last))
                break
            elif current.color == color:
                break                    
            else:
                last = [current]

            left -= 1

        return moves

    def _RightDiagonal(self, start, stop, direction, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, direction):
            if right >= constant.BOARD_SIZE:
                break
                
            current = self.board[r][right]
            if current == 0:
                if skipped and not last: # Prevents movement after skipping a piece
                    break 
                elif skipped:
                    moves[(r,right)] = last + skipped

                else:
                    moves[(r,right)] = last
                if last:
                    if direction == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, constant.BOARD_SIZE-1)
                    moves.update(self._LeftDiagonal(r+direction, row, direction, color, right-1, skipped=last))
                    moves.update(self._RightDiagonal(r+direction, row, direction, color, right+1, skipped=last))
                break
            elif current.color == color:
                break                    
            else:
                last = [current]

            right += 1

        return moves


    def RemovePiece(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == constant.P1_CENTER:
                    self.p1_pieces -= 1
                    print(self.p1_pieces)
                elif piece.color == constant.P2_CENTER:
                    self.p2_pieces -= 1
                    print(self.p2_pieces)
        if self.p1_pieces == 0:
            self.finished = True
            if not self.debug:                  # If the game is not in debug mode, it will show the winner
                pyautogui.alert("Player 2 wins!")
        elif self.p2_pieces == 0:
            self.finished = True
            if not self.debug:
                pyautogui.alert("Player 1 wins!")
        
