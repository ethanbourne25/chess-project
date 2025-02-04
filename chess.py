import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Chess')

#Squares
squareSize = 75
l = pygame.Surface((75, 75))
l.fill('burlywood1')

d = pygame.Surface((75, 75))
d.fill('chocolate4')

#White Pieces
whitePieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn",
                "rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
whiteStartingSquares = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
                        [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
whiteCaptured = []

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

#Black Pieces
blackPieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn",
                "rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
blackStartingSquares = [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7],
                        [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]
blackCaptured = []

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

turnNumber = 0

blackPieceList = blackPieces
blackPieceLocations = blackStartingSquares

whitePieceList = whitePieces
whitePieceLocations = whiteStartingSquares

def setupBoard():
    # Draw the board
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
    placePieces()

def placePieces():
    for i in range(len(blackPieceList)):
        print("Black piece with id = ", blackPieceList[i], "with location = ", blackPieceLocations[i])
        if blackPieceList[i] == " pawn":
            print("Y")
        elif blackPieceList[i] == "pawn":
            screen.blit(blackPawn, (blackPieceLocations[i][1] * squareSize, (7 - blackPieceLocations[i][0]) * squareSize))
        elif blackPieceList[i] == "bishop":
            screen.blit(blackBishop, (blackPieceLocations[i][1] * squareSize, (7 - blackPieceLocations[i][0]) * squareSize))
        elif blackPieceList[i] == "rook":
            screen.blit(blackRook, (blackPieceLocations[i][1] * squareSize, (7 - blackPieceLocations[i][0]) * squareSize))
        elif blackPieceList[i] == "knight":
            screen.blit(blackKnight, (blackPieceLocations[i][1] * squareSize, (7 - blackPieceLocations[i][0]) * squareSize))
        elif blackPieceList[i] == "queen":
            screen.blit(blackQueen, (blackPieceLocations[i][1] * squareSize, (7 - blackPieceLocations[i][0]) * squareSize))
        elif blackPieceList[i] == "king":
            screen.blit(blackKing, (blackPieceLocations[i][1] * squareSize, (7 - blackPieceLocations[i][0]) * squareSize))
        else:
            raise TypeError("Invalid piece")
    for i in range(len(whitePieceList)):
        if whitePieceList[i] == "pawn":
            screen.blit(whitePawn, (whitePieceLocations[i][1] * squareSize, (7 - whitePieceLocations[i][0]) * squareSize))
        elif whitePieceList[i] == "bishop":
            screen.blit(whiteBishop, (whitePieceLocations[i][1] * squareSize, (7 - whitePieceLocations[i][0]) * squareSize))
        elif whitePieceList[i] == "rook":
            screen.blit(whiteRook, (whitePieceLocations[i][1] * squareSize, (7 - whitePieceLocations[i][0]) * squareSize))
        elif whitePieceList[i] == "knight":
            screen.blit(whiteKnight, (whitePieceLocations[i][1] * squareSize, (7 - whitePieceLocations[i][0]) * squareSize))
        elif whitePieceList[i] == "queen":
            screen.blit(whiteQueen, (whitePieceLocations[i][1] * squareSize, (7 - whitePieceLocations[i][0]) * squareSize))
        elif whitePieceList[i] == "king":
            screen.blit(whiteKing, (whitePieceLocations[i][1] * squareSize, (7 - whitePieceLocations[i][0]) * squareSize))
        else:
            raise TypeError("Invalid piece")
        
    

run = True
whiteTurn = True
gameRun = True
setupBoard()
while run:
    # Running logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    # Start the game
    


    
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
exit()