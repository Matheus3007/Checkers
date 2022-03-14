# PyCheckers
- [PyCheckers](#pycheckers)
  - [What is this?](#what-is-this)
  - [Project outline](#project-outline)
  - [Project roadmap](#project-roadmap)
      - [Minimum](#minimum)
  - [In depth look at functions and parameters](#in-depth-look-at-functions-and-parameters)
    - [Constant.py](#constantpy)
    - [piece.py](#piecepy)
    - [board.py](#boardpy)
    - [game.py](#gamepy)

## What is this?
This is a simple implementation of a checkers game using Python and Pygame.

## Project outline

| File        | Purpose                                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Constant.py | Stores functions used mainly when building the Graphical Environment                                                                    |
| Board.py    | General controlles, the brain which controls the pieces, draws itself and controls current turn                                         |
| Piece.py    | Piece class, has functions regarding drawing itself and knows ownsership and current state.                                             |
| Game.py     | General integration files, merges draw functions with control functions, responsible for selecting pieces and displaying their movement |
| Main.py     | File which calls game related functions and creates the screen, go here if you want to activate debug mode                              |

## Project roadmap

#### Minimum
 - [x] Board
 - [x] Piece behaviour
 - [x] Turn controller
 - [x] Game checker
 - [x] Debug mode
 - [x] Unity Testing

## In depth look at functions and parameters

### Constant.py
- BOARD_WIDTH and BOARD_HEIGHT: Parameters responsible for setting screen size, once everything depends on them it's pretty safe to adjust it as you see fit
- BOARD_SIZE: Defines the amount of squares in a board, was created considering the further implementation of other gamemodes, such as *International Draughts*, which is a gamemode played on a 10x10 board.
- Color constants: Temper as you see fit, they have pretty self explanatory names, but beware that they are not self dependent, so you may make your game harder by messing with them.
- Size constants: They all depend on board size and width, so I don't recommend altering them individually, even though the names are self explanatory.

### piece.py
The piece takes two arguments when created: a tuple related to it's coordinates on the board and it's color.
- FindCenter(): Calculates the position of the center of the piece onscreen
- CrownPiece(): Crowns the piece
- DrawPiece(screen): Given a screen, draws the piece on it, considering it's internal coordinates.
- movePiece(newRow, newCol): Given a new coordinate, moves the piece there and finds it's new center

### board.py
- DefineBoard() and DefineTestBoard(): Both functions generate an internal board represented by a 2-dimensional array, although DefineTestBoard will only be called in debug mode, which can be achieved by creating a Board object with the first parameter set to True (it defaults to False).
- DrawBoard(screen): Creates a visual representation of the board itself; note that it doesn't draw the pieces yet. This function simply draws the checkered board on screen, needs a screen to be drawed on, which can be created with pygame.display.
- DrawAll(screen): Calls on DrawBoard and DrawPiece (method related to pieces) to draw both the board and the pieces on screen.
- MovePieceOnBoard(piece, row, col): Moves a determinate piece to the selected square, given it's coordinates. Also responsible for crowning pieces that reach the other side.
- GetPiece(row, col): Gets piece object placed on the board.
- GetMoves(piece): Finds the valid moves given a determinate piece. A valid move is forward given the piece isn't crowned, always diagonal and may be a jump over adversary pieces as long as they are on diagonal corners and the following square is empty.
- Left and RightDiagonal(start, stop, direction, color, left/right, skipped): Heart of the GetMoves() method, it recursevily checks for valid moves on a diagonal, first left, than right. start is the starting square, stop the square on which it'll stop checking, direction relates to the color of the piece or if they are crowned or not, left/right parameters relate to the direction represented by left or right and finally, skipped is a list containing the skipped pieces.
- RemovePiece(pieces): Removes the given list of pieces from the internal board. Note that it doesnt erase anything from the screen, but the pieces simply stop being drawed on the next screen cycle.

### game.py
Game() has an attribute that defaults to false just as Board(), so that the user doesn't need to interact with the internal method board, it works just the same, simply acting as a different point of access.
- Update(): Updates what's onscreen
- ResetGame(): Resets the game, which can happen both by the user's choice or the end of a game.
- Select(row, col): Given a square, tries to select it. If nothing's selected previously and the square has a piece belonging to the current player, it is selected and it's moves are displayed. If something's selected and the square is not a valid move, the piece gets unselected and a new one is chosen. Lastly, if a piece is selected and then a valid move's selected, the piece is moved.
- Move(row, col): Given a square, move a piece towards that square, as long as it's empty
- DrawMoves(moves): Given a list of squares that represent the valid moves for a piece, signal them to the user onscreen.
- ChangeTurn(): Turn manager for the game, P1 starts playing. The bottom player is P1.
