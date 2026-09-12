import pygame, time
from sys import exit
from pieces import getLegalMoves, getColor, getAttackedSquares, findCheck, getAllMoves

# Sizes
squareSize = 75
borderSize = squareSize // 12

# Setup screen
pygame.init()
screen = pygame.display.set_mode((squareSize * 16, squareSize * 8))
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

font = pygame.font.SysFont('mvboli',  30)
font2 = pygame.font.SysFont('impact', 90)
font3 = pygame.font.SysFont('impact', 30)
font4 = pygame.font.SysFont('mvboli', 30)
# create a text surface object,
# on which text is drawn on it.
textWhite = font.render('White Turn', True, white, black)
boxWhite = pygame.Surface((squareSize * 4, squareSize * 4))
boxWhite.fill('black')

textBlack = font.render('Black Turn', True, black, white)
boxBlack = pygame.Surface((squareSize * 4, squareSize * 4))
boxBlack.fill('white')

textRectWhite = textWhite.get_rect()
textRectWhite.center = (squareSize * 10, squareSize * 1)
textRectBlack = textWhite.get_rect()
textRectBlack.center = (squareSize * 10, squareSize * 1)

boxWhite2 = pygame.Surface((squareSize * 4 * 0.9, squareSize * 4 * 0.9))
boxWhite2.fill('black')

boxBlack2 = pygame.Surface((squareSize * 4 * 0.8, squareSize * 4 * 0.8))
boxBlack2.fill('white')

# background boxes for options on right
boxOptionLight = pygame.Surface((squareSize * 4, squareSize * 8 / 3))
boxOptionLight.fill('burlywood1')
boxOptionDark = pygame.Surface((squareSize * 4, squareSize * 8 / 3))
boxOptionDark.fill('chocolate4')
# frame boxes for buttons on right
boxFrameLight = pygame.Surface((squareSize * 4 * 0.9, squareSize * 8 / 3 * 0.9))
boxFrameLight.fill('burlywood1')
boxFrameDark = pygame.Surface((squareSize * 4 * 0.9, squareSize * 8 / 3 * 0.9))
boxFrameDark.fill('chocolate4')
# button boxes on fight
boxButtonLight = pygame.Rect(squareSize * 12 + (squareSize * 0.4), (squareSize * 0.3), squareSize * 4 * 0.8, squareSize * 8 / 3 * 0.8)
#boxButtonLight.fill('burlywood1')
boxButtonDark = pygame.Rect(squareSize * 12 + (squareSize * 0.4), squareSize * 8 / 3 + (squareSize * 0.3), squareSize * 4 * 0.8, squareSize * 8 / 3 * 0.8)
#boxButtonDark.fill('chocolate4')
boxButtonLight2 = pygame.Rect(squareSize * 12 + (squareSize * 0.4), squareSize * 8 / 3 * 2 + (squareSize * 0.3), squareSize * 4 * 0.8, squareSize * 8 / 3 * 0.8)
#boxButtonLight2.fill('burlywood1')

# draw offer popup
boxDrawOffer = pygame.Rect(squareSize * 4, squareSize * 2, squareSize * 8, squareSize * 4)

# promotion popup
#boxPromotion = pygame.Rect
boxPromotion = pygame.Rect(0, 0, squareSize * 3, squareSize * 1)

# Setup turn Number display
textTurn = font.render('Turn 0', True, black, white)
textRectTurn = textTurn.get_rect()
textRectTurn.center = (squareSize * 10, squareSize * 5)
# Setup check display
textCheck = font.render('Check', True, black, white)
textRectCheck = textCheck.get_rect()
textRectCheck.center = (squareSize * 10, squareSize * 6)
#Setup checkmate display
textCheck2 = font.render('Checkmate', True, black, white)
textRectCheck2 = textCheck2.get_rect()
textRectCheck2.center = (squareSize * 10, squareSize * 6)

#Setup text for displaying who won
textWin = font.render('Draw', True, black, white)
textRectWin = textWin.get_rect()
textRectWin.center = (squareSize * 10, squareSize * 7)

# Setup text for draw, resign, and end game
textTie = font.render('Offer Draw', True, black)
textRectTie = textTie.get_rect()
textRectTie.center = (squareSize * 14, squareSize / 6 * 8)

textResign = font.render('Resign', True, black)
textRectResign = textResign.get_rect()
textRectResign.center = (squareSize * 14, squareSize * 4)

textEnd = font.render('End Game', True, black)
textRectEnd = textEnd.get_rect()
textRectEnd.center = (squareSize * 14, squareSize / 6 * 40)

boxWhiteTimer  = pygame.Rect(squareSize * 8.5, squareSize * 1.5, squareSize * 3, squareSize * 1)
boxWhiteTimerBorder = pygame.Rect(squareSize * 8.5, squareSize * 1.5, squareSize * 3, squareSize * 1)
boxBlackTimer  = pygame.Rect(squareSize * 8.5, squareSize * 2.75, squareSize * 3, squareSize * 1)
boxBlackTimerBorder = pygame.Rect(squareSize * 8.5, squareSize * 2.75, squareSize * 3, squareSize * 1)
# ---------------------------------- HOME SCREEN ----------------------------------------
# Chess title
textChess = font2.render('Chess', True, white, black)
textRectChess = textChess.get_rect()
textRectChess.center = (squareSize * 1.75, squareSize)

# Credit my name
textCredit = font3.render('coded by Ethan Bourne', True, white, black)
textRectCredit = textCredit.get_rect()
textRectCredit.center = (squareSize * 5.5, squareSize * 1.25)

# player title
textPlayer = font3.render('Players:', True, white, black)
textRectPlayer = textPlayer.get_rect()
textRectPlayer.center = (squareSize * 1, squareSize * 2.5)
textRectPlayer.left = squareSize * .5
# timer title
textTimerTitle = font3.render('Timer:', True, white, black)
textRectTimerTitle = textTimerTitle.get_rect()
textRectTimerTitle.center = (squareSize * 1, squareSize * 3.5)
textRectTimerTitle.left = squareSize * .5
# select color title
textSelectColor = font3.render('Select Color:', True, white, black)
textRectSelectColor = textSelectColor.get_rect()
textRectSelectColor.center = (squareSize * 1, squareSize * 4.5)
textRectSelectColor.left = squareSize * .5

# buttons for home screen
boxPlayer = pygame.Rect(squareSize * 3, squareSize * 2, squareSize * 2, squareSize * 0.75)
boxPlayer2 = pygame.Rect(squareSize * 6, squareSize * 2, squareSize * 2, squareSize * 0.75)

boxTimer1  = pygame.Rect(squareSize * 2, squareSize * 3, squareSize * 1.5, squareSize * 0.75)
boxTimer3  = pygame.Rect(squareSize * 3.75, squareSize * 3, squareSize * 1.5, squareSize * 0.75)
boxTimer5  = pygame.Rect(squareSize * 5.5, squareSize * 3, squareSize * 1.5, squareSize * 0.75)
boxTimer10  = pygame.Rect(squareSize * 7.25, squareSize * 3, squareSize * 1.5, squareSize * 0.75)
boxTimer0  = pygame.Rect(squareSize * 9, squareSize * 3, squareSize * 1.5, squareSize * 0.75)

boxSelectWhite  = pygame.Rect(squareSize * 3, squareSize * 4, squareSize * 2, squareSize * 0.75)
boxSelectBlack  = pygame.Rect(squareSize * 6, squareSize * 4, squareSize * 2, squareSize * 0.75)

boxStartGame  = pygame.Rect(squareSize * 4, squareSize * 6, squareSize * 3.5, squareSize * 1.5)
boxStartGameBorder = pygame.Rect(squareSize * 4, squareSize * 6, squareSize * 3.5, squareSize * 1.5)

# text for home screen buttons
textOnePlayer = font3.render('1 Player', True, black, None)
textRectOnePlayer = textOnePlayer.get_rect()
textRectOnePlayer.center = boxPlayer.center

textTwoPlayer = font3.render('2 Players', True, black, None)
textRectTwoPlayer = textTwoPlayer.get_rect()
textRectTwoPlayer.center = boxPlayer2.center

textTimer1 = font3.render('1 min', True, black, None)
textRectTimer1 = textTimer1.get_rect()
textRectTimer1.center = boxTimer1.center

textTimer3 = font3.render('3 min', True, black, None)
textRectTimer3 = textTimer3.get_rect()
textRectTimer3.center = boxTimer3.center

textTimer5 = font3.render('5 min', True, black, None)
textRectTimer5 = textTimer5.get_rect()
textRectTimer5.center = boxTimer5.center

textTimer10 = font3.render('10 min', True, black, None)
textRectTimer10 = textTimer10.get_rect()
textRectTimer10.center = boxTimer10.center

textTimer0 = font3.render('None', True, black, None)
textRectTimer0 = textTimer0.get_rect()
textRectTimer0.center = boxTimer0.center

textSelectWhite = font3.render('White', True, black, None)
textRectSelectWhite = textSelectWhite.get_rect()
textRectSelectWhite.center = boxSelectWhite.center

textSelectBlack = font3.render('Black', True, black, None)
textRectSelectBlack = textSelectBlack.get_rect()
textRectSelectBlack.center = boxSelectBlack.center

textStartGame = font3.render('Start Game', True, black, None)
textRectStartGame = textStartGame.get_rect()
textRectStartGame.center = boxStartGame.center

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
# m is list of legal moves for selected square s
# t is the turn number
# c is boolean, if true it is check
# cm is boolean, if true it is checkmate
# r is winner, if -1 than black wins, 1 if white wins, 0 if draw, and none if game is still continuing
# p is boolean, if true than there is a pawn that needs to be promoted
# dOffer is boolean, if true a draw was offered and needs to be accepted or rejected
# ps is square of pawn being promoted
# tl is the timer length for the game
def drawBoard(b, s, wt, m, t, c, cm, r, p, dOffer, ps, tl):
    
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

    # Check for checkmate conditions
    #allMoves = getAllMoves(b, wt)

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

    # Display if it is check or checkmate
    if c:
        if cm:
            check2 = 'Checkmate'
            textCheck2 = font.render(check2, True, black, white)
            screen.blit(textCheck2, textRectCheck2)
        else:
            check = 'Check'
            textCheck = font.render(check, True, black, white)
            screen.blit(textCheck, textRectCheck)
    else:
        check = ''
        check2 = ''
        textCheck = font.render(check, True, black, white)
        screen.blit(textCheck, textRectCheck)

    # Display winner if there is a winner
    if r is not None:
        #print("Winner is: ", r)

        if r == 0:
            #print("tie")
            whoWon = 'Draw'
        elif r == 1:
            #print('white wins')
            whoWon = 'White Wins!'
        else:
            #print('black wins')
            whoWon = 'Black Wins!'

        textWin = font.render(whoWon, True, black, white)
        textRectWin = textWin.get_rect()
        textRectWin.center = (squareSize * 10, squareSize * 7)
        screen.blit(textWin, textRectWin)
    
    

    #print(pygame.mouse.get_pos())
    
    # Display draw offer button (tbd)
    screen.blit(boxOptionLight, (squareSize * 12, 0))
    screen.blit(boxFrameDark, (squareSize * 12 + (squareSize * 0.2), (squareSize * 0.15)))
    current_color = None
    if boxButtonLight.collidepoint(pygame.mouse.get_pos()):
        current_color = 'burlywood1'
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    else:
        current_color = 'chocolate4'
        #pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.draw.rect(screen, current_color, boxButtonLight, 0, squareSize // 2)
    screen.blit(textTie, textRectTie)

    # Display resignation button (tbd)

    screen.blit(boxOptionDark, (squareSize * 12, squareSize * 8 / 3))
    screen.blit(boxFrameLight, (squareSize * 12 + (squareSize * 0.2), squareSize * 8 / 3 + (squareSize * 0.15)))
    current_color2 = None
    if boxButtonDark.collidepoint(pygame.mouse.get_pos()):
        current_color2 = 'chocolate4'
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    else:
        current_color2 = 'burlywood1'
        #pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.draw.rect(screen, current_color2, boxButtonDark, 0 ,squareSize // 2)

    screen.blit(textResign, textRectResign)

    # Display end game button (tbd)

    screen.blit(boxOptionLight, (squareSize * 12, squareSize * 8 / 3 * 2))
    screen.blit(boxFrameDark, (squareSize * 12 + (squareSize * 0.2), squareSize * 8 / 3 * 2 + (squareSize * 0.15)))
    #screen.blit(boxButtonLight, (squareSize * 12 + (squareSize * 0.4), squareSize * 8 / 3 * 2 + (squareSize * 0.3)))
    current_color3 = None
    if boxButtonLight2.collidepoint(pygame.mouse.get_pos()):
        current_color3 = 'burlywood1'
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    else:
        current_color3 = 'chocolate4'
        #pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.draw.rect(screen, current_color3, boxButtonLight2, 0 ,squareSize // 2)

    screen.blit(textEnd, textRectEnd)

    # Draw offer popup
    if dOffer:
        pygame.draw.rect(screen, 'red', boxDrawOffer)

    # Promotion popup
    if p:
        #boxPromotion = pygame.Rect(squareSize * 4, squareSize * 2, squareSize * 3, squareSize * 1)
        
        px = ps % 8
        py = ps // 8

        boxPromotion = pygame.Rect(squareSize * px, squareSize * py, squareSize * 3, squareSize * 1)
        #print('boxPromotion x = ', boxPromotion.x, ' boxPromotion y = ', boxPromotion.y)
        pygame.draw.rect(screen, 'white', boxPromotion)
        if wt:
            screen.blit(blackQueen, (squareSize * px, squareSize * py))
            screen.blit(blackRook, (squareSize * (px + 1), squareSize * py))
            screen.blit(blackKnight, (squareSize * (px + 2), squareSize * py))
        else:
            screen.blit(whiteQueen, (squareSize * px, squareSize * py))
            screen.blit(whiteRook, (squareSize * (px + 1), squareSize * py))
            screen.blit(whiteKnight, (squareSize * (px + 2), squareSize * py))


        

    # Display timer boxes
    if tl != 0:
        pygame.draw.rect(screen, 'white', boxWhiteTimer)
        pygame.draw.rect(screen, 'gray', boxWhiteTimerBorder, squareSize // 10, 0)

        pygame.draw.rect(screen, 'black', boxBlackTimer)
        pygame.draw.rect(screen, 'gray', boxBlackTimerBorder, squareSize // 10, 0)

# Draw the home screen
# n is number of players
# t is timer length
# wt is true if one player is playing as white, false if one player is playing as black
def drawHome(n, t, wt):
    pygame.draw.rect(screen, black, pygame.Rect(0, 0, squareSize * 16, squareSize * 8))
    screen.blit(textChess, textRectChess)
    screen.blit(textCredit, textRectCredit)
    # draw titles
    screen.blit(textPlayer, textRectPlayer)
    screen.blit(textTimerTitle, textRectTimerTitle)
    if numPlayers == 1:
        screen.blit(textSelectColor, textRectSelectColor)
    # draw select player buttons
    if numPlayers == 1:
        pygame.draw.rect(screen, 'green', boxPlayer, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxPlayer2, 0, squareSize // 10)
    else:
        pygame.draw.rect(screen, 'gray', boxPlayer, 0, squareSize // 10)
        pygame.draw.rect(screen, 'green', boxPlayer2, 0, squareSize // 10)
    # text for selecting player
    screen.blit(textOnePlayer, textRectOnePlayer)
    screen.blit(textTwoPlayer, textRectTwoPlayer)
    # draw timer buttons
    if t == 1:
        pygame.draw.rect(screen, 'gray', boxTimer0, 0, squareSize // 10)
        pygame.draw.rect(screen, 'green', boxTimer1, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer3, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer5, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer10, 0, squareSize // 10)
    elif t == 3:
        pygame.draw.rect(screen, 'gray', boxTimer0, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer1, 0, squareSize // 10)
        pygame.draw.rect(screen, 'green', boxTimer3, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer5, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer10, 0, squareSize // 10)
    elif t == 5:
        pygame.draw.rect(screen, 'gray', boxTimer0, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer1, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer3, 0, squareSize // 10)
        pygame.draw.rect(screen, 'green', boxTimer5, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer10, 0, squareSize // 10)
    elif t == 10:
        pygame.draw.rect(screen, 'gray', boxTimer0, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer1, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer3, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer5, 0, squareSize // 10)
        pygame.draw.rect(screen, 'green', boxTimer10, 0, squareSize // 10)
    else:
        pygame.draw.rect(screen, 'green', boxTimer0, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer1, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer3, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer5, 0, squareSize // 10)
        pygame.draw.rect(screen, 'gray', boxTimer10, 0, squareSize // 10)

    # text for timers
    screen.blit(textTimer1, textRectTimer1)
    screen.blit(textTimer3, textRectTimer3)
    screen.blit(textTimer5, textRectTimer5)
    screen.blit(textTimer10, textRectTimer10)
    screen.blit(textTimer0, textRectTimer0)

    # select color
    if n == 1:

        if wt:
            pygame.draw.rect(screen, 'green', boxSelectWhite, 0, squareSize // 10)
            pygame.draw.rect(screen, 'gray', boxSelectBlack, 0, squareSize // 10)
        else:
            pygame.draw.rect(screen, 'gray', boxSelectWhite, 0, squareSize // 10)
            pygame.draw.rect(screen, 'green', boxSelectBlack, 0, squareSize // 10)

        screen.blit(textSelectWhite, textRectSelectWhite)
        screen.blit(textSelectBlack, textRectSelectBlack)

    pygame.draw.rect(screen, 'chocolate4', boxStartGame, 0, squareSize // 10)
    pygame.draw.rect(screen, 'burlywood1', boxStartGameBorder, squareSize // 8, squareSize // 10)
    screen.blit(textStartGame, textRectStartGame)


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
board = startingBoard.copy()
run = True
whiteTurn = True
turnNumber = 0
fiftyTurnCounter = 0
enPassantPawn = -1

whiteShortCastle = True
whiteLongCastle = True
blackShortCastle = True
blackLongCastle = True

promotion = False
promotionSquare = None
drawOffered = False

selected = None
isCheck = False
isMate = False
winner = None
isGameValid = True
legalMoves = []
playing = False

numPlayers = 2
timerLength = 0
selectColor = True

startTime = 0
endTime = 0
whiteTimer = 0
blackTimer = 0

pygame.mouse.set_cursor(*pygame.cursors.arrow)

#Main loop for running game
while run:

    # Either display home screen or game screen
    # Currently only display game screen with drawBoard
    if playing:
        drawBoard(board, selected, whiteTurn, legalMoves, turnNumber, isCheck, isMate, winner, promotion, drawOffered, promotionSquare, timerLength)
        # run timer with updated values
        if timerLength != 0:
            if whiteTurn:
                #print('Hi')
                textWhiteTimer = font4.render('0:00', True, black, None)
                textBlackTimer = font4.render('0:00', True, white, None)
            else:
                textBlackTimer = font4.render('0:00', True, white, None)
                textWhiteTimer = font4.render('0:00', True, black, None)

            textRectWhiteTimer = textWhiteTimer.get_rect()
            textRectWhiteTimer.center = boxWhiteTimer.center
            textRectBlackTimer = textBlackTimer.get_rect()
            textRectBlackTimer.center = boxBlackTimer.center

            screen.blit(textWhiteTimer, textRectWhiteTimer)
            screen.blit(textBlackTimer, textRectBlackTimer)

    else:
        drawHome(numPlayers, timerLength, selectColor)
        

    # Running logic
    for event in pygame.event.get():
        # Quit application when you x out
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:

            # if mouse is released on board screen
            if playing:
                # game screen loop, has to handle cases where either draw is offered or piece is promoted
                if not drawOffered and not promotion:
                    # Get the position of mouse and convert it to a square
                    pos = pygame.mouse.get_pos()
                    square = getSquare(pos)
                    # logic for clicking on the board
                    if pos[0] <= 600 and isGameValid:
                        # logic for selecting a piece
                        if selected is None and board[square] is not None and isGameValid:
                            #print("get Color = ", getColor(board[square]))
                            if getColor(board[square]) > 0 and whiteTurn:
                                selected = square
                                legalMoves = getLegalMoves(board, selected)
                            elif getColor(board[square]) < 0 and not whiteTurn:
                                selected = square
                                legalMoves = getLegalMoves(board, selected)
                        # logic for moving a piece
                        elif selected is not None:
                            # Make a move if clicked square is legal
                            if square in legalMoves:
                                # Move the selected piece to its new square


                                temp = board[selected]
                                board[selected] = None
                                board[square] = temp
                                selected = None


                                # Pawn promotion case (TBD)
                                # if white pawn makes it to 8th rank, or black pawn makes it to 1st rank
                                print('temp is: ', temp)
                                print('square is: ', square) 
                                if temp == 'p' and square > 55 or temp == 'P' and square < 8:
                                    print('Reached promotion')
                                    promotion = True
                                    promotionSquare = square
                                # Does the move allow for en passant?

                                # See if there is a check
                                isCheck = findCheck(board, whiteTurn)

                                # See if game should end by checkmate or stalemate
                                # get all moves for piece of opposite color
                                allMoves = getAllMoves(board, not whiteTurn)
                                if not allMoves:
                                    if not isCheck:
                                        winner = 0
                                    elif whiteTurn:
                                        winner = 1
                                        isMate = True
                                    else:
                                        winner = -1
                                        isMate = True
                                    isGameValid = False

                                # See if game ends by threefold repetition (TBD)

                                # Change whose turn it is and update turn number if necessary
                                # NEED TO TRACK 50 TURN RULE (TBD)
                                whiteTurn = not whiteTurn
                                if whiteTurn:
                                    turnNumber += 1
                                # Timer logic (TBD)
                            # if you click on the selected piece again then deselect the piece
                            elif square is selected:
                                selected = None
                            # if you click on another piece then select that piece instead
                            elif getColor(board[square]) == getColor(board[selected]):
                                selected = square
                                legalMoves = getLegalMoves(board, selected)

                            # end of moving piece logic
                    # logic of draw offer (TBD)
                    if (boxButtonLight.collidepoint(pygame.mouse.get_pos())) and isGameValid:
                        print('Offer draw')
                        drawOffered = True
                    # logic of resigning
                    if (boxButtonDark.collidepoint(pygame.mouse.get_pos())) and isGameValid:
                        print('Resign')
                        isGameValid = False
                        if whiteTurn:
                            winner = -1
                        else:
                            winner = 1
                    # logic of end game (TBD)
                    if (boxButtonLight2.collidepoint(pygame.mouse.get_pos())):
                        print('End Game')
                        # For the moment this resets the game to starting conditions
                        board = startingBoard.copy()
                        run = True
                        whiteTurn = True
                        turnNumber = 0
                        fiftyTurnCounter = 0
                        enPassantPawn = -1
                        whiteShortCastle = True
                        whiteLongCastle = True
                        blackShortCastle = True
                        blackLongCastle = True
                        promotion = False
                        promotionSquare = None
                        drawOffered = False
                        selected = None
                        isCheck = False
                        isMate = False
                        winner = None
                        isGameValid = True

                        playing = False

                # draw offer logic (TBD)
                elif drawOffered:
                    print("You made it")
                    if (boxDrawOffer.collidepoint(pygame.mouse.get_pos())):
                        drawOffered = False
                # logic for if a pawn reaches the last rank
                elif promotion:
                    print("Promotion")
                    #get promotion square coordinates to display options for piece to promote pawn to
                    px = promotionSquare % 8
                    py = promotionSquare // 8
                    boxPromotion = pygame.Rect(squareSize * px, squareSize * py, squareSize * 3, squareSize * 1)
                    if (boxPromotion.collidepoint(pygame.mouse.get_pos())):
                        #print('promotionSquare is: ', promotionSquare)
                        clickedX = pygame.mouse.get_pos()[0] // squareSize
                        #print('px is: ', px, ', while clicked x is: ', clickedX, 'is white: ', whiteTurn)
                        # get x coordinate that is clicked on to decide what piece the pawn becomes
                        if not whiteTurn:
                            if clickedX == px:
                                board[promotionSquare] = 'Q'
                            elif clickedX == px + 1:
                                board[promotionSquare] = 'R'
                            else:
                                board[promotionSquare] = 'N'
                        else:
                            if clickedX == px:
                                board[promotionSquare] = 'q'
                            elif clickedX == px + 1:
                                board[promotionSquare] = 'r'
                            else:
                                board[promotionSquare] = 'n'
                        #update conditions to not handle a promotion
                        promotion = False
                        promotionSquare = None
                    #print("At square ", square, " is the following piece:", board[square])
            # Mouse event for home screen
            else:
                # Handle clicking every single button
                # Start Button
                if (boxStartGame.collidepoint(pygame.mouse.get_pos())):
                    playing = True
                # 1 player
                elif (boxPlayer.collidepoint(pygame.mouse.get_pos())):
                    numPlayers = 1
                # 2 player
                elif (boxPlayer2.collidepoint(pygame.mouse.get_pos())):
                    numPlayers = 2
                # Timer 1 min
                elif (boxTimer1.collidepoint(pygame.mouse.get_pos())):
                    timerLength = 1
                    startTime = time.perf_counter()
                    print('Start time is: ', startTime)
                # Timer 3 min
                elif (boxTimer3.collidepoint(pygame.mouse.get_pos())):
                    timerLength = 3
                    endTime = time.perf_counter() - startTime
                    print('Time difference: ', endTime)
                    print('Min = ', endTime // 60, ', Seconds = ', endTime % 60, ', Milliseconds = ', endTime - int(endTime))
                # Timer 5 min
                elif (boxTimer5.collidepoint(pygame.mouse.get_pos())):
                    timerLength = 5
                # Timer 10 min
                elif (boxTimer10.collidepoint(pygame.mouse.get_pos())):
                    timerLength = 10
                # Timer None
                elif (boxTimer0.collidepoint(pygame.mouse.get_pos())):
                    timerLength = 0
                elif (boxSelectWhite.collidepoint(pygame.mouse.get_pos())) and numPlayers == 1:
                    selectColor = True
                elif (boxSelectBlack.collidepoint(pygame.mouse.get_pos())) and numPlayers == 1:
                    selectColor = False
                #print(pygame.font.get_fonts())
    


    
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
exit()