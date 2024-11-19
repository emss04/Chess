from Piece import Rook, Bishop, Knight, Queen, King, Pawn


class Board:
    def __init__(self):
        self.board = []
        self.validMoves = []


    def addToValid(self, x, y):
        self.validMoves.append([x, y])
   
    def clearValid(self):
        self.validMoves.clear()

    def withinValid(self, x, y):
        for i in range(0, len(self.validMoves)):
            if self.validMoves[i][0] == x and self.validMoves[i][1] == y:
                return True
        return False
    #checks if there is piece at x, y, if there is return
    #piece located there,
    #if none return None(null)
    def hasPiece(self, x, y):
        if self.board[y][x] is None:
            return None
        else:
            return self.board[y][x]
   
    def reset(self):
        #Initializing/Resetting board to be able to access positions
        self.board = []
        for i in range(8):
            curRow = []
            for j in range(8):
                curRow.append(None)
            self.board.append(curRow)


        #white side
        self.board[0] = [Rook("white", 0, 0), Knight("white", 1, 0), Bishop("white", 2, 0), 
                        Queen("white", 3, 0), King("white", 4, 0),Bishop("white", 5, 0),
                        Knight("white", 6, 0), Rook("white", 7, 0)]
        #pawns
        for i in range(8):
            self.board[1][i] = Pawn("white", i, 1)  
            
        #black side
        self.board[7] = [Rook("black", 0, 7),Knight("black", 1, 7), Bishop("black", 2, 7), 
         Queen("black", 3, 7), King("black", 4, 7), Bishop("black", 5, 7),
         Knight("black", 6, 7), Rook("black", 7, 7)]
        #pawns
        for i in range(8):
            self.board[6][i] = Pawn("black", i, 6)

    def printBoard(self):
        for i in range(7, -1, -1):
            for j in range(8):
                if isinstance(self.board[i][j], Pawn):
                    if self.board[i][j].color == "white":
                        print("wP", end=" ")
                    else:
                        print("bP", end=" ")
                elif isinstance(self.board[i][j], Knight):
                    if self.board[i][j].color == "white":
                        print("wN", end=" ")
                    else:
                        print("bN", end=" ")
                elif isinstance(self.board[i][j], Bishop):
                    if self.board[i][j].color == "white":
                        print("wB", end=" ")
                    else:
                        print("bB", end=" ")
                elif isinstance(self.board[i][j], Rook):
                    if self.board[i][j].color == "white":
                        print("wR", end=" ")
                    else:
                        print("bR", end=" ")
                elif isinstance(self.board[i][j], King):
                    if self.board[i][j].color == "white":
                        print("wK", end=" ")
                    else:
                        print("bK", end=" ")
                elif isinstance(self.board[i][j], Queen):
                    if self.board[i][j].color == "white":
                        print("wQ", end=" ")
                    else:
                        print("bQ", end=" ")
                else:
                    print("  ", end=" ")
            print(i)
        print("0  1  2  3  4  5  6  7")
    def printValids(self):
        for i in range(0, len(self.validMoves)):
            print(self.validMoves[i])