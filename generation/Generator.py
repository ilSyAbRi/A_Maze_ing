from generation.Maze import Maze
import random


class MazeGenerator:
    @staticmethod
    def get_unvisited_neighbors(maze, row, col):
        neighbors = []

        if row > 0 and not maze.grid[row - 1][col].visited:
            neighbors.append((row - 1, col, "N"))

        if row < maze.height - 1 and not maze.grid[row + 1][col].visited:
            neighbors.append((row + 1, col, "S"))

        if col > 0 and not maze.grid[row][col - 1].visited:
            neighbors.append((row, col - 1, "W"))

        if col < maze.width - 1 and not maze.grid[row][col + 1].visited:
            neighbors.append((row, col + 1, "E"))

        return neighbors

    @staticmethod
    def generate_maze(maze):
        stack = [maze.entry]
        path = [maze.entry]

        row, col = maze.entry 
        maze.grid[row][col].visited = True
        #seed_value = maze.seed()
        #if seed_value is not None:
            #random.seed(seed_value)
        while stack:
            row, col = stack[-1]
            neighbors = MazeGenerator.get_unvisited_neighbors(maze,row, col)
            if neighbors:

                nx, ny, direction = random.choice(neighbors)
                maze.grid[nx][ny].visited = True

                if direction == "N":
                    maze.grid[row][col].north = False
                    maze.grid[nx][ny].south = False
                elif direction == "S":
                    maze.grid[row][col].south = False
                    maze.grid[nx][ny].north = False
                elif direction == "E":
                    maze.grid[row][col].east = False
                    maze.grid[nx][ny].west = False
                elif direction == "W":
                    maze.grid[row][col].west = False
                    maze.grid[nx][ny].east = False

                stack.append((nx, ny))
                path.append((nx, ny))
            else:
                stack.pop()

        return path
