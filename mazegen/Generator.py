from Cell import Cell
import random
import sys
from collections import deque
from enum import Enum

Coordinate = tuple[int, int]
Step = tuple[int, int, str]


class Colors(Enum):
    """Define available RGBA color constants."""
    BLACK = 0xFF000000
    GREEN = 0xFF0CDFA4
    PURPLE = 0xFF4A0CDE
    ORANGE = 0xFFFFA500
    BLUE = 0xFF7fceff
    PINK = 0xFFCB0CDF
    RED = 0xFFDF0C1C
    DARK_BLUE = 0xFF2A3AC7
    WHITE = 0xFFE6E7F1
    YELLOW = 0xFFFFD700


class MazeGenerator:
    """Generate, solve, and export maze data."""

    def __init__(
        self,
        width: int,
        height: int,
        entry: Coordinate,
        exit: Coordinate,
        output_file: str,
        seed: int | None,
        perfect: str,
    ) -> None:
        """Initialize maze settings and internal grid state."""
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.seed = seed
        self.perfect = perfect
        self.grid: list[list[Cell]] = [
            [Cell() for _ in range(width)] for _ in range(height)
        ]
        self.cell_size = self.calculate_cell_size(width, height)
        self.color = Colors.PINK.value

    @staticmethod
    def calculate_cell_size(width: int, height: int) -> int:
        """Compute pixel size per cell from maze dimensions."""
        adjust_width = 1920 // width
        adjust_height = 1080 // height
        if (width * height) < 100:
            return min(adjust_width, adjust_height) - 40
        if (width * height) < 1000:
            return min(adjust_width, adjust_height) - 10
        # if (width * height) < 5000:
        #     return min(adjust_width, adjust_height) - 2
        if (width * height) < 10000:
            return min(adjust_width, adjust_height) - 2
        return min(adjust_width, adjust_height)

    def find_42(self) -> tuple[list[Coordinate], list[Coordinate]]:
        """Return coordinate sets that draw the 42 marker."""
        center = (self.width // 2, self.height // 2)
        lst4: list[Coordinate] = [
            (center[0] - 1, center[1]),
            (center[0] - 2, center[1]),
            (center[0] - 3, center[1]),
            (center[0] - 3, center[1] - 1),
            (center[0] - 3, center[1] - 2),
            (center[0] - 1, center[1] + 1),
            (center[0] - 1, center[1] + 2),
        ]
        lst2: list[Coordinate] = [
            (center[0] + 1, center[1]),
            (center[0] + 2, center[1]),
            (center[0] + 3, center[1]),
            (center[0] + 3, center[1] - 1),
            (center[0] + 3, center[1] - 2),
            (center[0] + 3, center[1] - 2),
            (center[0] + 2, center[1] - 2),
            (center[0] + 1, center[1] - 2),
            (center[0] + 1, center[1] + 1),
            (center[0] + 1, center[1] + 2),
            (center[0] + 2, center[1] + 2),
            (center[0] + 3, center[1] + 2),
        ]
        return lst4, lst2

    def mark_42(self) -> None:
        """Mark 42 cells as visited in the current grid."""
        lst4, lst2 = self.find_42()
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if (x, y) in lst4 or (x, y) in lst2:
                    cell.visited = True

    def get_unvisited_neighbors(self, row: int, col: int) -> list[Step]:
        """Return unvisited neighbor cells with movement directions."""
        neighbors: list[Step] = []
        if row > 0 and not self.grid[row - 1][col].visited:
            neighbors.append((row - 1, col, "N"))
        if row < self.height - 1 and not self.grid[row + 1][col].visited:
            neighbors.append((row + 1, col, "S"))
        if col > 0 and not self.grid[row][col - 1].visited:
            neighbors.append((row, col - 1, "W"))
        if col < self.width - 1 and not self.grid[row][col + 1].visited:
            neighbors.append((row, col + 1, "E"))
        return neighbors

    def get_right_wall_neighbors(self, row: int, col: int) -> list[Step]:
        """Return reachable neighbors through opened walls."""
        neighbors: list[Step] = []
        if row > 0 and self.grid[row][col].north is False:
            neighbors.append((row - 1, col, "N"))
        if row < self.height - 1 and self.grid[row][col].south is False:
            neighbors.append((row + 1, col, "S"))
        if col > 0 and self.grid[row][col].west is False:
            neighbors.append((row, col - 1, "W"))
        if col < self.width - 1 and self.grid[row][col].east is False:
            neighbors.append((row, col + 1, "E"))
        return neighbors

    def return_to_true_mark(self) -> None:
        """Restore border walls after imperfect carving."""
        for j in range(self.width):
            self.grid[0][j].north = True
        for j in range(self.width):
            self.grid[self.height - 1][j].south = True
        for i in range(self.height):
            self.grid[i][0].west = True
        for i in range(self.height):
            self.grid[i][self.width - 1].east = True

    def mark_path_for_imperfect(self) -> None:
        """Reset visits and reapply protected cells and border walls."""
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].visited = False

        self.mark_42()

        for j in range(self.width):
            self.grid[0][j].north = True
        for j in range(self.width):
            self.grid[self.height - 1][j].south = True
        for i in range(self.height):
            self.grid[i][0].west = True
        for i in range(self.height):
            self.grid[i][self.width - 1].east = True

    def check_cell_and_wall_for_imperfect(
        self,
        row: int,
        col: int,
        next_row: int,
        next_col: int,
    ) -> bool:
        """Check whether both cells can lose one wall safely."""
        if self.grid[row][col].visited:
            return False

        current_walls = [
            self.grid[row][col].north,
            self.grid[row][col].south,
            self.grid[row][col].east,
            self.grid[row][col].west,
        ]
        next_walls = [
            self.grid[next_row][next_col].north,
            self.grid[next_row][next_col].south,
            self.grid[next_row][next_col].east,
            self.grid[next_row][next_col].west,
        ]

        return current_walls.count(True) > 1 and next_walls.count(True) > 1

    def check_and_break_direction(
        self,
        row: int,
        col: int,
        direction: str,
        nx: int,
        ny: int,
    ) -> None:
        """Break matching walls for two adjacent cells by direction."""
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

    def generate_maze(self) -> list[Step]:
        """Generate maze passages and optionally add imperfect cycles."""
        stack: list[Coordinate] = [self.entry]
        path: list[Step] = []

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
            number_of_try = 10000000000
            while wall_to_break and number_of_try != 0:
                row = random.randint(0, self.height - 1)
                col = random.randint(0, self.width - 1)
                neighbors = self.get_unvisited_neighbors(row, col)
                if neighbors:
                    nx, ny, direction = random.choice(neighbors)
                    if self.check_cell_and_wall_for_imperfect(
                        row, col, nx, ny
                    ):
                        self.check_and_break_direction(
                            row, col, direction, nx, ny
                            )
                        path.append((row, col, direction))
                        wall_to_break -= 1
                number_of_try -= 1
            self.return_to_true_mark()

        return path

    def solve_maze(self) -> list[Step]:
        """Solve the maze from entry to exit using BFS."""
        start = self.entry
        end = self.exit

        queue: deque[Coordinate] = deque([start])
        visited: set[Coordinate] = {start}
        came_from: dict[Coordinate, tuple[Coordinate, str]] = {}
        path: list[Step] = []

        while queue:
            row, col = queue.popleft()
            current = (row, col)

            neighbors = self.get_right_wall_neighbors(row, col)
            for nx, ny, direction in neighbors:
                new = (nx, ny)
                if new not in visited:
                    visited.add(new)
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
        return path

    def from_bool_to_decimal(self, row: int, col: int) -> int:
        """Convert a cell wall state into its hexadecimal nibble value."""
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

    def generate_output_file(self, path: list[Step]) -> None:
        """Write maze grid, points, and solution path to the output file."""
        try:
            with open(self.output_file, "w") as file:
                for i in range(self.height):
                    line = ""
                    for j in range(self.width):
                        value = self.from_bool_to_decimal(i, j)
                        line += format(value, "X")
                    file.write(line + "\n")

                file.write("\n")
                file.write(
                    f"{self.entry[0]}, {self.entry[1]}\n"
                )
                file.write(
                    f"{self.exit[0]}, {self.exit[1]}\n"
                )

                path_str = ""
                for _, _, direction in path:
                    path_str += direction
                file.write(path_str + "\n")
        except Exception as exc:
            print("generation file", exc)
            sys.exit(1)
