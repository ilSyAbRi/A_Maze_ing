from generation.Maze import Maze
import random


class MazeGenerator:
    DIRECTIONS: dict[str, tuple] = {'N': (0,-1) , 'S':(0, 1), 'E':(1, 0), 'W':(-1, 0)}
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
    def check_AND_break_direction(maze, row, col, direction, nx, ny):
        
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



    @staticmethod
    def generate_maze(maze):
        stack = [maze.entry]
        path = [maze.entry]

        row, col = maze.entry
        maze.grid[row][col].visited = True

        while stack:
            row, col = stack[-1]
            neighbors = MazeGenerator.get_unvisited_neighbors(maze, row, col)
            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                maze.grid[nx][ny].visited = True
                MazeGenerator.check_AND_break_direction(maze, row, col, direction, nx, ny)
                stack.append((nx, ny))
                path.append((nx, ny))
            else:
                stack.pop()

        if maze.perfect.lower() == "false":
            for x in range(maze.width):
                for y in range(maze.height):
                    maze.grid[x][y].visited = False
            maze.mark_42()
            
            wall_to_break = maze.height * maze.width // 20
            while wall_to_break:
                row_index = random.randint(1, maze.height - 2)
                col_index = random.randint(1, maze.width - 2)


                cell = maze.grid[row_index][col_index]
                if cell.visited:
                    continue
                cell.visited = True
                walls = ['N', 'S', 'E', 'W']
                random.shuffle(walls)
                for wall in walls:
                    # check if there is a wall to break.. If there is at least one break it and return
                    nx, ny = row_index + direction[wall][0], col_index + direction[wall][1]
                    if (not maze.grid[nx][ny].visited and 0 < nx < maze.height and 0 < ny < maze.width):
                        MazeGenerator.check_AND_break_direction(maze, row_index, col_index, wall, nx, ny)
                        wall_to_break -= 1


        return path
