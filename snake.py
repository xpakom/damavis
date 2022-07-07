
paths = []
COUNTER = 0

def increment():
    global COUNTER
    COUNTER = COUNTER + 1

def reset():
    global COUNTER
    COUNTER = 0

def checkValidData(board, snake, depth):
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
    print ("Select up")
    u = []
    u.append(pos[0])
    u.append(pos[1] - 1)
    print(u)
    print('\n')
    return u

def downPos (pos):
    print ("Select down")
    d = []
    d.append(pos[0])
    d.append(pos[1] + 1)
    print(d)
    print('\n')
    return d

def rightPos (pos):
    print ("Select right")
    r = []
    r.append(pos[0] + 1)
    r.append(pos[1])
    print(r)
    print('\n')
    return r

def leftPos (pos):
    print ("Select left")
    l = []
    l.append(pos[0] - 1)
    l.append(pos[1])
    print(l)
    print('\n')
    return l

def checkCollision(snake, nextPos):
    if nextPos in snake[:-1]:
        return True
    else:
        return False

def checkOutBounds(board, nextPos):
    if nextPos[0] < board[0] and nextPos[1] < board[1] and nextPos [0] >= 0 and nextPos[1] >= 0:
        return False
    else:
        return True

def snakeNextPos(snake, nextPos):
    snakeNext = []
    snakeNext.append(nextPos)
    for ps in snake[:-1]:
        snakeNext.append(ps)
    return snakeNext

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
            print ("Going up")
            print(snakeUp)
            print(depth - 1)
            print(actualPathUp)
            print('\n')
            createPaths(board, snakeUp, depth - 1, actualPathUp)
        if not checkCollision(snake,d) and not checkOutBounds(board,d):
            snakeDown = snakeNextPos(snake,d)
            actualPathDown = []
            for pt in actualPath:
                actualPathDown.append(pt)
            actualPathDown.append(d)
            print ("Going down")
            print(snakeDown)
            print(depth - 1)
            print(actualPathDown)
            print('\n')
            createPaths(board, snakeDown, depth - 1, actualPathDown)
        if not checkCollision(snake,r) and not checkOutBounds(board,r):
            snakeRight = snakeNextPos(snake,r)
            actualPathRight = []
            for pt in actualPath:
                actualPathRight.append(pt)
            actualPathRight.append(r)
            print ("Going right")
            print(snakeRight)
            print(depth - 1)
            print(actualPathRight)
            print('\n')
            createPaths(board, snakeRight, depth - 1, actualPathRight)
        if not checkCollision(snake,l) and not checkOutBounds(board,l):
            snakeLeft = snakeNextPos(snake,l)
            actualPathLeft = []
            for pt in actualPath:
                actualPathLeft.append(pt)
            actualPathLeft.append(l)
            print ("Going left")
            print(snakeLeft)
            print(depth - 1)
            print(actualPathLeft)
            print('\n')
            createPaths(board, snakeLeft, depth - 1, actualPathLeft)
    else:
        #print (actualPath)
        print("+1")
        print('\n')
        increment()
        if (not actualPath in paths):
            paths.append(actualPath)


def numberOfAvailableDifferentPaths(board, snake, depth):
    checking =  checkValidData(board,snake,depth)
    if checking != "Checking succesfull. All data is OK.":
        return checking + "\nRevise the data and retry."
    
    reset()
    createPaths(board, snake, depth, [])
    pathsNumber = len(paths)
    return pathsNumber