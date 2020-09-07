from UserInput import *
from BoardUI import *

EMPTY_TIC_TAC_TOE_BOARD = [0] * 9
EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD = [[0] * 9 for _ in range(9)]

P1_MOVE_VALUE = 1
P2_MOVE_VALUE = 4

class Board:
    def __init__(self):
        self.bigBoard = EMPTY_TIC_TAC_TOE_BOARD
        self.miniBoards = EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD
    
class Player:
    def __init__(self, draw, name, character, isP1):
        self.draw = draw
        self.name = name
        self.character = character
        self.isP1 = isP1
        self.moveValue = P1_MOVE_VALUE if isP1 else P2_MOVE_VALUE
        self.winThreshold = self.moveValue * 3


def playGame(board: Board, p1: Player, p2: Player):
    userSelectsSpaceOnBigBoard = True
    currentPlayer = p1

# These methods may seem like they're doing too much based on the number of parameters they have, but I wanted to ensure that a move (changing the backing data structure, setting the UI, and printing it out to the screen) could be done all in one method to ensure that a step wouldn't be forgotten
def performMiniBoardMove(board, p1, p2, uiRows, bigBoardSpace, miniBoardSpace, currPlayer):
    board.miniBoards[bigBoardSpace][miniBoardSpace] = currPlayer.moveValue
    setBoardUI(board, p1, p2, uiRows, bigBoardSpace)
    drawBoard(uiRows)

def performBigBoardMove(board, p1, p2, uiRows, bigBoardSpace, currPlayer):
    board.bigBoard[bigBoardSpace] = currPlayer.moveValue
    setBoardUI(board, p1, p2, uiRows, bigBoardSpace)
    drawBoard(uiRows)


if __name__ == "__main__":
    # spaceIndex = 8
    # rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[spaceIndex]
    board = Board()
    uiRows = initializeEmptyBoard()
    # setXBoard(uiRows, rowOffset, columnOffset)

    # spaceIndex = 7
    # rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[spaceIndex]

    # setOBoard(uiRows, rowOffset, columnOffset)

    p1 = Player(setXBoard, "", "x", True)
    p2 = Player(setOBoard, "", "o", False)
    currPlayer = p2
    bigBoardSpace = 8

    performBigBoardMove(board, p1, p2, uiRows, bigBoardSpace, currPlayer)

    miniBoardSpace = 4
    bigBoardSpace = 2
    performMiniBoardMove(board, p1, p2, uiRows, bigBoardSpace, miniBoardSpace, currPlayer)

    # m = [0,1,4,0,1,4,0,1,4]
    # spaceIndex = 6
    # rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[spaceIndex]
    # setUnfinishedBoard(uiRows, rowOffset, columnOffset, m, p1, p2)

    # drawBoard(uiRows)




    # while True:
    #     board = Board(bigBoard=EMPTY_TIC_TAC_TOE_BOARD, miniBoards=EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD)
    #     playGame()