import pygame
# Contains main constants used in the game

# Dimensional constants:

BOARD_WIDTH = 600  # Width of the game board in pixels
BOARD_HEIGTH = BOARD_WIDTH  # Height of the game board in pixels

BOARD_SIZE = 8  # Number of squares in the side of the board
SQUARE_SIDE = BOARD_WIDTH / BOARD_SIZE  # square side in pixels
SQUARE_CENTER = SQUARE_SIDE / 2  # square center in pixels
PIECE_RADIUS = SQUARE_SIDE / 3  # radius of the piece in pixels
PIECE_AMOUNT = 3 * BOARD_SIZE / 2  # amount of pieces on the board

# Color constants
PRIMARY_COLOR = (65, 0, 118)
SECONDARY_COLOR = (232,230,227)
VALIDMOVE_COLOR = (0, 0, 0)
# P1
P1_CENTER = (84, 27, 130)
P1_BORDER = (40, 11, 64)
P1_HIGHLIGHT = (232, 205, 2)
# P2
P2_CENTER = (214, 213, 210)
P2_BORDER = (152, 149, 149)
P2_HIGHLIGHT = (153, 5, 5)

#Crowns
P1_CROWN = pygame.transform.scale(pygame.image.load('game\sources\QultureIconPurple.png'), (PIECE_RADIUS*2, PIECE_RADIUS*2))
P2_CROWN = pygame.transform.scale(pygame.image.load('game\sources\QultureIconWhite.png'), (PIECE_RADIUS*2, PIECE_RADIUS*2))

# Sounds
pygame.mixer.init()
MOVE_SOUND = pygame.mixer.Sound('game\sources\PieceSound.wav')
CAPTURE_SOUND = pygame.mixer.Sound('game\sources\Capture.wav')