def is_valid(board, row, col):
    # TODO: Implement the is_valid function
    pass

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
    # TODO: Implement the print_board function
    pass


solution = n_queens(4)
print (solution)
print_board(solution[0])