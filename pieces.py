# get legal moves for selected piece s on the board b
def getLegalMoves(b, s):
    l = []

    if b[s] == 'P':
        l = pawn(b, s, True)
    elif b[s] == 'p':
        l = pawn(b, s, False)

    return l


def pawn(b, s , wt):

    l = []
    if wt:
        l.append(s - 8)
    else:
        l.append(s + 8)

    return l

def knight():
    
    return None

def bishop():
    
    return None

def rook():
    
    return None

def queen():
    
    return None

def king():
    
    return None