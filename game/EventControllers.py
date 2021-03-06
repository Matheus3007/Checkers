import constant as ct


def GetPosFromMouse(pos):
    x, y = pos
    row = int(y // ct.SQUARE_SIDE)
    col = int(x // ct.SQUARE_SIDE)
    print("Row: " + str(row) + " Column: " + str(col))
    return row, col


def MovePieceWithMouse(pos, board):
    piece = board.GetPiece(pos[0], pos[1])

    if piece != 0:
        board.MovePieceOnBoard(piece, 3, 4)
