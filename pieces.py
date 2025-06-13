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
    
    # get visible moves for your selected piece
    l = getVisibleMoves(b, s)
    
    # get king location for your color pieces
    kW = None
    kB = None

    loc = 0
    for pos in b:
        if pos == 'K':
            kW = loc
            break
        elif pos == 'k':
            kB = loc
        loc += 1
        if kW is not None and kB is not None:
            break

    if getColor(b[s]) > 0:
        wt = True
    else:
        wt = False

    print("white king location is ", kW,' black king loc is ', kB, ' and color is white is ', wt)

    lRemove = []
    # now go through your legal moves
    if s != kW and s != kB:
        for i in range(0, len(l)):
            #make the move in a fake board state. if in the resulting fake board state your king is attacked, then the move is not legal and should be removed
            print ('i is ', i, ' of value ', l[i], ' in l: ', l)
            # Create extra board
            b2 = b.copy()
            # Move the piece
            b2[l[i]] = b2[s]
            b2[s] = None

            # Go through the pieces of the opposite color
            for s2 in range(0, 64):
                # You cannot move if resulting move ends in your king attacked, this essentially adds pins
                # if black piece and its whites move
                if getColor(b2[s2]) < 0 and wt:
                    l2 = getVisibleMoves(b2, s2)
                    #print('l2 is ', l2, ' for s2 of ', s2)
                    if kW in l2:
                        lRemove.append(l[i])
                # if white piece and its blacks move
                elif getColor(b2[s2]) > 0 and not wt:
                    l2 = getVisibleMoves(b2, s2)
                    if kB in l2:
                        lRemove.append(l[i])

                    


    

            
    
    print('List of visible moves is: ', l)
    print('List of moves to be removed is: ', lRemove)

    return list(set(l) - set(lRemove))

def getVisibleMoves(b, s):
    l = []
    # white pawn
    if b[s] == 'P':
        l = pawn(b, s, True)
    # black pawn
    elif b[s] == 'p':
        l = pawn(b, s, False)
    # white knight
    elif b[s] == 'N':
        l = knight(b, s, True)
    # black knight
    elif b[s] == 'n':
        l = knight(b, s, False)
    # white bishop
    elif b[s] == 'B':
        l = bishop(b, s, True)
    # black bishop
    elif b[s] == 'b':
        l = bishop(b, s, False)
    # white rook
    elif b[s] == 'R':
        l = rook(b, s, True)
    # black rook
    elif b[s] == 'r':
        l = rook(b, s , False)
    # white queen
    elif b[s] == 'Q':
        l = queen(b, s, True)
    # black queen
    elif b[s] == 'q':
        l = queen(b, s, False)
    # white king
    elif b[s] == 'K':
        l = king(b, s, True)
    # black king
    elif b[s] == 'k':
        l = king(b, s, False)

    return l

# return a list of all attacked squares by one color on the board
def getAttackedSquares(b, wt):
    l = []
    for i in range(0, len(b)):
        if getColor(b[i]) > 0 and wt:
            if b[i] == 'P':
                if i // 8 > 0 and i % 8 > 0:
                    l.append(i - 9)
                if i // 8 > 0 and i % 8 < 7:
                    l.append(i - 7)
            elif b[i] == 'N':
                l2 = knightVisible(i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'B':
                l2 = bishopVisible(b, i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'R':
                l2 = rookVisible(b, i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'Q':
                l2 = queenVisible(b, i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'K':
                l2 = kingVisible(i)
                l = list(set(l).union(set(l2)))
        elif getColor(b[i]) < 0 and not wt:
            if b[i] == 'p':
                if i // 8 < 7 and i % 8 < 7:
                    l.append(i + 9)
                if i // 8 < 7 and i % 8 > 0:
                    l.append(i + 7)    
            elif b[i] == 'n':
                l2 = knightVisible(i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'b':
                l2 = bishopVisible(b, i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'r':
                l2 = rookVisible(b, i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'q':
                l2 = queenVisible(b, i)
                l = list(set(l).union(set(l2)))
            elif b[i] == 'k':
                l2 = kingVisible(i)
                l = list(set(l).union(set(l2)))

    return l
            
def findCheck(b, wt):
    l = getAttackedSquares(b, wt)
    # get king location for your color pieces
    kW = None
    kB = None

    loc = 0
    for pos in b:
        if pos == 'K':
            kW = loc
            break
        elif pos == 'k':
            kB = loc
        loc += 1
        if kW is not None and kB is not None:
            break
    
    if kB in l and wt or kW in l and not wt:
        return True
    
    return False


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

def knightVisible(s):
    l = []
    # for knight need to check 8 locations to see if they are on the board
    # for up and down just need to check bounds of s ( 0 <= s <= 63)
    # for left and right get the x coordinate of s and make sure it can move left or right the proper amount
    x = s % 8
    # finally if on board then check that there is not a piece of the same color on that square
    # location 1 (up 2, left 1)     s - 17
    if (s - 17) >= 0 and x > 0:
        l.append(s - 17)
    # location 2 (up 2, right 1)    s - 15
    if (s - 15) >= 0 and x < 7:
        l.append(s - 15)
    # location 3 (up 1, left 2)     s - 10
    if (s - 10) >= 0 and x > 1:       
        l.append(s - 10)
    # location 4 (up 1, right 2)    s - 6
    if (s - 6) >= 0 and x < 6:
        l.append(s - 6)
    # location 5 (down 1, left 2)   s + 6
    if (s + 6) <= 63 and x > 1:
        l.append(s + 6)
    # location 6 (down 1, right 2)  s + 10
    if (s + 10) <= 63 and x < 6:
        l.append(s + 10)
    # location 7 (down 2, left 1)   s + 15
    if (s + 15) <= 63 and x > 0:
        l.append(s + 15)
    # location 8 (down 2, right 1)  s + 17
    if (s + 17) <= 63 and x < 7:
        l.append(s + 17)

    return l

def knight(b, s , wt):

    l = knightVisible(s)
    lRemove = []
    # filter out squares with friendly piece
    for i in l:
        if getColor(b[i]) > 0 and wt or getColor(b[i]) < 0 and not wt:
            lRemove.append(i)

    return list(set(l) - set(lRemove))


def bishopVisible(b, s):
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
            l.append(temp)

    return l

def bishop(b, s , wt):
    l = bishopVisible(b, s)
    lRemove = []
    # filter out squares with friendly piece
    for i in l:
        if getColor(b[i]) > 0 and wt or getColor(b[i]) < 0 and not wt:
            lRemove.append(i)

    return list(set(l) - set(lRemove))


    

def rookVisible(b, s):
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
                l.append(temp)
    
    return l


def rook(b, s , wt):

    l = rookVisible(b, s)
    lRemove = []
    # filter out squares with friendly piece
    for i in l:
        if getColor(b[i]) > 0 and wt or getColor(b[i]) < 0 and not wt:
            lRemove.append(i)

    return list(set(l) - set(lRemove))

def queenVisible(b, s):
    l1 = rookVisible(b, s)
    l2 = bishopVisible(b, s)
    return l1 + l2

def queen(b, s , wt):
    # queen is essentially a rook and bishop combined, so need to check 4 diagonals and 4 cardinal directions
    l = queenVisible(b, s)
    lRemove = []
    # filter out squares with friendly piece
    for i in l:
        if getColor(b[i]) > 0 and wt or getColor(b[i]) < 0 and not wt:
            lRemove.append(i)

    return list(set(l) - set(lRemove))

def kingVisible(s):
    l = []
    x = s % 8
    y = s // 8
    # need to check 8 directions
    # up left
    temp = s - 9
    if x > 0 and y > 0:
        l.append(temp)
    
    # up
    temp = s - 8
    if y > 0:
        l.append(temp)

    # up right
    temp = s - 7
    if x < 7 and y > 0:
        l.append(temp)

    # left
    temp = s - 1
    if x > 0:
        l.append(temp)

    # right
    temp = s + 1
    if x < 7:
        l.append(temp)

    # down left
    temp = s + 7
    if x > 0 and y < 7:
        l.append(temp)

    # down
    temp = s + 8
    if y < 7:
        l.append(temp)
        
    # down right
    temp = s + 9
    if x < 7 and y < 7:
        l.append(temp)
    
    return l

def king(b, s , wt):

    l = kingVisible(s)

    lRemove = []
    # filter out squares with friendly piece
    for i in l:
        if getColor(b[i]) > 0 and wt or getColor(b[i]) < 0 and not wt:
            lRemove.append(i)

    l2 = list(set(l) - set(lRemove))
    # filter out if opponent piece sees square in l
    lRemove2 = getAttackedSquares(b, not wt)



    return list(set(l2) - set(lRemove2))

