from Board import Board
from Piece import King, Pawn, Rook
class Controller:
    def __init__(self):
        self.board = Board()
        self.board.reset()
        self.endGame = False
        self.turn = 0
        self.curColor = "white"
        self.curSelect = None

    def startGame(self):
        
        while (not self.endGame):
            self.curColor = "white"
            self.board.printBoard()
            self.promptInput()
            self.board.printBoard()
            self.curColor = "black"
            self.promptInput()
            quit = input("x to quit")
            if quit == "x":
                break

    def promptInput(self):
        while (True):
            try:
                selection = input("Select with xy format: ")
                if  str(selection).isdigit() and len(str(selection)) == 2 :
                    selX = int(selection[0])
                    selY = int(selection[1])
                    if 0 <= selX <= 7 and 0 <= selY <= 7:
                        if self.board.hasPiece(selX, selY) == None:
                            print(f"No piece at ({selX}, {selY})")
                        elif self.board.hasPiece(selX, selY).color is not self.curColor:
                            print("Cannot select opponents pieces, reselect.")
                        else:
                            self.curSelect = self.board.hasPiece(selX, selY)
                            self.board.hasPiece(selX, selY).validMoves(self.board, selX, selY)
                            break
                    else:
                        ("Invalid input, both x and y must be within 0-7")
                else:
                    print("Invalid input, must be in xy format with integers 0-7")
            except ValueError:
                print("Only integers 0-7 allowed")

        while (True):
            try:
                target = input("Select target position with xy format: ")
                if target.isdigit() and len(target) == 2:
                    tarX = int(target[0])
                    tarY = int(target[1])
                    if 0 <= tarX <= 7 and 0 <= tarY <= 7:
                        
                        if (not self.board.withinValid(tarX, tarY)):
                            print("Not a valid position")
                        else:
                            if isinstance(self.board.hasPiece(selX, selY), (King, Pawn, Rook)):
                                self.board.hasPiece(selX, selY).moved = True
                            self.board.board[tarY][tarX] = self.board.hasPiece(selX, selY)
                            self.board.board[selY][selX] = None
                            
                            break
                    else:
                        ("Invalid input, both x and y must be within 0-7")
                else:
                    print("Invalid input, must be in xy format with integers 0-7")
            except ValueError:
                print("Only integers 0-7 allowed")