import time
import UserInput
import BoardUI

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


def playGame(board, p1, p2, uiRows):
    userSelectsSpaceOnBigBoard = True
    currPlayer = p1

    while True:
        if userSelectsSpaceOnBigBoard: bigBoardSpace = UserInput.prompForBigBoardSpace(board.bigBoard, currPlayer)
        miniBoardSpace = UserInput.prompForMiniBoardSpace(board.miniBoards[bigBoardSpace], currPlayer, bigBoardSpace)
        performMiniBoardMove(board, p1, p2, uiRows, bigBoardSpace, miniBoardSpace, currPlayer)
        if isThreeInARow(board.miniBoards[bigBoardSpace], currPlayer.winThreshold):
            printDelayedMessage("Three in a row!")
            performBigBoardMove(board, p1, p2, uiRows, bigBoardSpace, currPlayer)
            if isThreeInARow(board.bigBoard, currPlayer.winThreshold):
                printDelayedMessage(f"{currPlayer.name} wins!")
                return

        currPlayer = p1 if not currPlayer.isP1 else p2
        bigBoardSpace = miniBoardSpace
        bigBoardSpaceAlreadyOccupied = board.bigBoard[bigBoardSpace] > 0
        userSelectsSpaceOnBigBoard = bigBoardSpaceAlreadyOccupied
        if bigBoardSpaceAlreadyOccupied:
            printDelayedMessage("The big board space that you are forced to play in is already complete. Choose any unfinished big board space you want to play in.")

def isThreeInARow(board, winThreshold):
    threeInARowList = [(0, 1, 2), (0, 3, 6), (6, 7, 8), (2, 5, 8), (0, 4, 8), (2, 4, 6), (3, 4, 5), (1, 4, 7)]
    for x, y, z in threeInARowList:
        if board[x] + board[y] + board[z] == winThreshold: return True
    return False

def printDelayedMessage(message):
    time.sleep(1)
    print(f"\n{message}\n")
    time.sleep(5)

# These methods may seem like they're doing too much based on the number of parameters they have, but I wanted to ensure that a move (changing the backing data structure, setting the UI, and printing it out to the screen) could be done all in one method to ensure that a step wouldn't be forgotten
def performMiniBoardMove(board, p1, p2, uiRows, bigBoardSpace, miniBoardSpace, currPlayer):
    board.miniBoards[bigBoardSpace][miniBoardSpace] = currPlayer.moveValue
    BoardUI.setBoardUI(board, p1, p2, uiRows, bigBoardSpace)
    BoardUI.drawBoard(uiRows)

def performBigBoardMove(board, p1, p2, uiRows, bigBoardSpace, currPlayer):
    board.bigBoard[bigBoardSpace] = currPlayer.moveValue
    BoardUI.setBoardUI(board, p1, p2, uiRows, bigBoardSpace)
    BoardUI.drawBoard(uiRows)


if __name__ == "__main__":
    p1Name = UserInput.promptForName(isP1=True)
    p2Name = UserInput.promptForName(isP1=False)
    p1Character = UserInput.promptForCharacter(p1Name)
    if p1Character == "x":
        p1Draw = BoardUI.setXBoard
        p2Character = "o"
        p2Draw = BoardUI.setOBoard
    else:
        p1Draw = BoardUI.setOBoard
        p2Character = "x"
        p2Draw = BoardUI.setXBoard

    p1 = Player(p1Draw, p1Name, p1Character, isP1=True)
    p2 = Player(p2Draw, p2Name, p2Character, isP1=False)
    board = Board()
    uiRows = BoardUI.initializeEmptyUI()

    while True:
        playGame(board, p1, p2, uiRows)
        if not UserInput.promptToPlayAgain(): break