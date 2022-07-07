# DAMAVIS SNAKE CHALLENGE by Francisco Munoz Gomez
from snake import numberOfAvailableDifferentPaths

if __name__ == "__main__":
    option = -1
    while(int(option) != 0):
        print("\nSNAKE CALCULATOR by Francisco Munoz Gomez\n\n")
        print("MENU (input the option number): \n")
        print("1. Acceptance tests.\n")
        print("2. Custom test.\n")
        print("0. Exit")
        option = input("\n")

        if int(option) == 1:
            print("\nTest 1:\n")
            numberOfAvailableDifferentPaths([4, 3], [[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]],3)
            print("\nTest 2:\n")
            numberOfAvailableDifferentPaths([2, 3], [[0,2],[0,1],[0,0],[1,0],[1,1],[1,2]],10)
            print("\nTest 3:\n")
            numberOfAvailableDifferentPaths([10, 10], [[5,5],[5,4],[4,4],[4,5]],4)
            option = -1 
        if int(option) == 2:
            print("RESPECT THE INSTRUCTIONS, MAXIMUS AND MINIMUS FOR GETTING A CORRECT SOLUTION.")
            print("IF ANY OF THE DATA IS OUT OF BOUNDS, THE CALCULUS WON'T DO AND YOU WILL HAVE TO ENTER ALL DATA AGAIN.")
            board_h = 0
            board_w = 0
            board_w = int(input("\nEnter the width of the board (maximum 10):\n"))
            board_h = int(input("\nEnter the heigth of the board (maximum 10):\n"))
            board = []
            board.append(board_w)
            board.append(board_h)
            
            snakeSize = 0
            snakeSize = int(input("""\nWrite the size of the snake (the size of the snake must be between 3 and 7): \n"""))
            snake = []
            count = 0
            print("Introduce all the cells of the snake one by one, starting with the head:\n")
            while count < snakeSize:
                pos_x = int(input("Introduce cell " + str((count + 1)) + " x coodinate (must be between 0 and the width of the board\n"))
                pos_y = int(input("Introduce cell " + str((count + 1)) + " y coodinate (must be between 0 and the heigth of the board\n"))
                pos = []
                pos.append(pos_x)
                pos.append(pos_y)
                snake.append(pos)
                count = count + 1

            depth = int(input("Enter the path depth (must be between 1 an 20): "))
            numberOfAvailableDifferentPaths(board,snake,depth)
            option = -1 