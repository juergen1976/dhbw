def solve_maze(maze):
    def is_safe(x, y):
        # Check if (x, y) is within bounds and is an open path
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    def backtrack(x, y, path):
        # Base case: if we reach the bottom-right corner, return True
        if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
            path.append((x, y))
            return True

        # Mark the current cell as part of the path
        path.append((x, y))
        maze[x][y] = -1  # Mark visited

        # Explore all four possible directions: down, right, up, left
        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = x + direction[0], y + direction[1]
            if is_safe(new_x, new_y):
                if backtrack(new_x, new_y, path):
                    return True

        # Backtrack: unmark the current cell and remove it from the path
        path.pop()
        maze[x][y] = 0
        return False

    # Initialize path and start backtracking from the top-left corner
    path = []
    if backtrack(0, 0, path):
        return path
    else:
        return None

# Test the function with an example
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

path = solve_maze(maze)
if path:
    print("Path found:", path)
else:
    print("No path found.")
