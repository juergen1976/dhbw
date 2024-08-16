# Pseudo-code for solving Sudoku using backtracking

# A function to check if placing a number in a cell is valid
def is_valid(board, row, col, num):
    # Check if 'num' is not present in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if 'num' is not present in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if 'num' is not present in the current 3x3 sub-grid
    # Find the starting row and column of the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3

    # Traverse the 3x3 grid
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    # If all checks pass, it's valid to place 'num' here
    return True


# A utility function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    # Iterate through the entire board
    for row in range(9):
        for col in range(9):

            # If the cell is empty (represented by 0), try to fill it
            if board[row][col] == 0:

                # Try placing digits from 1 to 9 in the empty cell
                for num in range(1, 10):

                    # Check if placing 'num' in (row, col) is valid
                    if is_valid(board, row, col, num):

                        # If valid, place 'num' in the cell
                        board[row][col] = num

                        # Recursively try to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If the current configuration doesn't lead to a solution,
                        # backtrack by resetting the cell and trying the next number
                        board[row][col] = 0

                # If no valid number can be placed in this cell, backtrack
                return False

    # If the board is completely filled without any conflict, return True (solution found)
    return True


# A helper function to print the Sudoku board (optional, for visualization)
def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


# Sample Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku and print the result
if solve_sudoku(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")
