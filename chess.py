import pygame
from sys import exit
from pieces import getLegalMoves, getColor

# Sizes
squareSize = 75
borderSize = squareSize // 12

# Setup screen
pygame.init()
screen = pygame.display.set_mode((squareSize * 12, squareSize * 8))
pygame.display.set_caption('Chess')

# Setup Squares
l = pygame.Surface((squareSize, squareSize))
l.fill('burlywood1')

d = pygame.Surface((squareSize, squareSize))
d.fill('chocolate4')

# Setup border, need a row and a column

border1 = pygame.Surface((squareSize, borderSize))
border1.fill('darkgoldenrod1')
border2 = pygame.Surface((borderSize, squareSize))
border2.fill('darkgoldenrod1')

# Setup turn display
white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont('timesnewroman',  30)
# create a text surface object,
# on which text is drawn on it.
textWhite = font.render('White Turn', True, white, black)
boxWhite = pygame.Surface((squareSize * 4, squareSize * 4))
boxWhite.fill('black')

textBlack = font.render('Black Turn', True, black, white)
boxBlack = pygame.Surface((squareSize * 4, squareSize * 4))
boxBlack.fill('white')

textRectWhite = textWhite.get_rect()
textRectWhite.center = (squareSize * 10, squareSize * 2)
textRectBlack = textWhite.get_rect()
textRectBlack.center = (squareSize * 10, squareSize * 2)

boxWhite2 = pygame.Surface((squareSize * 4 * 0.9, squareSize * 4 * 0.9))
boxWhite2.fill('black')

boxBlack2 = pygame.Surface((squareSize * 4 * 0.8, squareSize * 4 * 0.8))
boxBlack2.fill('white')

textTurn = font.render('Turn 0', True, black, white)
textRectTurn = textTurn.get_rect()
textRectTurn.center = (squareSize * 10, squareSize * 6)
# Setup turn Number display

# Setup images for every piece
whitePawn = pygame.image.load('./pieces/pawn_white.png').convert_alpha()
whitePawn = pygame.transform.scale(whitePawn, (squareSize, squareSize))

whiteRook = pygame.image.load('./pieces/rook_white.png').convert_alpha()
whiteRook = pygame.transform.scale(whiteRook, (squareSize, squareSize))

whiteBishop = pygame.image.load('./pieces/bishop_white.png').convert_alpha()
whiteBishop = pygame.transform.scale(whiteBishop, (squareSize, squareSize))

whiteKnight = pygame.image.load('./pieces/knight_white.png').convert_alpha()
whiteKnight = pygame.transform.scale(whiteKnight, (squareSize, squareSize))

whiteQueen = pygame.image.load('./pieces/queen_white.png').convert_alpha()
whiteQueen = pygame.transform.scale(whiteQueen, (squareSize, squareSize))

whiteKing = pygame.image.load('./pieces/king_white.png').convert_alpha()
whiteKing = pygame.transform.scale(whiteKing, (squareSize, squareSize))

blackPawn = pygame.image.load('pieces/pawn_black.png').convert_alpha()
blackPawn = pygame.transform.scale(blackPawn, (squareSize, squareSize))

blackRook = pygame.image.load('pieces/rook_black.png').convert_alpha()
blackRook = pygame.transform.scale(blackRook, (squareSize, squareSize))

blackBishop = pygame.image.load('pieces/bishop_black.png').convert_alpha()
blackBishop = pygame.transform.scale(blackBishop, (squareSize, squareSize))

blackKnight = pygame.image.load('pieces/knight_black.png').convert_alpha()
blackKnight = pygame.transform.scale(blackKnight, (squareSize, squareSize))

blackQueen = pygame.image.load('pieces/queen_black.png').convert_alpha()
blackQueen = pygame.transform.scale(blackQueen, (squareSize, squareSize))

blackKing = pygame.image.load('pieces/king_black.png').convert_alpha()
blackKing = pygame.transform.scale(blackKing, (squareSize, squareSize))

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

# Draw the board and place pieces from board b
# Highlight selected square s
# wt is boolean, if true is white's turn
# m is list of legal moves
# t is the turn number
# Future: show possible squares to move with selected piece
def drawBoard(b, s, wt, m, t):
    
    # Draw the squares
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0: 
                    screen.blit(l, (i * squareSize, j * squareSize))
                else:
                    screen.blit(d, (i * squareSize, j * squareSize))
            else:
                if j % 2 == 0: 
                    screen.blit(d, (i * squareSize, j * squareSize))
                else:
                    screen.blit(l, (i * squareSize, j * squareSize))
    # Place the pieces
    placePieces(b)
    # Highlight selected square
    # Convert square number to row and column
    if s is not None:
        #print(b)
        #print("Selected square number is ", s)
        x = s % 8
        y = s // 8
        #print("x is ", x, ", y is ", y)

        # Now take row and column to get to upper left corner of square
        squareX = x * squareSize
        squareY = y * squareSize
        # Draw half of border
        screen.blit(border1, (squareX, squareY))
        screen.blit(border2, (squareX, squareY))
        # Now need to change y for bottom row of border
        squareY2 = squareY + squareSize - borderSize
        # Need to change x for right column of border
        squareX2 = squareX + squareSize - borderSize
        # Draw other half
        screen.blit(border1, (squareX, squareY2))
        screen.blit(border2, (squareX2, squareY))

        # Highlight possible moves
        for possibleMove in m:
            if board[possibleMove] is None:
                pygame.draw.circle(screen, 'gray46', (possibleMove % 8 * squareSize + (squareSize * 0.5), possibleMove // 8 * squareSize  + (squareSize * 0.5)), squareSize * 0.2, 0)
            else:
                pygame.draw.circle(screen, 'gray46', (possibleMove % 8 * squareSize + (squareSize * 0.5), possibleMove // 8 * squareSize  + (squareSize * 0.5)), squareSize * 0.5, squareSize // 10)


        #pygame.draw.circle(screen, 'gray46', (3 * squareSize + (squareSize * 0.5), 3 * squareSize  + (squareSize * 0.5)), squareSize * 0.2, 0)
        #pygame.draw.circle(screen, 'gray46', (4 * squareSize + (squareSize * 0.5), 3 * squareSize  + (squareSize * 0.5)), squareSize * 0.5, squareSize // 10)


    # Display turn
    if wt:
        screen.blit(boxWhite, (squareSize * 8, 0))
        screen.blit(textWhite, textRectWhite)
    else:
        screen.blit(boxBlack, (squareSize * 8, 0))
        screen.blit(textBlack, textRectBlack)
    # Display turn number
    screen.blit(boxBlack, (squareSize * 8, squareSize * 4))
    screen.blit(boxWhite2, (squareSize * 8 + (squareSize * 0.2), squareSize * 4 + (squareSize * 0.2)))
    screen.blit(boxBlack2, (squareSize * 8 + (squareSize * 0.4), squareSize * 4 + (squareSize * 0.4)))

    turn = 'Turn ' + str(t)
    textTurn = font.render(turn, True, black, white)
    screen.blit(textTurn, textRectTurn)
        


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

# Return the square number by receiving input coordinates
def getSquare(coordinates):
    # Divide each coordinate by square size in order to get corresponding square row and column
    x = coordinates[0] // squareSize
    y = coordinates[1] // squareSize
    #print("X = ", x, ", y = ", y)
    # Convert the square row and column to location in array
    return (y * 8) + x
    
# Set up variables for game
board = startingBoard
run = True
whiteTurn = True
turnNumber = 0
#gameRun = True
selected = None
isCheck = False
legalMoves = []

#Main loop for running game
while run:
    drawBoard(board, selected, whiteTurn, legalMoves, turnNumber)
    # Running logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Get the position of mouse and convert it to a square
            pos = pygame.mouse.get_pos()
            square = getSquare(pos)
            # logic for selecting a piece
            if selected is None and board[square] is not None:
                #print("get Color = ", getColor(board[square]))
                if getColor(board[square]) > 0 and whiteTurn:
                    selected = square
                    legalMoves = getLegalMoves(board, selected)
                elif getColor(board[square]) < 0 and not whiteTurn:
                    selected = square
                    legalMoves = getLegalMoves(board, selected)
            # logic for moving a piece
            elif selected is not None:
                # Make a move and change turns, need to add logic to check if valid move
                temp = board[selected]
                board[selected] = None
                board[square] = temp
                selected = None
                # Change whose turn it is and update turn number if necessary
                whiteTurn = not whiteTurn
                if whiteTurn:
                    turnNumber += 1
            #print("At square ", square, " is the following piece:", board[square])
    


    
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
exit()