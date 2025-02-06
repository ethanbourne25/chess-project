# Base Class for a piece, every individual piece is a subclass of this
class Piece:
    # Constructor
    def __init__(self, color, numMoves):
        self.color = color
        self.numMoves = numMoves
        self.type = None
        self.position = None

    # Return all squares that the piece "sees"
    def visibleSquares(self, board):
        return None
    
    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        return None

# Class for a pawn
class Pawn(Piece):
    # Constructor
    def __init__(self, color, numMoves, position):
        super().__init__(self, color, numMoves)
        self.type = "pawn"
        self.position = position
    
    # Return all squares that the piece "sees" for captures
    def visibleSquares(self, board):
        # For visible squares for a pawn, it can see diagonally ahead
        if self.color == "white":
            print(2)
        else:
            print(3)

    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        return None

# Class for a knight
class Knight(Piece):
    # Constructor
    def __init__(self, color, numMoves, position):
        super().__init__(self, color, numMoves)
        self.type = "knight"
        self.position = position
    
    # Return all squares that the piece "sees"
    def visibleSquares(self, board):
        # Knight moves in L shape
        visible = []
        # 2 up, 1 left
        if self.position[0] >= 1 and self.position[1] <= 5:
            visible.append((self.position[0] - 1, self.position[1] + 2))
        # 2 up, 1 right
        if self.position[0] <= 6 and self.position[1] <= 5:
            visible.append((self.position[0] + 1, self.position[1] + 2))
        # 2 left, 1 up
        if self.position[0] >= 2 and self.position[1] <= 6:
            visible.append((self.position[0] - 2, self.position[1] + 1))
        # 2 left, 1 down
        if self.position[0] >= 2 and self.position[1] >= 1:
            visible.append((self.position[0] - 2, self.position[1] - 1))
        # 2 right, 1 up
        if self.position[0] <= 5 and self.position[1] <= 6:
            visible.append((self.position[0] + 2, self.position[1] + 1))
        # 2 right, 1 down
        if self.position[0] <= 5 and self.position[1] >= 1:
            visible.append((self.position[0] + 2, self.position[1] - 1))
        # 2 down, 1 left
        if self.position[0] >= 1 and self.position[1] >= 2:
            visible.append((self.position[0] - 1, self.position[1] - 2))
        # 2 down, 1 right
        if self.position[0] <= 6 and self.position[1] >= 2:
            visible.append((self.position[0] + 1, self.position[1] - 2))

        return visible
    
    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        possibleMoves = []
        visible = self.visibleSquares(board)
        for pos in visible:
            # Now check if square has piece of same color, if not, then add to possible moves
            possibleMoves.append(pos)
            # Have to account for pins though, ugh

        return possibleMoves

# Class for a bishop
class Bishop(Piece):
    # Constructor
    def __init__(self, color, numMoves, position):
        super().__init__(self, color, numMoves)
        self.type = "bishop"
        self.position = position
    
    # Return all squares that the piece "sees"
    def visibleSquares(self, board):
        return None
    
    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        return None

# Class for a rook
class Rook(Piece):
    # Constructor
    def __init__(self, color, numMoves, position):
        super().__init__(self, color, numMoves)
        self.type = "rook"
        self.position = position

    # Return all squares that the piece "sees"
    def visibleSquares(self, board):
        return None
    
    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        return None

# Class for a queen
class Queen(Piece):
    # Constructor
    def __init__(self, color, numMoves, position):
        super().__init__(self, color, numMoves)
        self.type = "queen"
        self.position = position

    # Return all squares that the piece "sees"
    def visibleSquares(self, board):
        return None
    
    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        return None

# Class for a king
class King(Piece):
    # Constructor
    def __init__(self, color, numMoves, position):
        super().__init__(self, color, numMoves)
        self.type = "king"
        self.position = position

    # Return all squares that the piece "sees"
    def visibleSquares(self, board):
        return None
    
    # Return all squares that the piece can move to
    def possibleMoves(self, board):
        return None
           
