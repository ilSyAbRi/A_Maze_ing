from generation.Cell import Cell
from generation.Maze import Maze

DIRECTIONS = {
    "N": (-1, 0),  # up
    "E": (0, 1),   # right
    "S": (1, 0),   # down
    "W": (0, -1),  # left
}

OPPOSITE = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E",
}


def get_unvisited_neighbors(self, x, y):
    neighbors = []

    # UP
    if x > 0 and not self.grid[x - 1][y].visited:
        neighbors.append((x - 1, y, "N"))

    # RIGHT
    if y < self.width - 1 and not self.grid[x][y + 1].visited:
        neighbors.append((x, y + 1, "E"))

    # DOWN
    if x < self.height - 1 and not self.grid[x + 1][y].visited:
        neighbors.append((x + 1, y, "S"))

    # LEFT
    if y > 0 and not self.grid[x][y - 1].visited:
        neighbors.append((x, y - 1, "W"))

    return neighbors

def do_dfs_algo(self):
    stack = [self.entry]
