import pygame
from sys import exit

# Setup screen
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Chess')

#Setup Squares
squareSize = 75
l = pygame.Surface((75, 75))
l.fill('burlywood1')

d = pygame.Surface((75, 75))
d.fill('chocolate4')

# Setup images for every piece
whitePawn = pygame.image.load('./pieces/pawn_white.png').convert_alpha()
whitePawn = pygame.transform.scale(whitePawn, (75, 75))

whiteRook = pygame.image.load('./pieces/rook_white.png').convert_alpha()
whiteRook = pygame.transform.scale(whiteRook, (75, 75))

whiteBishop = pygame.image.load('./pieces/bishop_white.png').convert_alpha()
whiteBishop = pygame.transform.scale(whiteBishop, (75, 75))

whiteKnight = pygame.image.load('./pieces/knight_white.png').convert_alpha()
whiteKnight = pygame.transform.scale(whiteKnight, (75, 75))

whiteQueen = pygame.image.load('./pieces/queen_white.png').convert_alpha()
whiteQueen = pygame.transform.scale(whiteQueen, (75, 75))

whiteKing = pygame.image.load('./pieces/king_white.png').convert_alpha()
whiteKing = pygame.transform.scale(whiteKing, (75, 75))

blackPawn = pygame.image.load('pieces/pawn_black.png').convert_alpha()
blackPawn = pygame.transform.scale(blackPawn, (75, 75))

blackRook = pygame.image.load('pieces/rook_black.png').convert_alpha()
blackRook = pygame.transform.scale(blackRook, (75, 75))

blackBishop = pygame.image.load('pieces/bishop_black.png').convert_alpha()
blackBishop = pygame.transform.scale(blackBishop, (75, 75))

blackKnight = pygame.image.load('pieces/knight_black.png').convert_alpha()
blackKnight = pygame.transform.scale(blackKnight, (75, 75))

blackQueen = pygame.image.load('pieces/queen_black.png').convert_alpha()
blackQueen = pygame.transform.scale(blackQueen, (75, 75))

blackKing = pygame.image.load('pieces/king_black.png').convert_alpha()
blackKing = pygame.transform.scale(blackKing, (75, 75))

#setup initial board with default starting positon
startingBoard = []
startingBoard.append("r")
startingBoard.append("n")
startingBoard.append("b")
startingBoard.append("q")
startingBoard.append("k")
startingBoard.append("b")
startingBoard.append("n")
startingBoard.append("r")
for i in range(8):
    startingBoard.append("p")
for i in range(32):
    startingBoard.append(None)
for i in range(8):
    startingBoard.append("P")
startingBoard.append("R")
startingBoard.append("N")
startingBoard.append("B")
startingBoard.append("Q")
startingBoard.append("K")
startingBoard.append("B")
startingBoard.append("N")
startingBoard.append("R")

# Draw the board and place pieces in initial position
def setupBoard():
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0: 
                    screen.blit(l, (i * 75, j * 75))
                else:
                    screen.blit(d, (i * 75, j * 75))
            else:
                if j % 2 == 0: 
                    screen.blit(d, (i * 75, j * 75))
                else:
                    screen.blit(l, (i * 75, j * 75))
    # Place the pieces
    placePieces(startingBoard)

# Place the pieces for any position using list representation of the position, b
def placePieces(b):
    x = 0
    y = 7
    for i in range(len(b)):
        # Find and draw piece
        #print("For i = ", i, ", b[i] = ", b[i], ", x = ", x, ", y = ", y)
        if b[i] == "p":
            screen.blit(blackPawn, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "P":
            screen.blit(whitePawn, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "n":
            screen.blit(blackKnight, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "N":
            screen.blit(whiteKnight, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "b":
            screen.blit(blackBishop, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "B":
            screen.blit(whiteBishop, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "r":
            screen.blit(blackRook, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "R":
            screen.blit(whiteRook, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "q":
            screen.blit(blackQueen, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "Q":
            screen.blit(whiteQueen, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "k":
            screen.blit(blackKing, (x * squareSize, (7 - y) * squareSize))
        elif b[i] == "K":
            screen.blit(whiteKing, (x * squareSize, (7 - y) * squareSize))
        # Update coordinates
        if x < 7:
            x += 1
        else:
            x = 0
            y += -1

        
    
# Set up variables for game
board = startingBoard
run = True
whiteTurn = True
turnNumber = 0
gameRun = True
setupBoard()

#Main loop for running game
while run:
    # Running logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clickedPiece = [i for i in board if i.rect.collidepoint(pos)]
            print(clickedPiece)

    # Start the game
    


    
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
exit()