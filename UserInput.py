import time

def prompForBigBoardSpace(board, currPlayer):
    return promptForSpace(board, "big board", currPlayer.name)

def prompForMiniBoardSpace(board, currPlayer, bigBoardSpace):
    return promptForSpace(board, "mini board", currPlayer.name, f"\nCurrent big space: {bigBoardSpace}\n")

def promptForSpace(board, boardType, currPlayer, bigBoardSpaceMsg="\n"):
    promptMsg = f"0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8\n\n{currPlayer}:{bigBoardSpaceMsg}Select which space in the {boardType} you want to play in:"
    errorMsg1 = "Only 0 through 8 allowed"
    errorMsg2 = "Space is already taken"
    while True:
        val = input(promptMsg).lower()
        if len(val) > 1 or val not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            print(f"\n{errorMsg1}\n")
            time.sleep(1)
            continue
        elif board[int(val)] > 0:
            print(f"\n{errorMsg2}\n")
            time.sleep(1)
            continue
        return int(val)

def promptToPlayAgain():
    promptMsg = "Play again? [y/n]:"
    errorMsg = "Only y or n allowed"
    inputIsInvalid = lambda val: len(val) > 1 or val not in ["y", "n"]
    generateReturnValue = lambda val: True if val == "y" else False
    return makePrompt(promptMsg, errorMsg, inputIsInvalid, generateReturnValue)

def promptForName(isP1):
    defaultName = "Player 1" if isP1 else "Player 2"
    promptMsg = "Enter your name []:"
    errorMsg = "20 character limit"
    inputIsInvalid = lambda val: len(val) > 20
    generateReturnValue = lambda val: val if len(val) > 0 else defaultName
    return makePrompt(promptMsg, errorMsg, inputIsInvalid, generateReturnValue)

def promptForCharacter():
    promptMsg = "Enter your character [x/o]:"
    errorMsg = "Only x or o allowed"
    inputIsInvalid = lambda val: len(val) > 1 or val not in ["x", "o"]
    generateReturnValue = lambda val: val
    return makePrompt(promptMsg, errorMsg, inputIsInvalid, generateReturnValue)

def makePrompt(promptMsg, errorMsg, inputIsInvalid, generateReturnValue):
    while True:
        val = input(promptMsg).lower()
        if inputIsInvalid(val):
            print(f"\n{errorMsg}\n")
            time.sleep(1)
            continue
        return generateReturnValue(val)