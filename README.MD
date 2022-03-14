# PyCheckers
- [PyCheckers](#pycheckers)
  - [What is this?](#what-is-this)
  - [Project outline](#project-outline)
  - [Project roadmap](#project-roadmap)
      - [Minimum](#minimum)
      - [Extras](#extras)

## What is this?
This is a simple implementation of a checkers game using Python and Pygame.

## Project outline

| File        | Purpose                                                                                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Constant.py | Stores functions used mainly when building the Graphical Environment                                                                                       |
| Board.py    | General controlles, the brain which controls the pieces, draws itself and controls current turn                                                            |
| Piece.py    | Piece class, has functions regarding drawing itself and knows ownsership and current state.                                                                |
| Main.py     | Placeholder file which calls the main pygame functions and starting the game, also controls the state machine responsible for displaying different screens |


## Project roadmap

#### Minimum
 - [x] Board
 - [x] Piece behaviour
 - [x] Turn controller
 - [x] Game checker
 - [ ] Debug mode
 - [ ] Unity Testing
#### Extras
 - [ ] Screen controller
 - [ ] 1P mode
 - [ ] Alternative gamemodes