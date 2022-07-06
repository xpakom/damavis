
def checkValidData(board:list, snake:list, depth:int):
    if len(board) != 2 or 10 < board[0] or board[0] < 0 or 10 < board[1] or board[1] < 0:
        return "The size of the board is out of bounds. Must be between 1 and 10."
    if 3 <= len(snake) <= 7:
        for pos in snake:
            if len(pos) != 2:
                return "The size of at least one of the coordinates of the snake is wrong."
            if 0 > pos[0] or pos[0] > board[0] or 0 > pos[1] or pos[1] > board[1]:
                return "At least one of the coordinates of the snake is out of bounds."
    else:
        return "The snake is too short or too long. Must be between 3 and 7."
    if depth < 1 or depth > 20:
        return "The depth of the path must be between 1 and 20."
    
    return "Checking succesfull. All data is OK."

def numberOfAvailableDifferentPaths(board:list, snake:list, depth:int):
    checking =  checkValidData(board,snake,depth)
    if checking != "Checking succesfull. All data is OK.":
        return checking + "\nRevise the data and retry."

    