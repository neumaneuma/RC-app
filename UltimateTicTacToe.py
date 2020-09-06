from typing import List
from UserInput import *
from BoardUI import *

COORDINATE_ADJUSTMENTS = {0: (0, 0), 1: (0, 4), 2: (0, 8), 3: (4, 0), 4: (4, 4), 5: (4, 8), 6: (8, 0), 7: (8, 4), 8: (8, 8)}
SPACE_INDEX_TO_COORDINATE = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 1), 5: (1, 2), 6: (2, 0), 7: (2, 1), 8: (2, 2)}

EMPTY_TIC_TAC_TOE_BOARD = [0] * 9
EMPTY_ULTIMATE_TIC_TAC_TOE_BOARD = [EMPTY_TIC_TAC_TOE_BOARD for _ in range(9)]
# BLANK_ROW = ["x", "|", "x", "|", "x", " ", "|", " ", "x", "|", "x", "|", "x", " ", "|", " ", "x", "|", "x", "|", "x"]
# BLANK_ROW = [" ", "|", " ", "|", " ", " ", "|", " ", " ", "|", " ", "|", " ", " ", "|", " ", " ", "|", " ", "|", " "]
# BLANK_UI = [BLANK_ROW for _ in range(9)]

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

    return [
        rowWithPipes, 
        rowWithDashes, 
        rowWithPipes, 
        rowWithDashes, 
        rowWithPipes, 
        rowWithSpaces, 
        borderRow, 
        rowWithPipes, 
        rowWithDashes, 
        rowWithPipes, 
        rowWithDashes, 
        rowWithPipes, 
        rowWithSpaces, 
        borderRow, 
        rowWithPipes, 
        rowWithDashes, 
        rowWithPipes, 
        rowWithDashes, 
        rowWithPipes, 
        rowWithSpaces, 
    ]


def clearSpaceOnBigBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    for r in range(0, 5):
        for c in range(0, 5):
            uiRows[r + rowOffset][c + columnOffset] = " "

def initializeXBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    clearSpaceOnBigBoard(uiRows, rowOffset, columnOffset)
    # for r in range(0, 5):
    #     for c in range(0, 5):
    #         if r != c: continue
    #         uiRows[r + rowOffset][c + columnOffset] = "x"
    # uiRows[0 + rowOffset][4 + columnOffset] = "x"
    # uiRows[4 + rowOffset][0 + columnOffset] = "x"
    # uiRows[1 + rowOffset][3 + columnOffset] = "x"
    # uiRows[3 + rowOffset][1 + columnOffset] = "x"




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