from Controller import Controller


def main():
    controller = Controller()
    #Confirm things are running all the way through
    controller.board.printBoard()
    controller.board.board[0][1].validMoves(controller.board, 7, 3)
    print(controller.board.board[0][1])
    controller.board.printValids()
if __name__ == "__main__":
    main()