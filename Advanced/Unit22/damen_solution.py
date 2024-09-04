def is_valid(board, row, col):
    for i in range(row):
        # 1. ensures that no two queens are placed in the same column.
        # 2. checks both the left and right diagonals. If the difference between columns equals the difference between rows, it means the queens are on the same diagonal.
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def print_board(sol):
    n = len(sol)
    board = [['.' for _ in range(n)] for _ in range(n)]
    # Place queens on the board
    for i, col in enumerate(sol):
        board[i][col] = 'Q'
    # Print out the board
    for row in board:
        print(' '.join(row))

def is_valid2(board, row, col):
    for i in range(row):
        if board[i] == col:  # Same column check
            return False
        if board[i] - col == i - row:  # Same major diagonal check
            return False
        if board[i] - col == row - i:  # Same minor diagonal check
            return False
    return True

def n_queens(n):
    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid2(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1] * n)
    return result




solution = n_queens(5)
print (solution)
print_board(solution[0])