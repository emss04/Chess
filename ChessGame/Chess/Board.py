from Piece import Rook, Bishop, Knight, Queen, King, Pawn


class Board:
    def __init__(self):
        self.board = []
        self.validMoves = []


    def addToValid(self, x, y):
        self.validMoves.append([x, y])
   
    def clearValid(self):
        self.validMoves.clear()


    #checks if there is piece at x, y, if there is return
    #piece located there,
    #if none return None(null)
    def hasPiece(self, x, y):
        if self.board[x][y] is None:
            return None
        else:
            return self.board[x][y]
   
    def reset(self):
        #Initializing/Resetting board to be able to access positions
        self.board = []
        for i in range(8):
            curRow = []
            for j in range(8):
                curRow.append(None)
            self.board.append(curRow)


        #white side
        self.board[0] = [Rook("white", 0, 0), Bishop("white", 1, 0), Knight("white", 2, 0),
                        Queen("white", 3, 0), King("white", 4, 0), Knight("white", 5, 0),
                        Bishop("white", 6, 0), Rook("white", 7, 0)]
        #pawns
        for i in range(8):
            self.board[1][i] = Pawn("white", i, 1)  


        #black side
        self.board[7] = [Rook("black", 0, 7), Bishop("black", 1, 7), Knight("black", 2, 7),
         Queen("black", 3, 7), King("black", 4, 7), Knight("black", 5, 7),
         Bishop("black", 6, 7), Rook("black", 7, 7)]
        #pawns
        for i in range(8):
            self.board[6][i] = Pawn("black", i, 6)