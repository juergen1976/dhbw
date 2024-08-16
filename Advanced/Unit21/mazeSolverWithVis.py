import matplotlib.pyplot as plt
import numpy as np

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

def visualize_maze(maze, path=None):
    n, m = len(maze), len(maze[0])

    # Create a grid visualization (1 for walls, 0 for free path)
    grid = np.array(maze)
    grid[grid == -1] = 0  # Mark visited cells as empty for visualization

    # Plot the maze
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='binary', interpolation='nearest')

    # Add walls (1 = wall, 0 = path)
    ax.set_xticks(np.arange(-.5, m, 1), minor=True)
    ax.set_yticks(np.arange(-.5, n, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.tick_params(which='minor', size=0)

    # Mark the path, if exists
    if path:
        x_coords, y_coords = zip(*path)
        ax.plot(y_coords, x_coords, color='red', linewidth=2, marker='o', markersize=5)

    # Set labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Maze with Path')

    plt.show()

# Example Maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Solve the maze
path = solve_maze(maze)

# Visualize the maze and the path (if found)
visualize_maze(maze, path)
