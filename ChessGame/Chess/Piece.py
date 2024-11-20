 # parent
class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
   
    def validMoves(self, board, x, y, updateThreat=False):
        print("need to have option to generate possible moves")

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False
        self.canPromote = False
   
    def validMoves(self, board, x, y, updateThreat=False):
        board.clearValid()
#TODO: Need to implement en passant by keeping track of last move, and if the last move by opponent
#was 2 square move. Handle last move in controller. 
        if self.color == "white":
            if self.moved == False:
                #able to move 2 squares
                possibleMoves = [
                    (x, y + 1), (x, y + 2),
                    (x - 1, y + 1), (x + 1, y + 1)
                ]
            else:
                possibleMoves = [
                    (x, y + 1), (x - 1, y + 1),
                    (x + 1, y + 1)
                ]
        else:
            if self.moved == False:
                possibleMoves = [
                    (x, y - 1), (x, y - 2),
                    (x - 1, y - 1), (x + 1, y - 1)
                ]
            else:
                possibleMoves = [
                    (x, y - 1), (x - 1, y - 1),
                    (x + 1, y - 1)
                ]
        for (newX, newY) in possibleMoves:
            #update threat flag map setting. 
            if (updateThreat):
                if self.color == "white":
                    curMap = board.whiteThreat
                else:
                    curMap = board.blackThreat
            #making sure moves within board limits
            if newX < 8 and newX >= 0 and newY < 8 and newY >= 0:
                if updateThreat:
                    if x != newX:
                        #adding new threats if threatflag set
                        curMap[f"{newX}{newY}"][0] += 1
                        curMap[f"{newX}{newY}"].append(self)

                    continue
                 #able to capture    
                elif x != newX and board.hasPiece(newX, newY) != None and board.hasPiece(newX, newY).color != self.color:
                    board.addToValid(newX, newY)

                #check if able to do a double move(no piece in between)       
                elif x == newX and abs(newY - y) == 2:
                    if self.color == "white":
                        if board.hasPiece(newX, y + 1) == None:
                            board.addToValid(newX, newY)
                    else:
                        if board.hasPiece(newX, y - 1) == None:
                            board.addToValid(newX, newY)

                #forward move
                elif x == newX and board.hasPiece(newX, newY) == None:
                    board.addToValid(newX, newY)
    #Call this on the spot you want to remove pawn threats from,
    #Call valid moves with threaten flag to reupdate threats at new location
    def removeThreats(self, board, x,  y):
        if self.color == "white":
            curMap = board.whiteThreat
            removing = [
                (x - 1, y + 1),
                (x + 1, y + 1)
            ]
        else:
            curMap = board.blackThreat
            removing = [
                (x - 1, y - 1),
                (x + 1, y - 1)
            ]
        for (newX, newY) in removing:
            #making sure moves within board limits
            if newX < 8 and newX >= 0 and newY < 8 and newY >= 0:
                curMap[f"{newX}{newY}"].remove(self)
                curMap[f"{newX}{newY}"][0] -= 1

            
    def promote(self):
        self.canPromote = True


       
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False


    def validMoves(self, board, x, y, updateThreat=False):
        print("placeholder")
        possibleMoves = [
            (x + 1, y), (x + 1, y + 1), (x, y + 1),
            (x - 1, y + 1), (x - 1, y), (x - 1, y - 1),
            (x, y - 1), (x + 1, y - 1)
        ]
        if (updateThreat):
            if self.color == "white":
                curMap = board.whiteThreat
            else:
                curMap = board.blackThreat
        for (newX, newY) in possibleMoves:
            #making sure moves within board limits
            #TODO: not checking whether move would put in check yet.
            if newX < 8 and newX >= 0 and newY < 8 and newY >= 0:
                if updateThreat:
                    curMap[f"{newX}{newY}"][0] += 1
                    curMap[f"{newX}{newY}"].append(self)
                elif board.hasPiece(newX, newY) == None or board.hasPiece(newX, newY).color != self.color:
                    board.addToValid(newX, newY)

    def removeThreats(self, board, x,  y):
        if self.color == "white":
            curMap = board.whiteThreat
        else:
            curMap = board.blackThreat
        removing = [
            (x + 1, y), (x + 1, y + 1), (x, y + 1),
            (x - 1, y + 1), (x - 1, y), (x - 1, y - 1),
            (x, y - 1), (x + 1, y - 1)
        ]
        for (newX, newY) in removing:
            #making sure moves within board limits
            if newX < 8 and newX >= 0 and newY < 8 and newY >= 0:
                curMap[f"{newX}{newY}"].remove(self)
                curMap[f"{newX}{newY}"][0] -= 1


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


    def validMoves(self, board, x, y, updateThreat=False):
        board.clearValid()
        
        if (updateThreat):
            if self.color == "white":
                curMap = board.whiteThreat
            else:
                curMap = board.blackThreat
        #going right
        for i in range(1, 8 - x):
            if updateThreat:
                curMap[f"{x + i}{y}"][0] += 1
                curMap[f"{x + i}{y}"].append(self)
                if board.hasPiece(x + i, y):
                    break
            elif board.hasPiece(x + i, y):
                if board.hasPiece(x + i, y).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y).color == self.color
                    break
            else:
                board.addToValid(x + i, y)

        #going left
        for i in range(1, x + 1):
            if updateThreat:
                curMap[f"{x - i}{y}"][0] += 1
                curMap[f"{x - i}{y}"].append(self)
                if board.hasPiece(x - i, y):
                    break
            elif board.hasPiece(x - i, y):
                if board.hasPiece(x - i, y).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y).color == self.color
                    break
            else:
                board.addToValid(x - i, y)

        #going up
        for i in range(1, y):
            if updateThreat:
                curMap[f"{x}{y + i}"][0] += 1
                curMap[f"{x}{y + i}"].append(self)
                if board.hasPiece(x, y + i):
                    break
            elif board.hasPiece(x, y + i):
                if board.hasPiece(x, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x, y + i)
                    break
            else:
                board.addToValid(x, y + i)

        #going down
        for i in range(1, 8 - y):
            if updateThreat:
                curMap[f"{x}{y - i}"][0] += 1
                curMap[f"{x}{y - i}"].append(self)
                if board.hasPiece(x, y - i):
                    break
            elif board.hasPiece(x, y - i):
                if board.hasPiece(x, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x, y - i)
                    break
            else:
                board.addToValid(x, y - i)

        #going top right
        for i in range(1, min(8 - x, 8 - y)):
            if updateThreat:
                curMap[f"{x + i}{y + i}"][0] += 1
                curMap[f"{x + i}{y + i}"].append(self)
                if board.hasPiece(x + i, y + i):
                    break
            elif board.hasPiece(x + i, y + i):
                if board.hasPiece(x + i, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y + i)
                    break
            else:
                board.addToValid(x + i, y + i)
        #going top left
        for i in range(1, min(x, 8 - y)):
            if updateThreat:
                curMap[f"{x - i}{y + i}"][0] += 1
                curMap[f"{x - i}{y + i}"].append(self)
                if board.hasPiece(x - i, y + i):
                    break
            if board.hasPiece(x - i, y + i):
                if board.hasPiece(x - i, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y + i)
                    break
            else:
                board.addToValid(x - i, y + i)


        #going bottom right
        for i in range(1, min(8 - x, y)):
            if updateThreat:
                curMap[f"{x + i}{y - i}"][0] += 1
                curMap[f"{x + i}{y - i}"].append(self)
                if board.hasPiece(x + i, y - i):
                    break
            elif board.hasPiece(x + i, y - i):
                if board.hasPiece(x + i, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y - i)
                    break
            else:
                board.addToValid(x + i, y - i)


        #going bottom left
        for i in range(1, min(x, y)):
            if updateThreat:
                curMap[f"{x - i}{y - i}"][0] += 1
                curMap[f"{x - i}{y - i}"].append(self)
                if board.hasPiece(x - i, y - i):
                    break
            elif board.hasPiece(x - i, y - i):
                if board.hasPiece(x - i, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y - i)
                    break
            else:
                board.addToValid(x - i, y - i)

    def removeThreats(self, board, x, y):
        if self.color == "white":
            curMap = board.whiteThreat
        else:
            curMap = board.blackThreat               
        #going right
        for i in range(1, 8 - x):
            if self in curMap[f"{x + i}{y}"]:
                curMap[f"{x + i}{y}"].remove(self)
                curMap[f"{x + i}{y}"][0] -= 1

        #going left
        for i in range(1, x + 1):
            if self in curMap[f"{x - i}{y}"]:
                curMap[f"{x - i}{y}"].remove(self)
                curMap[f"{x - i}{y}"][0] -= 1

        #going up
        for i in range(1, 8 - y):
            if self in curMap[f"{x}{y + i}"]:
                curMap[f"{x}{y + i}"].remove(self)
                curMap[f"{x}{y + i}"][0] -= 1

        #going down
        for i in range(1, y + 1):
            if self in curMap[f"{x}{y - i}"]:
                curMap[f"{x}{y - i}"].remove(self)
                curMap[f"{x}{y - i}"][0] -= 1

        #going top right
        for i in range(1, min(8 - x, 8 - y)):
            if self in curMap[f"{x + i}{y + i}"]:
                curMap[f"{x + i}{y + i}"].remove(self)
                curMap[f"{x + i}{y + i}"][0] -= 1


        #going top left
        for i in range(1, min(x, 8 - y)):
            if self in curMap[f"{x - i}{y + i}"]:
                curMap[f"{x - i}{y + i}"].remove(self)
                curMap[f"{x - i}{y + i}"][0] -= 1


        #going bottom right
        for i in range(1, min(8 - x, y)):
            if self in curMap[f"{x + i}{y - i}"]:
                curMap[f"{x + i}{y - i}"].remove(self)
                curMap[f"{x + i}{y - i}"][0] -= 1


        #going bottom left
        for i in range(1, min(x, y)):
            if self in curMap[f"{x - i}{y - i}"]:
                curMap[f"{x - i}{y - i}"].remove(self)
                curMap[f"{x - i}{y - i}"][0] -= 1

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def validMoves(self, board, x, y, updateThreat=False):
        board.clearValid()
        possibleMoves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2), 
            (x - 1, y + 2), (x - 1, y - 2)
        ]
        for (newX, newY) in possibleMoves:
            #making sure move is valid
            if newX < 8 and newX >= 0 and newY < 8 and newY >= 0:
                #short circuiting to avoid error
                if board.hasPiece(newX, newY) == None or board.hasPiece(newX, newY).color != self.color:
                    board.addToValid(newX, newY)



class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


    def validMoves(self, board, x, y, updateThreat=False):
        #going to go through the 4 different directions using 4 forloops
        #This is all assuming it's from white players perspective.
        board.clearValid()

        if (updateThreat):
            if self.color == "white":
                curMap = board.whiteThreat
            else:
                curMap = board.blackThreat
        #going top right
        for i in range(1, min(8 - x, 8 - y)):
            if updateThreat:
                curMap[f"{x + i}{y + i}"][0] += 1
                curMap[f"{x + i}{y + i}"].append(self)
            if board.hasPiece(x + i, y + i):
                if board.hasPiece(x + i, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y + i)
                    break
            board.addToValid(x + i, y + i)


        #going top left
        for i in range(1, min(x, 8 - y)):
            if updateThreat:
                curMap[f"{x - i}{y + i}"][0] += 1
                curMap[f"{x - i}{y + i}"].append(self)
            if board.hasPiece(x - i, y + i):
                if board.hasPiece(x - i, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y + i)
                    break
            board.addToValid(x - i, y + i)


        #going bottom right
        for i in range(1, min(8 - x, y)):
            if updateThreat:
                curMap[f"{x + i}{y - i}"][0] += 1
                curMap[f"{x + i}{y - i}"].append(self)
            if board.hasPiece(x + i, y - i):
                if board.hasPiece(x + i, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y - i)
                    break
            board.addToValid(x + i, y - i)


        #going bottom left
        for i in range(1, min(x, y)):
            if updateThreat:
                curMap[f"{x - i}{y - i}"][0] += 1
                curMap[f"{x - i}{y - i}"].append(self)
            if board.hasPiece(x - i, y - i):
                if board.hasPiece(x - i, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y - i)
                    break
            board.addToValid(x - i, y - i)
    def removeThreats(self, board, x, y):
        if self.color == "white":
            curMap = board.whiteThreat
        else:
            curMap = board.blackThreat               

        #going top right
        for i in range(1, min(8 - x, 8 - y)):
            if self in curMap[f"{x + i}{y + i}"]:
                curMap[f"{x + i}{y + i}"].remove(self)
                curMap[f"{x + i}{y + i}"][0] -= 1


        #going top left
        for i in range(1, min(x, 8 - y)):
            if self in curMap[f"{x - i}{y + i}"]:
                curMap[f"{x - i}{y + i}"].remove(self)
                curMap[f"{x - i}{y + i}"][0] -= 1


        #going bottom right
        for i in range(1, min(8 - x, y)):
            if self in curMap[f"{x + i}{y - i}"]:
                curMap[f"{x + i}{y - i}"].remove(self)
                curMap[f"{x + i}{y - i}"][0] -= 1


        #going bottom left
        for i in range(1, min(x, y)):
            if self in curMap[f"{x - i}{y - i}"]:
                curMap[f"{x - i}{y - i}"].remove(self)
                curMap[f"{x - i}{y - i}"][0] -= 1


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False

    def validMoves(self, board, x, y, updateThreat=False):
        board.clearValid()

        if (updateThreat):
            if self.color == "white":
                curMap = board.whiteThreat
            else:
                curMap = board.blackThreat
        #going right
        for i in range(1, 8 - x):
            if updateThreat:
                curMap[f"{x + i}{y}"][0] += 1
                curMap[f"{x + i}{y}"].append(self)
            if board.hasPiece(x + i, y):
                if board.hasPiece(x + i, y).color == self.color:
                    break
                else:
                    board.addToValid(x + i, y).color == self.color
                    break
            board.addToValid(x + i, y)

        #going left
        for i in range(1, x + 1):
            if updateThreat:
                curMap[f"{x - i}{y}"][0] += 1
                curMap[f"{x - i}{y}"].append(self)
            if board.hasPiece(x - i, y):
                if board.hasPiece(x - i, y).color == self.color:
                    break
                else:
                    board.addToValid(x - i, y).color == self.color
                    break
            board.addToValid(x - i, y)

        #going up
        for i in range(1, y):
            if updateThreat:
                curMap[f"{x}{y + i}"][0] += 1
                curMap[f"{x}{y + i}"].append(self)
            if board.hasPiece(x, y + i):
                if board.hasPiece(x, y + i).color == self.color:
                    break
                else:
                    board.addToValid(x, y + i)
                    break
            board.addToValid(x, y + i)

        #going down
        for i in range(1, 8 - y):
            if updateThreat:
                curMap[f"{x}{y - i}"][0] += 1
                curMap[f"{x}{y - i}"].append(self)
            if board.hasPiece(x, y - i):
                if board.hasPiece(x, y - i).color == self.color:
                    break
                else:
                    board.addToValid(x, y - i)
                    break
            board.addToValid(x, y - i)
    def removeThreats(self, board, x, y):
        if self.color == "white":
            curMap = board.whiteThreat
        else:
            curMap = board.blackThreat               
        #going right
        for i in range(1, 8 - x):
            if self in curMap[f"{x + i}{y}"]:
                curMap[f"{x + i}{y}"].remove(self)
                curMap[f"{x + i}{y}"][0] -= 1

        #going left
        for i in range(1, x + 1):
            if self in curMap[f"{x - i}{y}"]:
                curMap[f"{x - i}{y}"].remove(self)
                curMap[f"{x - i}{y}"][0] -= 1

        #going up
        for i in range(1, 8 - y):
            if self in curMap[f"{x}{y + i}"]:
                curMap[f"{x}{y + i}"].remove(self)
                curMap[f"{x}{y + i}"][0] -= 1

        #going down
        for i in range(1, y + 1):
            if self in curMap[f"{x}{y - i}"]:
                curMap[f"{x}{y - i}"].remove(self)
                curMap[f"{x}{y - i}"][0] -= 1


