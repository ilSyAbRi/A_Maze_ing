from generation.Maze import Maze
import random


class MazeGenerator:
    @staticmethod
    def get_unvisited_neighbors(maze, row, col):
        neighbors = []

        #UP
        if row > 0 and not maze.grid[row - 1][col].visited:
            neighbors.append((row - 1, col, "N"))
        #Down
        if row < maze.height - 1 and not maze.grid[row + 1][col].visited:
            neighbors.append((row + 1, col, "S"))
        #Left
        if col > 0 and not maze.grid[row][col - 1].visited:
            neighbors.append((row, col - 1, "W"))
        #Right
        if col < maze.width - 1 and not maze.grid[row][col + 1].visited:
            neighbors.append((row, col + 1, "E"))

        return neighbors


    @staticmethod
    def get_right_wall_neighbors(maze, row, col):
        neighbors = []

        if row > 0 and maze.grid[row][col].north == False:
            neighbors.append((row - 1, col, "N"))

        if row < maze.height - 1 and maze.grid[row][col].south == False:
            neighbors.append((row + 1, col, "S"))

        if col > 0 and maze.grid[row][col].west == False:
            neighbors.append((row, col - 1, "W"))

        if col < maze.width - 1 and maze.grid[row][col].east == False:
            neighbors.append((row, col + 1, "E"))

        return neighbors

    @staticmethod
    def return_to_true_mark(maze):
        # top row top wall
        for j in range(maze.width):
            maze.grid[0][j].north = False

        # bottom row bottom wall
        for j in range(maze.width):
            maze.grid[maze.height - 1][j].south = False

        # left column left wall
        for i in range(maze.height):
            maze.grid[i][0].west = False

        # right column right wall
        for i in range(maze.height):
            maze.grid[i][maze.width - 1].east = False


    @staticmethod
    def mark_path_for_imperfect(maze):

        for i in range(maze.height):
            for j in range(maze.width):
                maze.grid[i][j].visited = False

        maze.mark_42()

        # top row top wall
        for j in range(maze.width):
            maze.grid[0][j].north = True

        # bottom row bottom wall
        for j in range(maze.width):
            maze.grid[maze.height - 1][j].south = True

        # left column left wall
        for i in range(maze.height):
            maze.grid[i][0].west = True

        # right column right wall
        for i in range(maze.height):
            maze.grid[i][maze.width - 1].east = True

    @staticmethod
    def check_cell_and_wall_for_imperfect(maze, row, col, next_row, next_col):

        if maze.grid[row][col].visited == True:
            return False

        current_north = maze.grid[row][col].north
        current_south = maze.grid[row][col].south
        current_east = maze.grid[row][col].east
        current_west = maze.grid[row][col].west

        next_north = maze.grid[next_row][next_col].north
        next_south = maze.grid[next_row][next_col].south
        next_east = maze.grid[next_row][next_col].east
        next_west = maze.grid[next_row][next_col].west

        current_walls = [current_north, current_south, current_east, current_west]
        next_walls = [next_north, next_south, next_east, next_west]

        count_current_walls = current_walls.count(True)
        count_next_walls = next_walls.count(True)

        if count_current_walls > 1 and count_next_walls > 1:
            return True
        else:
            return False


    @staticmethod
    def check_and_break_direction(maze, row, col, direction, nx, ny):
        
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
        path = []

        row, col = maze.entry
        maze.grid[row][col].visited = True

        if maze.seed is not None:
            random.seed(maze.seed)

        while stack:
            row, col = stack[-1]
            neighbors = MazeGenerator.get_unvisited_neighbors(maze, row, col)
            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                maze.grid[nx][ny].visited = True
                MazeGenerator.check_and_break_direction(maze, row, col, direction, nx, ny)
                stack.append((nx, ny))
                path.append((row, col, direction))
            else:
                stack.pop()

        if maze.perfect.lower() == "false":

            MazeGenerator.mark_path_for_imperfect(maze)
            wall_to_break = maze.height * maze.width // 1
            numberoftry = 10000000000
            while wall_to_break and not numberoftry == 0:
                row = random.randint(0, maze.height - 1)
                col = random.randint(0, maze.width - 1)
                neighbors = MazeGenerator.get_unvisited_neighbors(maze, row, col)
                if neighbors:
                    nx, ny, direction = random.choice(neighbors)
                    if MazeGenerator.check_cell_and_wall_for_imperfect(maze,row, col, nx, ny):
                        MazeGenerator.check_and_break_direction(maze, row, col, direction, nx, ny)
                        path.append((row, col, direction))
                        wall_to_break -= 1
                numberoftry -=1
            MazeGenerator.return_to_true_mark(maze)

        return path

    """
    1. not visited → ok
    2. mark visited
    3. add to queue
    4. remember how we got there
    """
    """
    @staticmethod
    def solve_maze(maze):
        start = maze.entry
        end = maze.exit

        queue = [start]
        visited = [start]
        path = []

        while queue:
            row, col = queue.pop(0)
            current = (row,col)
            neighbors = get_right_wall_neighbors(maze)
            while nx, ny, direction in neighbors:
                new = (nx, ny, direction)
                if new not in visited:
                    visited.append(new)
                    queue.append(new)
                    came_from[new] = (current, direction)
    """
