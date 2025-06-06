# Return 0 if place is empty, 1 if piece is white, and -1 if the piece is black
def getColor(piece):
    #print(piece)
    if piece is None:
        return 0
    elif piece == "P" or piece == "N" or piece == "B" or piece == "R" or piece == "Q" or piece == "K":
        return 1
    
    return -1

# get legal moves for selected piece s on the board b
def getLegalMoves(b, s):
    l = []
    # white pawn
    if b[s] == 'P':
        l = pawn(b, s, True)
    # black pawn
    elif b[s] == 'p':
        l = pawn(b, s, False)
    # white knight
    if b[s] == 'N':
        l = knight(b, s, True)
    # black knight
    elif b[s] == 'n':
        l = knight(b, s, False)
    # white bishop
    if b[s] == 'B':
        l = bishop(b, s, True)
    # black bishop
    elif b[s] == 'b':
        l = bishop(b, s, False)
    # white rook
    if b[s] == 'R':
        l = rook(b, s, True)
    # black rook
    elif b[s] == 'r':
        l = rook(b, s , False)
    # white queen
    if b[s] == 'Q':
        l = queen(b, s, True)
    # black queen
    elif b[s] == 'q':
        l = queen(b, s, False)
    # white king
    if b[s] == 'K':
        l = king(b, s, True)
    # black king
    elif b[s] == 'k':
        l = king(b, s, False)

    # need to check for checks if any of these moves are made and remove them from being playable?

    return l


def pawn(b, s , wt):

    l = []

    y = s // 8
    # pawn can move forward 2 if it is on starting square, can move forward 1 if not blocked, and can capture diagonally

    # NEED TO ACCOUNT FOR EN PASSANT IN THE FUTURE

    if wt:
        # check for case of being on starting square
        if y == 6 and b[s - 16] is None and b[s - 8] is None:
            l.append(s - 16)
        # now check forward move
        if y > 0 and b[s - 8] is None:
            l.append(s - 8)
        # now check 2 captures
        if y > 0 and getColor(b[s - 9]) < 0 and s % 8 > 0:
            l.append(s - 9)
        if y > 0 and getColor(b[s - 7]) < 0 and s % 8 < 7:
            l.append(s - 7)    
    else:
        # check for case of being on starting square
        if y == 1 and b[s + 16] is None and b[s + 8] is None:
            l.append(s + 16)
        # now check forward move
        if y < 7 and b[s + 8] is None:
            l.append(s + 8)
        # now check 2 captures
        if y < 7 and getColor(b[s + 9]) > 0 and s % 8 < 7:
            l.append(s + 9)
        if y < 7 and getColor(b[s + 7]) > 0 and s % 8 > 0:
            l.append(s + 7)    

    return l

def knight(b, s , wt):

    l = []
    
    # for knight need to check 8 locations to see if they are on the board and that a friendly piece is not there
    # for up and down just need to check bounds of s ( 0 <= s <= 63)
    # for left and right get the x coordinate of s and make sure it can move left or right the proper amount
    x = s % 8
    # finally if on board then check that there is not a piece of the same color on that square
    # location 1 (up 2, left 1)     s - 17
    if (s - 17) >= 0 and x > 0:
        if b[s - 17] is None:
            l.append(s - 17)
        elif getColor(b[s - 17]) < 0 and wt:
            l.append(s - 17)
        elif getColor(b[s - 17]) > 0 and not wt:
            l.append(s - 17)
    # location 2 (up 2, right 1)    s - 15
    if (s - 15) >= 0 and x < 7:
        if b[s - 15] is None:
            l.append(s - 15)
        elif getColor(b[s - 15]) < 0 and wt:
            l.append(s - 15)
        elif getColor(b[s - 15]) > 0 and not wt:
            l.append(s - 15)
    # location 3 (up 1, left 2)     s - 10
    if (s - 10) >= 0 and x > 1:
        if b[s - 10] is None:
            l.append(s - 10)
        elif getColor(b[s - 10]) < 0 and wt:
            l.append(s - 10)
        elif getColor(b[s - 10]) > 0 and not wt:
            l.append(s - 10)
    # location 4 (up 1, right 2)    s - 6
    if (s - 6) >= 0 and x < 6:
        if b[s - 6] is None:
            l.append(s - 6)
        elif getColor(b[s - 6]) < 0 and wt:
            l.append(s - 6)
        elif getColor(b[s - 6]) > 0 and not wt:
            l.append(s - 6)
    # location 5 (down 1, left 2)   s + 6
    if (s + 6) <= 63 and x > 1:
        if b[s + 6] is None:
            l.append(s + 6)
        elif getColor(b[s + 6]) < 0 and wt:
            l.append(s + 6)
        elif getColor(b[s + 6]) > 0 and not wt:
            l.append(s + 6)
    # location 6 (down 1, right 2)  s + 10
    if (s + 10) <= 63 and x < 6:
        if b[s + 10] is None:
            l.append(s + 10)
        elif getColor(b[s + 10]) < 0 and wt:
            l.append(s + 10)
        elif getColor(b[s + 10]) > 0 and not wt:
            l.append(s + 10)
    # location 7 (down 2, left 1)   s + 15
    if (s + 15) <= 63 and x > 0:
        if b[s + 15] is None:
            l.append(s + 15)
        elif getColor(b[s + 15]) < 0 and wt:
            l.append(s + 15)
        elif getColor(b[s + 15]) > 0 and not wt:
            l.append(s + 15)
    # location 8 (down 2, right 1)  s + 17
    if (s + 17) <= 63 and x < 7:
        if b[s + 17] is None:
            l.append(s + 17)
        elif getColor(b[s + 17]) < 0 and wt:
            l.append(s + 17)
        elif getColor(b[s + 17]) > 0 and not wt:
            l.append(s + 17)

    return l

def bishop(b, s , wt):

    l = []
    # calculate in the 4 diagonal directions until either the edge of the board or a piece is seen
    # if the piece seen is friendly then not valid square, if piece is opposite then it is a valid square
    x = s % 8
    y = s // 8
    
    offset = [-9, -7, 7, 9]
    foundPiece = False

    # up left
    foundPiece = False
    temp = s - 9
    while not foundPiece and temp >= 0 and temp % 8 < x and temp // 8 < y:
        if b[temp] is None:
            l.append(temp)
            temp -= 9
        else:
            foundPiece = True
            if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                l.append(temp)

    # up right
    foundPiece = False
    temp = s - 7
    while not foundPiece and temp >= 0 and temp % 8 > x and temp // 8 < y:
        if b[temp] is None:
            l.append(temp)
            temp -= 7
        else:
            foundPiece = True
            if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                l.append(temp)

    # down left
    foundPiece = False
    temp = s + 7
    while not foundPiece and temp <= 63 and temp % 8 < x and temp // 8 > y:
        if b[temp] is None:
            l.append(temp)
            temp += 7
        else:
            foundPiece = True
            if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                l.append(temp)

    # down right
    foundPiece = False
    temp = s + 9
    while not foundPiece and temp <= 63 and temp % 8 > x and temp // 8 > y:
        if b[temp] is None:
            l.append(temp)
            temp += 9
        else:
            foundPiece = True
            if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                l.append(temp)

    return l

def rook(b, s , wt):

    l = []
    x = s % 8
    y = s // 8
    # Need to go 4 directions until you hit a piece, and can move at that position if an opposite color to the selected piece

    # up
    foundPiece = False
    if y > 0:
        temp = s - 8
        while temp >= 0 and not foundPiece:
            if b[temp] is None:
                l.append(temp)
                temp -= 8
            else:
                foundPiece = True
                if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                    l.append(temp)
    
    # left
    foundPiece = False
    if x > 0:
        temp = s - 1
        while temp >= 0 and not foundPiece and temp % 8 < x:
            if b[temp] is None:
                l.append(temp)
                temp -= 1
            else:
                foundPiece = True
                if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                    l.append(temp)
    # right
    foundPiece = False
    if x < 7:
        temp = s + 1
        while temp <= 63 and not foundPiece and temp % 8 > x:
            if b[temp] is None:
                l.append(temp)
                temp += 1
            else:
                foundPiece = True
                if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                    l.append(temp)
    # down
    foundPiece = False
    if y < 7:
        temp = s + 8
        while temp <= 63 and not foundPiece:
            if b[temp] is None:
                l.append(temp)
                temp += 8
            else:
                foundPiece = True
                if getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
                    l.append(temp)


    return l

def queen(b, s , wt):
    # queen is essentially a rook and bishop combined, so need to check 4 diagonals and 4 cardinal directions
    l1 = bishop(b, s, wt)
    l2 = rook(b, s, wt)
    l = l1 + l2

    return l

def king(b, s , wt):

    l = []
    x = s % 8
    y = s // 8
    # need to check 8 directions

    # up left
    temp = s - 9
    if x > 0 and y > 0:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)
        

    # up
    temp = s - 8
    if y > 0:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)

    # up right
    temp = s - 7
    if x < 7 and y > 0:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)

    # left
    temp = s - 1
    if x > 0:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)

    # right
    temp = s + 1
    if x < 7:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)

    # down left
    temp = s + 7
    if x > 0 and y < 7:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)

    # down
    temp = s + 8
    if y < 7:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)
        
    # down right
    temp = s + 9
    if x < 7 and y < 7:
        if b[temp] is None or getColor(b[temp]) < 0 and wt or getColor(b[temp]) > 0 and not wt:
            l.append(temp)

    return l