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


    def is_safe_to_break(maze,row_index,col_index):

        if row_index >= maze.height or col_index >= maze.width:
            return False

        if row_index + 1 >= maze.height or col_index + 1>= maze.width:
            return False

        if row_index -1 >= 0 or col_index -1 >= 0:
            return False

        not_allowed_row , not_allowed_col = maze.find42()

        if row_index in not_allowed_row and col_index in not_allowed_col:
            return False

        if row_index + 1 in not_allowed_row and col_index  in not_allowed_col:
            return False

        if row_index - 1 in not_allowed_row and col_index in not_allowed_col:
            return False

        if row_index in not_allowed_row and col_index +1 in not_allowed_col:
            return False

        if row_index in not_allowed_row and col_index -1 in not_allowed_col:
            return False

        return True

        
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
            wall_to_break = maze.height * maze.widht // 20
            while Wall_to_break:
                row_index = random.randint(0, maze.height - 1)
                col_index = random.randint(0 , maze.widht - 1)

                cell = maze.grid[row_index][col_index]
                walls = [cell.north, cell.south, cell.east, cell.west]

                if is_safe_to_break(maze,row_index, col_index) and walls.count(True) == 3:
                    true_direction = []
                    if cell.north: true_direction.append("N")
                    if cell.south: true_direction.append("S")
                    if cell.east:  true_direction.append("E")
                    if cell.west:  true_direction.append("W")
                    random_wall = random.choice(true_direction)
                    check_AND_break_direction(cell,row,col,random_wall,row +1, col +1)

                    Wall_to_break -= 1

        return path
