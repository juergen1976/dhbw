def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True

def n_queens(n):
    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1] * n)
    return result

def print_board(sol):
    n = len(sol)
    board = [['.' for _ in range(n)] for _ in range(n)]
    # Place queens on the board
    for i, col in enumerate(sol):
        board[i][col] = 'Q'
    # Print out the board
    for row in board:
        print(' '.join(row))


solution = n_queens(4)
print (solution)
print_board(solution[0])