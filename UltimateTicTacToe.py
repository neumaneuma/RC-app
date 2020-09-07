from UserInput import *
from BoardUI import *

EMPTY_TIC_TAC_TOE_BOARD = [0] * 9
EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD = [EMPTY_TIC_TAC_TOE_BOARD for _ in range(9)]

P1_MOVE_VALUE = 1
P2_MOVE_VALUE = 4

class Board:
    def __init__(self, bigBoard, miniBoards):
        self.bigBoard = bigBoard
        self.miniBoards = miniBoards
    
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

# def updateBoard(board: Board, p1: Player, p2: Player):



if __name__ == "__main__":
    spaceIndex = 8
    rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[spaceIndex]
    uiRows = initializeEmptyBoard()
    setXBoard(uiRows, rowOffset, columnOffset)

    spaceIndex = 7
    rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[spaceIndex]

    setOBoard(uiRows, rowOffset, columnOffset)

    p1 = Player(None, "", "x", True)
    p2 = Player(None, "", "o", False)
    m = [0,1,4,0,1,4,0,1,4]
    spaceIndex = 6
    rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[spaceIndex]
    setUnfinishedBoard(uiRows, rowOffset, columnOffset, m, p1, p2)

    drawBoard(uiRows)




    # while True:
    #     board = Board(bigBoard=EMPTY_TIC_TAC_TOE_BOARD, miniBoards=EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD)
    #     playGame()