from typing import List
from UserInput import *
from BoardUI import *

COORDINATE_ADJUSTMENTS = {0: (0, 0), 1: (0, 8), 2: (0, 16), 3: (8, 0), 4: (8, 8), 5: (8, 16), 6: (16, 0), 7: (16, 8), 8: (16, 16)}
SPACE_INDEX_TO_COORDINATE = {0: (0, 0), 1: (0, 2), 2: (0, 4), 3: (2, 0), 4: (2, 2), 5: (2, 4), 6: (4, 0), 7: (4, 2), 8: (4, 4)}

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

# def initializeUnfinishedBoard(board: Board, p1: Player, p2: Player):
def initializeEmptyBoard():
    rowWithPipes = [i for i in " | |  |  | |  |  | | "]
    rowWithDashes = [i for i in "----- | ----- | -----"]
    rowWithSpaces = [i for i in "      |       |      "]
    borderRow = [i for i in "------|-------|------"]

    # I alter the contents of rowWithPipes and rowWithDashes to show where user played on the screen. However, if I didn’t use copy() then each rowWithPipes in my 2D list would reference the exact same list in memory (same for rowWithDashes), thereby changing each row when I only want to change one row. This seems like an inelegant solution though...
    return [rowWithPipes.copy(), rowWithDashes.copy(), rowWithPipes.copy(), rowWithDashes.copy(), rowWithPipes.copy(), rowWithSpaces, borderRow, rowWithSpaces, rowWithPipes.copy(), rowWithDashes.copy(), rowWithPipes.copy(), rowWithDashes.copy(), rowWithPipes.copy(), rowWithSpaces, borderRow, rowWithSpaces, rowWithPipes.copy(), rowWithDashes.copy(), rowWithPipes.copy(), rowWithDashes.copy(), rowWithPipes.copy(), rowWithSpaces]


def clearSpaceOnBigBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    for r in range(0, 5):
        for c in range(0, 5):
            uiRows[r + rowOffset][c + columnOffset] = " "

def initializeXBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    clearSpaceOnBigBoard(uiRows, rowOffset, columnOffset)
    for r in range(0, 5):
        for c in range(0, 5):
            if r != c: continue
            uiRows[r + rowOffset][c + columnOffset] = "x"
    uiRows[0 + rowOffset][4 + columnOffset] = "x"
    uiRows[4 + rowOffset][0 + columnOffset] = "x"
    uiRows[1 + rowOffset][3 + columnOffset] = "x"
    uiRows[3 + rowOffset][1 + columnOffset] = "x"




# def initializeOBoard(board: Board, p1: Player, p2: Player):

def drawBoard(uiRows: List[List[str]]):
    print()
    for row in uiRows:
        print("".join(row))
    print()


if __name__ == "__main__":
    spaceIndex = 0
    rowOffset, columnOffset = SPACE_INDEX_TO_COORDINATE[spaceIndex]
    uiRows = initializeEmptyBoard()
    initializeXBoard(uiRows, rowOffset, columnOffset)
    drawBoard(uiRows)

    # p1 = Player()
    

    # while True:
    #     board = Board(bigBoard=EMPTY_TIC_TAC_TOE_BOARD, miniBoards=EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD)
    #     playGame()