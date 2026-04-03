from generation.Maze import Maze
import random


class Cell:
    def __init__(self):
        self.north = True
        self.east = True
        self.south = True
        self.west = True
        self.visited = False


class MazeGenerator:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.grid = maze.grid
        self.width = maze.width
        self.height = maze.height
        self.entry = maze.entry

    def get_unvisited_neighbors(self, row, col):
        neighbors = []

        if row > 0 and not self.grid[row - 1][col].visited:
            neighbors.append((row - 1, col, "N"))

        if row < self.height - 1 and not self.grid[row + 1][col].visited:
            neighbors.append((row + 1, col, "S"))

        if col > 0 and not self.grid[row][col - 1].visited:
            neighbors.append((row, col - 1, "W"))

        if col < self.width - 1 and not self.grid[row][col + 1].visited:
            neighbors.append((row, col + 1, "E"))

        return neighbors

    def generate_maze(self):
        stack = [self.entry]
        path = [self.entry]

        row, col = self.entry
        self.grid[row][col].visited = True

        while stack:
            row, col = stack[-1]
            neighbors = self.get_unvisited_neighbors(row, col)

            if neighbors:
                if self.perfect.lower() == "true":
                    random.seed(self.seed)
                else:
                    nx, ny, direction = random.choice(neighbors)

                if direction == "N":
                    self.grid[row][col].north = False
                    self.grid[nx][ny].south = False
                elif direction == "S":
                    self.grid[row][col].south = False
                    self.grid[nx][ny].north = False
                elif direction == "E":
                    self.grid[row][col].east = False
                    self.grid[nx][ny].west = False
                elif direction == "W":
                    self.grid[row][col].west = False
                    self.grid[nx][ny].east = False

                self.grid[nx][ny].visited = True
                stack.append((nx, ny))
                path.append((nx, ny))
            else:
                stack.pop()

        return path
