
 # parent
class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def validMoves(self, board, x, y):
        print("need to have option to generate possible moves")


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False
    
    
    def validMoves(self, board, x, y):
        print("placeholder")

    #Once moved call moved() method
    def moved(self):
        self.moved = True
    #Use this to check for two space moves or en passant. 
    def hasMoved(self):
        return self.moved

        
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False

    def validMoves(self, board, x, y):
        print("placeholder")

    #Once moved call moved() method
    def moved(self):
        self.moved = True
    #Use this to check for valid castling
    def hasMoved(self):
        return self.moved

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def validMoves(self, board, x, y):
        print("placeholder")

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def validMoves(self, board, x, y):
        print("placeholder")

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def validMoves(self, board, x, y):
        #going to go through the 4 different directions using 4 forloops
        #This is all assuming it's from white players perspective.
        board.clearValid()

        #going top right
        for i in range(1, min(8 - x, 8 - y)):
            if board.hasPiece(x + i, y + i):
                if board.hasPiece(x + i, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y + i)
                    break
            board.addToValid(x + i, y + i)

        #going top left
        for i in range(1, min(x, 8 - y)):
            if board.hasPiece(x - i, y + i):
                if board.hasPiece(x - i, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y + i)
                    break
            board.addToValid(x - i, y + i)

        #going bottom right
        for i in range(1, min(8 - x, y)):
            if board.hasPiece(x + i, y - i):
                if board.hasPiece(x + i, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y - i)
                    break
            board.addToValid(x + i, y - i)

        #going bottom left
        for i in range(1, min(x, y)):
            if board.hasPiece(x - i, y - i):
                if board.hasPiece(x - i, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y - i)
                    break
            board.addToValid(x - i, y - i)

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False
    def validMoves(self, board, x, y):
        print("placeholder")
    
    #Once moved call moved() method
    def moved(self):
        self.moved = True
    #Use this to check for valid castling
    def hasMoved(self):
        return self.moved