from Piece import Rook, Bishop, Knight, Queen, King, Pawn


class Board:
    def __init__(self):
        self.board = []
        self.validMoves = []
        self.kingValids = []
        self.whiteThreat = {}
        self.blackThreat = {}

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
        
        #initializing threatMap for both white and black.
        #white(map of all tiles white is threatening(even friendly tiles))
        #DO NOT want to call update remove on every piece here so to save
        #on computation, so will manually intialize threatMap
        self.whiteThreat = {
            #back row
            '00' : [0],
            '10' : [1, self.board[0][0]], #rook protecting
            '20' : [1, self.board[0][3]], #king protecting
            '30' : [1, self.board[0][4]], #queen protecting
            '40' : [1, self.board[0][3]], #king protecting
            '50' : [1, self.board[0][4]], #queen protecting
            '60' : [1, self.board[0][7]], #rook protecting
            '70' : [0],
            #pawn row
            '01' : [1, self.board[0][0]], #rook protecting
            '11' : [1, self.board[0][2]], #bishop protecting
            '21' : [1, self.board[0][3]], #king protecting
            '31' : [4, self.board[0][1], self.board[0][2], self.board[0][3], self.board[0][4]], #knight, bishop, king, queen protecting
            '41' : [4, self.board[0][3], self.board[0][4], self.board[0][5], self.board[0][6]], #knight, bishop, king, queen protecting
            '51' : [1, self.board[0][4]], #queen protecting
            '61' : [1, self.board[0][6]], #bishop protecting
            '71' : [1, self.board[0][7]], # rook protecting

            #row above pawns
            '02' : [2, self.board[1][1], self.board[0][1]], #knight, pawn
            '12' : [2, self.board[1][0], self.board[1][2]], #pawn, pawn
            '22' : [3, self.board[0][1], self.board[1][1], self.board[1][3]], #knight, pawn, pawn
            '32' : [2, self.board[1][2], self.board[1][4]], #pawn, pawn
            '42' : [2, self.board[1][3], self.board[1][5]], #pawn, pawn
            '52' : [3, self.board[0][6], self.board[1][4], self.board[1][6]], #knight, pawn, pawn
            '62' : [2, self.board[1][5], self.board[1][7]], #knight pawn
            '72' : [2, self.board[0][6], self.board[1][6]], #pawn pawn
            #enemy side
            '07' : [0], '17' : [0],'27' : [0],'37' : [0],'47' : [0],'57' : [0],'67' : [0],'77' : [0],
            '06' : [0], '16' : [0],'26' : [0],'36' : [0],'46' : [0],'56' : [0],'66' : [0],'76' : [0],
            '05' : [0], '15' : [0],'25' : [0],'35' : [0],'45' : [0],'55' : [0],'65' : [0],'75' : [0],
            #inbetween empty threat tiles
            '03' : [0], '13' : [0],'23' : [0],'33' : [0],'43' : [0],'53' : [0],'63' : [0],'73' : [0],
            '04' : [0], '14' : [0],'24' : [0],'34' : [0],'44' : [0],'54' : [0],'64' : [0],'74' : [0]
        }
        self.blackThreat = {
            '07' : [0],
            '17' : [1, self.board[7][0]], #rook protecting
            '27' : [1, self.board[7][3]], #king protecting
            '37' : [1, self.board[7][4]], #queen protecting
            '47' : [1, self.board[7][3]], #king protecting
            '57' : [1, self.board[7][4]], #queen protecting
            '67' : [1, self.board[7][7]], #rook protecting
            '77' : [0],
            #pawn row
            '06' : [1, self.board[7][0]], #rook protecting
            '16' : [1, self.board[7][2]], #bishop protecting
            '26' : [1, self.board[7][3]], #king protecting
            '36' : [4, self.board[7][1], self.board[7][2], self.board[7][3], self.board[7][4]], #knight, bishop, king, queen protecting
            '46' : [4, self.board[7][3], self.board[7][4], self.board[7][5], self.board[7][6]], #knight, bishop, king, queen protecting
            '56' : [1, self.board[7][4]], #queen protecting
            '66' : [1, self.board[7][6]], #bishop protecting
            '76' : [1, self.board[7][7]], # rook protecting

            #front of pawn row
            '05' : [2, self.board[6][1], self.board[7][1]], #knight, pawn
            '15' : [2, self.board[6][0], self.board[6][2]], #pawn, pawn
            '25' : [3, self.board[7][1], self.board[6][1], self.board[6][3]], #knight, pawn, pawn
            '35' : [2, self.board[6][2], self.board[6][4]], #pawn, pawn
            '45' : [2, self.board[6][3], self.board[6][5]], #pawn, pawn
            '55' : [3, self.board[7][6], self.board[6][4], self.board[6][6]], #knight, pawn, pawn
            '65' : [2, self.board[6][5], self.board[6][7]], #knight pawn
            '75' : [2, self.board[7][6], self.board[6][6]], #pawn pawn
            #enemy side
            '00' : [0], '10' : [0],'20' : [0],'30' : [0],'40' : [0],'50' : [0],'60' : [0],'70' : [0],
            '01' : [0], '11' : [0],'21' : [0],'31' : [0],'41' : [0],'51' : [0],'61' : [0],'71' : [0],
            '02' : [0], '12' : [0],'22' : [0],'32' : [0],'42' : [0],'52' : [0],'62' : [0],'72' : [0],
            #inbetween empty threat tiles
            '03' : [0], '13' : [0],'23' : [0],'33' : [0],'43' : [0],'53' : [0],'63' : [0],'73' : [0],
            '04' : [0], '14' : [0],'24' : [0],'34' : [0],'44' : [0],'54' : [0],'64' : [0],'74' : [0]
        }
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
    
    def printThreats(self, color):
        if color == "white":
            curMap = self.whiteThreat
        else:
            curMap = self.blackThreat
        for i in range(7, -1, -1):
            for j in range(8):
                print(curMap.get(f"{j}{i}")[0], end ="  ")
            print()