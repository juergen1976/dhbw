def is_safe(board, row, col):
    # Check if it's possible to place a queen in the current position
    pass

def n_queens(n):
    board = [[False] * n for _ in range(n)]
    solutions = []
    # Try placing queens one by one
    for col in range(n):
        if is_safe(board, 0, col):
            board[0][col] = True
            # Recursively place the remaining queens
            if n > 1:
                for sol in n_queens(n-1):
                    solutions.append([0] + sol)
            else:
                solutions.append([0, col])
            board[0][col] = False # backtrack
    return solutions

n_queens(4)
