from generation.Cell import Cell

class Maze:
    @staticmethod
    def calculate_cell_size(width, height):
        adjust_width = 1920 // width 
        adjust_height = 1080 // height
        if (width * height) < 1000:
            return min(adjust_width, adjust_height) - 10
        if (width * height) < 5000:
            return min(adjust_width, adjust_height) - 2
        return min(adjust_width, adjust_height)
    
    def __init__(self, width, height, entry, exit, output_file, perfect):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.grid = [[ Cell() for _ in range(width)] for  _ in range(height)]
        self.cell_size = Maze.calculate_cell_size(width, height)

    def get_unvisited_neighbors(self, x, y):
        neighbors = []
        # UP
        if x > 0:
            if not self.grid[x - 1][y].visited:
                neighbors.append((x - 1, y, "N"))
        # down
        if x < self.height - 1 :
            if not self.grid[x + 1][y].visited:
                neighbors.append((x + 1, y, "S"))
        # left
        if y > 0:
            if not self.grid[x][y - 1].visited:
                neighbors.append((x, y - 1, "W"))
        # right
        if y < self.width - 1:
            if not self.grid[x][y + 1].visited:
                neighbors.append((x, y + 1, "E"))
        return neighbors

    def do_dfs_algo(self):
        stack = [self.entry]
        path = [self.entry]
        self.grid[self.entry[0]][self.entry[1]].visited = True

        while stack:
            x, y = stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)

            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                if direction == "N":
                    self.grid[x][y].north = False
                    self.grid[nx][ny].south = False
                elif direction == "S":
                    self.grid[x][y].south = False
                    self.grid[nx][ny].north = False
                elif direction == "E":
                    self.grid[x][y].east = False
                    self.grid[nx][ny].west = False
                elif direction == "W":
                    self.grid[x][y].west = False
                    self.grid[nx][ny].east = False

                self.grid[nx][ny].visited = True
                path.append((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

        self.path = path
        return path

