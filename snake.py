
paths = []

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

def upPos (pos):
    return [pos[0],pos[1] - 1]

def downPos (pos):
    return [pos[0],pos[1]+1]

def rightPos (pos):
    return [pos[0] + 1,pos[1]]

def leftPos (pos):
    return [pos[0] - 1,pos[1]]

def checkCollision(snake:list, nextPos:list):
    if nextPos in snake[:-1]:
        return True
    else:
        return False

def checkOutBounds(board:list, nextPos:list):
    if nextPos[0] < board[0] and nextPos[1] < board[1] and nextPos [0] >= 0 and nextPos[1] >= 0:
        return False
    else:
        return True

def snakeNextPos(snake:list, nextPos:list):
    return [snake[-1]] + nextPos

def createPaths(board:list, snake:list, depth:int, actualPath:list):
    if depth > 0:
        if not checkCollision(board,snake,upPos(snake[0])) and not checkOutBounds(board,upPos(snake[0])):
            snakeUp = snakeNextPos(snake,upPos(snake[0]))
            actualPathUp = actualPath.append(upPos(snake[0]))
            createPaths(board, snakeUp, depth - 1, actualPathUp)
        if not checkCollision(board,snake,downPos(snake[0])) and not checkOutBounds(board,upPos(snake[0])):
            snakeDown = snakeNextPos(snake,downPos(snake[0]))
            actualPathDown = actualPath.append(downPos(snake[0]))
            createPaths(board, snakeDown, depth - 1, actualPathDown)
        if not checkCollision(board,snake,rightPos(snake[0])) and not checkOutBounds(board,upPos(snake[0])):
            snakeRight = snakeNextPos(snake,rightPos(snake[0]))
            actualPathRight = actualPath.append(rightPos(snake[0]))
            createPaths(board, snakeRight, depth - 1, actualPathRight)
        if not checkCollision(board,snake,leftPos(snake[0])) and not checkOutBounds(board,upPos(snake[0])):
            snakeLeft = snakeNextPos(snake,leftPos(snake[0]))
            actualPathLeft = actualPath.append(leftPos(snake[0]))
            createPaths(board, snakeLeft, depth - 1, actualPathLeft)
    else:
        paths.append(actualPath)



def numberOfAvailableDifferentPaths(board:list, snake:list, depth:int):
    checking =  checkValidData(board,snake,depth)
    if checking != "Checking succesfull. All data is OK.":
        return checking + "\nRevise the data and retry."

    createPaths(board, snake, depth, [])
    pathsNumber = len(paths)
    print ("The amount of possible paths is: " + pathsNumber)
    return pathsNumber