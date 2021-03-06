# DAMAVIS SNAKE CHALLENGE by Francisco Munoz Gomez
import sys
paths = []

# Checks the sizes of the board, snake path and depth to ensure that it conforms 
# to the parameters required in the document.
def checkValidData(board, snake, depth):
    correct = True
    if len(board) != 2 or 10 < board[0] or board[0] < 1 or 10 < board[1] or board[1] < 1:
        print("The size of the board is out of bounds. Must be between 1 and 10.")
        correct = False
    if 3 <= len(snake) <= 7:
        for pos in snake:
            if len(pos) != 2:
                print("The size of at least one of the coordinates of the snake is wrong.")
                correct = False
            if 0 > pos[0] or pos[0] > board[0]-1 or 0 > pos[1] or pos[1] > board[1]-1:
                print("At least one of the coordinates of the snake is out of bounds.")
                correct = False
    else:
        print("The snake is too short or too long. Must be between 3 and 7.")
        correct = False
    if depth < 1 or depth > 20:
        print("The depth of the path must be between 1 and 20.")
        correct = False
    
    if correct:
        print("Checking succesfull. All data is OK.")
    return correct

# Returns the coordinates of the position above from the current position.
def upPos (pos):
    u = []
    u.append(pos[0])
    u.append(pos[1] - 1)
    return u

# Returns the coordinates of the position below from the current position.
def downPos (pos):
    d = []
    d.append(pos[0])
    d.append(pos[1] + 1)
    return d

# Returns the coordinates of the position on the right from the current position.
def rightPos (pos):
    r = []
    r.append(pos[0] + 1)
    r.append(pos[1])
    return r

# Returns the coordinates of the position on the left from the current position.
def leftPos (pos):
    l = []
    l.append(pos[0] - 1)
    l.append(pos[1])
    return l

# Check if the next position matches with any of the snake but the last one (because when it moves, it will avoid 
# collision). In case this happen, we return True to inform that the position is invalid.
def checkCollision(snake, nextPos):
    if nextPos in snake[:-1]:
        return True
    else:
        return False

# Check if the next position goes off the board.
# In case this happen, we return True to inform that the position is invalid.
def checkOutBounds(board, nextPos):
    if nextPos[0] < board[0] and nextPos[1] < board[1] and nextPos [0] >= 0 and nextPos[1] >= 0:
        return False
    else:
        return True

# Change the position of the snake. After then, the head is in the new first position and the rest of the body 
# go on but the tail actual position that disapears of the snake vector.
def snakeNextPos(snake, nextPos):
    snakeNext = []
    snakeNext.append(nextPos)
    for ps in snake[:-1]:
        snakeNext.append(ps)
    return snakeNext

"""Recursive algorithm that runs through all possible routing options, diversifying its calls into 4 movement options.
When a dead end position is reached that forces crashing or exiting the map and there are still steps to take 
(depth > 0), that route is lost. Routes that are successfully completed are stored in a global variable."""
def createPaths(board, snake, depth, actualPath):
    if depth > 0:
        u = upPos(snake[0])
        d = downPos(snake[0])
        r = rightPos(snake[0])
        l = leftPos(snake[0])
        if not checkCollision(snake,u) and not checkOutBounds(board,u):
            snakeUp = snakeNextPos(snake,u)
            actualPathUp = []
            for pt in actualPath:
                actualPathUp.append(pt)
            actualPathUp.append(u)
            createPaths(board, snakeUp, depth - 1, actualPathUp)
        if not checkCollision(snake,d) and not checkOutBounds(board,d):
            snakeDown = snakeNextPos(snake,d)
            actualPathDown = []
            for pt in actualPath:
                actualPathDown.append(pt)
            actualPathDown.append(d)
            createPaths(board, snakeDown, depth - 1, actualPathDown)
        if not checkCollision(snake,r) and not checkOutBounds(board,r):
            snakeRight = snakeNextPos(snake,r)
            actualPathRight = []
            for pt in actualPath:
                actualPathRight.append(pt)
            actualPathRight.append(r)
            createPaths(board, snakeRight, depth - 1, actualPathRight)
        if not checkCollision(snake,l) and not checkOutBounds(board,l):
            snakeLeft = snakeNextPos(snake,l)
            actualPathLeft = []
            for pt in actualPath:
                actualPathLeft.append(pt)
            actualPathLeft.append(l)
            createPaths(board, snakeLeft, depth - 1, actualPathLeft)
    else:
        if (not actualPath in paths):
            paths.append(actualPath)

# Main fuction
def numberOfAvailableDifferentPaths(board, snake, depth):
    # Check if there is any error on data.
    try:
        checking =  checkValidData(board,snake,depth)
        if not checking:
            print("Revise the data and retry.")
    except:
        print("Incorrect data syntax. Please retry.")
    
    # If there is not error, we calculate the possible paths.
    if checking:
        createPaths(board, snake, depth, [])
        pathsNumber = len(paths)
        print("Number of possible paths: " + str(pathsNumber))
        if pathsNumber > 0:
            # If there are paths, we ask the user if wants to show the list of them.
            text = input("Do you want to see the list of possible paths? Press 'y' for yes or any key for no:  ")
            if text == 'y' or text == 'Y':
                for p in paths:
                    print(p)

    # Clean the path list for the next execution
    print('\n\n')
    paths.clear()