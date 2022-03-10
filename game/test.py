import pygame
from pygame.locals import *

 
# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
         
        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((25, 25))
         
        # Define the color of the surface using RGB color coding.
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()
        self.PosX = 40
        self.PosY = 40
 
# initialize pygame
pygame.init()
black=(0,0,0)
# Define the dimensions of screen object
screen = pygame.display.set_mode((800, 600))
 
# instantiate all square objects
square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()
 
# Variable to keep our game loop running
gameOn = True
 
# Our game loop
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
             
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False
            elif event.key== K_UP:
                square1.PosY -= 10    
            elif event.key== K_DOWN:
                square1.PosY += 10    
            elif event.key== K_LEFT:
                square1.PosX -= 10    
            elif event.key== K_RIGHT:
                square1.PosX += 10     
        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False
 
    # Define where the squares will appear on the screen
    # Use blit to draw them on the screen surface
    screen.fill(black)
    screen.blit(square1.surf, (square1.PosX, square1.PosY))
    screen.blit(square2.surf, (40, 530))
    screen.blit(square3.surf, (730, 40))
    screen.blit(square4.surf, (730, 530))
 
    # Update the display using flip
    pygame.display.flip()