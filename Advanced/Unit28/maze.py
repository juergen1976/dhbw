import heapq
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.height, self.width = maze.shape

    class Node:
        def __init__(self, pos, cost, heuristic):
            self.pos = pos
            self.cost = cost
            self.heuristic = heuristic

        def total_cost(self):
            return self.cost + self.heuristic

    def manhattan_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def heuristic(self, node):
        goal = (self.height-1, self.width-1)
        return self.manhattan_distance(node.pos, goal)

    def get_neighbors(self, pos):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = pos[0] + dr, pos[1] + dc
            if 0 <= r < self.height and 0 <= c < self.width and self.maze[r][c] == 0:
                neighbors.append((r, c))
        return neighbors

    def search(self):
        start = (0, 0)
        goal = (self.height-1, self.width-1)

        frontier = []
        heapq.heappush(frontier, self.Node(start, 0, self.heuristic(self.Node(start, 0, 0))))

        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:
            current = heapq.heappop(frontier).pos

            if current == goal:
                break

            for neighbor in self.get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(self.Node(neighbor, new_cost, 0))
                    heapq.heappush(frontier, self.Node(neighbor, new_cost, priority))
                    came_from[neighbor] = current

        return came_from, cost_so_far

def visualize(maze, came_from, cost_so_far):
    plt.figure(figsize=(8, 6))
    plt.imshow(maze, cmap='binary', interpolation='nearest')

    start = (0, 0)
    goal = (len(maze)-1, len(maze[0])-1)

    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path = path[::-1]

    for r, c in path:
        maze[r][c] = 2

    plt.scatter([c for r, c in path], [r for r, c in path], color='red')
    plt.scatter(goal[1], goal[0], color='green')
    plt.show()

if __name__ == '__main__':
    maze = np.array([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ], dtype=int)

    solver = MazeSolver(maze)
    came_from, cost_so_far = solver.search()
    visualize(maze, came_from, cost_so_far)