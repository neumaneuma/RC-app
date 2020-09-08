from typing import List

COORDINATE_ADJUSTMENTS = {0: (0, 0), 1: (0, 8), 2: (0, 16), 3: (8, 0), 4: (8, 8), 5: (8, 16), 6: (16, 0), 7: (16, 8), 8: (16, 16)}
SPACE_INDEX_TO_COORDINATE = {0: (0, 0), 1: (0, 2), 2: (0, 4), 3: (2, 0), 4: (2, 2), 5: (2, 4), 6: (4, 0), 7: (4, 2), 8: (4, 4)}

def initializeEmptyUI():
    rowWithPipes = " | |  |  | |  |  | | "
    rowWithDashes = "----- | ----- | -----"
    rowWithSpaces = "      |       |      "
    borderRow = "------|-------|------"
    gen = lambda string: [i for i in string]

    # I use a lambda to generate a different list each time because otherwise every instance of rowWithPipes,
    # for example, would refer to the same list in memory. This would result in every row changing at once instead
    # of just the row selected.
    return [gen(rowWithPipes), gen(rowWithDashes), gen(rowWithPipes), gen(rowWithDashes), gen(rowWithPipes), gen(rowWithSpaces),
    gen(borderRow), gen(rowWithSpaces), gen(rowWithPipes), gen(rowWithDashes), gen(rowWithPipes), gen(rowWithDashes),
    gen(rowWithPipes), gen(rowWithSpaces), gen(borderRow), gen(rowWithSpaces), gen(rowWithPipes), gen(rowWithDashes),
    gen(rowWithPipes), gen(rowWithDashes), gen(rowWithPipes), gen(rowWithSpaces)]

def setUnfinishedBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int, miniBoard: List[int], p1, p2):
    for index, spaceValue in enumerate(miniBoard):
        r, c = SPACE_INDEX_TO_COORDINATE[index]
        if spaceValue == p1.moveValue:
            uiRows[r + rowOffset][c + columnOffset] = p1.character
        elif spaceValue == p2.moveValue:
            uiRows[r + rowOffset][c + columnOffset] = p2.character

def clearSpaceOnBigBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    for r in range(0, 5):
        for c in range(0, 5):
            uiRows[r + rowOffset][c + columnOffset] = " "

def setXBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    clearSpaceOnBigBoard(uiRows, rowOffset, columnOffset)
    for r in range(0, 5):
        for c in range(0, 5):
            if r != c: continue
            uiRows[r + rowOffset][c + columnOffset] = "x"
    uiRows[0 + rowOffset][4 + columnOffset] = "x"
    uiRows[4 + rowOffset][0 + columnOffset] = "x"
    uiRows[1 + rowOffset][3 + columnOffset] = "x"
    uiRows[3 + rowOffset][1 + columnOffset] = "x"

def setOBoard(uiRows: List[List[str]], rowOffset: int, columnOffset: int):
    clearSpaceOnBigBoard(uiRows, rowOffset, columnOffset)
    for r in range(0, 5):
        for c in range(0, 5):
            if r == 0 or c == 0 or r == 4 or c == 4:
                uiRows[r + rowOffset][c + columnOffset] = "o"

def setBoardUI(board, p1, p2, uiRows, bigBoardSpace):
    rowOffset, columnOffset = COORDINATE_ADJUSTMENTS[bigBoardSpace]
    value = board.bigBoard[bigBoardSpace]
    if value == p1.moveValue: p1.draw(uiRows, rowOffset, columnOffset)
    elif value == p2.moveValue: p2.draw(uiRows, rowOffset, columnOffset)
    else: setUnfinishedBoard(uiRows, rowOffset, columnOffset, board.miniBoards[bigBoardSpace], p1, p2)

def drawBoard(uiRows: List[List[str]]):
    print()
    for row in uiRows:
        print("".join(row))
    print()