from Cell import Cell
import random
from enum import Enum


class Colors(Enum):
    BLACK =  0xFF000000
    GREEN =  0xff0a9f2c
    PURPLE = 0xFF4a0cde
    YELLOW = 0xFFFFD700
    ORANGE = 0xFFFFA500
    WHITE = 0XFe6dbdfF
    BLUE = 0xff2b6cfb 
    PINK = 0xffcb0cdf


class MazeGenerator:
    def __init__(self, width, height, entry, exit, output_file, seed, perfect):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.seed = seed
        self.perfect = perfect
        self.grid = [[ Cell() for _ in range(width)] for  _ in range(height)]
        self.cell_size = self.calculate_cell_size(width, height)
        self.color = Colors.PINK.value

    @staticmethod
    def calculate_cell_size(width, height):
        adjust_width = 1920 // width 
        adjust_height = 1080 // height
        if (width * height) < 100:
            return min(adjust_width, adjust_height) - 40
        if (width * height) < 1000:
            return min(adjust_width, adjust_height) - 10
        if (width * height) < 5000:
            return min(adjust_width, adjust_height) - 2
        return min(adjust_width, adjust_height)

    def find_42(self):
        center = (self.width // 2, self.height // 2)
        lst4 = [
            (center[0] - 1, center[1]), (center[0] - 2, center[1]), (center[0] - 3, center[1]),
            (center[0] - 3, center[1] - 1), (center[0] - 3, center[1] - 2),
            (center[0] - 1, center[1] + 1), (center[0] -1, center[1] + 2)
        ]
        lst2 = [
            (center[0] + 1, center[1]), (center[0] + 2, center[1]), (center[0] + 3, center[1]),
            (center[0] + 3, center[1] - 1), (center[0] + 3, center[1] - 2), 
            (center[0] + 3, center[1] - 2), 
            (center[0] + 2, center[1] - 2) ,(center[0] + 1, center[1] - 2),
            (center[0] + 1, center[1] + 1), (center[0] + 1, center[1] + 2),
            (center[0] + 2, center[1] + 2) , (center[0] + 3 ,center[1] + 2)
        ]
        return lst4, lst2

    def mark_42(self):
        lst4, lst2 = self.find_42()
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if (x,y) in lst4 or (x,y) in lst2:
                    cell.visited = True

    def get_unvisited_neighbors(self, row, col):
        neighbors = []

        #UP
        if row > 0 and not self.grid[row - 1][col].visited:
            neighbors.append((row - 1, col, "N"))
        #Down
        if row < self.height - 1 and not self.grid[row + 1][col].visited:
            neighbors.append((row + 1, col, "S"))
        #Left
        if col > 0 and not self.grid[row][col - 1].visited:
            neighbors.append((row, col - 1, "W"))
        #Right
        if col < self.width - 1 and not self.grid[row][col + 1].visited:
            neighbors.append((row, col + 1, "E"))

        return neighbors



    def get_right_wall_neighbors(self, row, col):
        neighbors = []

        if row > 0 and self.grid[row][col].north == False:
            neighbors.append((row - 1, col, "N"))

        if row < self.height - 1 and self.grid[row][col].south == False:
            neighbors.append((row + 1, col, "S"))

        if col > 0 and self.grid[row][col].west == False:
            neighbors.append((row, col - 1, "W"))

        if col < self.width - 1 and self.grid[row][col].east == False:
            neighbors.append((row, col + 1, "E"))

        return neighbors


    def return_to_true_mark(self):
        # top row top wall
        for j in range(self.width):
            self.grid[0][j].north = True

        # bottom row bottom wall
        for j in range(self.width):
            self.grid[self.height - 1][j].south = True

        # left column left wall
        for i in range(self.height):
            self.grid[i][0].west = True

        # right column right wall
        for i in range(self.height):
            self.grid[i][self.width - 1].east = True



    def mark_path_for_imperfect(self):

        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].visited = False

        self.mark_42()

        # top row top wall
        for j in range(self.width):
            self.grid[0][j].north = True

        # bottom row bottom wall
        for j in range(self.width):
            self.grid[self.height - 1][j].south = True

        # left column left wall
        for i in range(self.height):
            self.grid[i][0].west = True

        # right column right wall
        for i in range(self.height):
            self.grid[i][self.width - 1].east = True


    def check_cell_and_wall_for_imperfect(self, row, col, next_row, next_col):

        if self.grid[row][col].visited == True:
            return False

        current_north = self.grid[row][col].north
        current_south = self.grid[row][col].south
        current_east = self.grid[row][col].east
        current_west = self.grid[row][col].west

        next_north = self.grid[next_row][next_col].north
        next_south = self.grid[next_row][next_col].south
        next_east = self.grid[next_row][next_col].east
        next_west = self.grid[next_row][next_col].west

        current_walls = [current_north, current_south, current_east, current_west]
        next_walls = [next_north, next_south, next_east, next_west]

        count_current_walls = current_walls.count(True)
        count_next_walls = next_walls.count(True)

        if count_current_walls > 1 and count_next_walls > 1:
            return True
        else:
            return False



    def check_and_break_direction(self, row, col, direction, nx, ny):
        
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



    def generate_maze(self):
        stack = [self.entry]
        path = []

        row, col = self.entry
        self.grid[row][col].visited = True

        if self.seed is not None:
            random.seed(self.seed)

        while stack:
            row, col = stack[-1]
            neighbors = self.get_unvisited_neighbors(row, col)
            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                self.grid[nx][ny].visited = True
                self.check_and_break_direction(row, col, direction, nx, ny)
                stack.append((nx, ny))
                path.append((row, col, direction))
            else:
                stack.pop()

        if self.perfect.lower() == "false":

            self.mark_path_for_imperfect()
            wall_to_break = self.height * self.width // 20
            numberoftry = 10000000000
            while wall_to_break and not numberoftry == 0:
                row = random.randint(0, self.height - 1)
                col = random.randint(0, self.width - 1)
                neighbors = self.get_unvisited_neighbors(row, col)
                if neighbors:
                    nx, ny, direction = random.choice(neighbors)
                    if self.check_cell_and_wall_for_imperfect(row, col, nx, ny):
                        self.check_and_break_direction(row, col, direction, nx, ny)
                        path.append((row, col, direction))
                        wall_to_break -= 1
                numberoftry -=1
            self.return_to_true_mark()

        return path

    """
    1. not visited → ok
    2. mark visited
    3. add to queue
    4. remember how we got there
    """

    def solve_maze(self):
        start = self.entry
        end = self.exit

        queue = [start]
        visited = [start]
        came_from = {}
        path = []

        while queue:
            row, col = queue.pop(0)
            current = (row, col)

            neighbors = self.get_right_wall_neighbors(row, col)

            for nx, ny, direction in neighbors:
                new = (nx, ny)

                if new not in visited:
                    visited.append(new)
                    queue.append(new)
                    came_from[new] = (current, direction)
            if current == end:
                break

        current = end
        while current != start:
            prev, direction = came_from[current]
            path.append((prev[0], prev[1], direction))
            current = prev

        path.reverse()
        return(path)
    

    def from_bool_to_decimal(self, row, col):
        add = 0
        if self.grid[row][col].north:
            add += 0b0001

        if self.grid[row][col].south:
            add += 0b0010

        if self.grid[row][col].east:
            add += 0b0100

        if self.grid[row][col].west:
            add += 0b1000

        return add

    def generate_output_file(self, path):
        try:
            with open(self.output_file, "w") as f:

                for i in range(self.height):
                    line = ""
                    for j in range(self.width):
                        value = self.from_bool_to_decimal(i, j)
                        line += format(value, "X")
                    f.write(line + "\n")

                f.write("\n")

                f.write(f"{self.entry[0]}, {self.entry[1]}\n")
                f.write(f"{self.exit[0]}, {self.exit[1]}\n")

                path_str = ""
                for _, _, direction in path:
                    path_str += direction
                f.write(path_str + "\n")

        except Exception as e:
            print("generation file", e)
            sys.exit(1)
