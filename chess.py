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
                "rook", "bishop", "knight", "queen", "king", "knight", "bishop", "rook"]
whiteStartingSquares = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
whiteCaptured = []

whitePawn = pygame.image.load('./pieces/pawn_white.png')
#whitePawn = pygame.image.scale(whitePawn, (75, 75))

whiteRook = pygame.image.load('./pieces/rook_white.png')
#whiteRook = pygame.image.scale(whiteRook, (75, 75))

whiteBishop = pygame.image.load('./pieces/bishop_white.png')
#whiteBishop = pygame.image.scale(whiteBishop, (75, 75))

whiteKnight = pygame.image.load('./pieces/knight_white.png')
#whiteKnight = pygame.image.scale(whiteKnight, (75, 75))

whiteQueen = pygame.image.load('./pieces/queen_white.png')
#whiteQueen = pygame.image.scale(whiteQueen, (75, 75))

whiteKing = pygame.image.load('./pieces/king_white.png')
#whiteKing = pygame.image.scale(whiteKing, (75, 75))

#Black Pieces
blackPieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn",
                "rook", "bishop", "knight", "queen", "king", "knight", "bishop", "rook"]
blackStartingSquares = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                        (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
blackCaptured = []

blackPawn = pygame.image.load('pieces/pawn_black.png')
#blackPawn = pygame.image.scale(blackPawn, (75, 75))

blackRook = pygame.image.load('pieces/rook_black.png')
#blackRook = pygame.transform.scale(blackRook, (75, 75))

blackBishop = pygame.image.load('pieces/bishop_black.png')
blackBishop = pygame.transform.scale(blackBishop, (75, 75))

blackKnight = pygame.image.load('pieces/knight_black.png')
#blackKnight = pygame.image.scale(blackKnight, (75, 75))

blackQueen = pygame.image.load('pieces/queen_black.png')
#blackQueen = pygame.transform.scale(blackQueen, (75, 75))

blackKing = pygame.image.load('pieces/king_black.png')
#blackKing = pygame.transform.scale(blackKing, (75, 75))

turnNumber = 0

def placePieces():
    for i in range(2):
        j = 1
        
    

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
    
    placePieces()
    
    
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
exit()