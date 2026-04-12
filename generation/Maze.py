from generation.Cell import Cell
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
    UNKNOWN = 0xffcb0cdf

class Maze:
    def __init__(self, width, height, entry, exit, output_file, seed, perfect):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.seed = seed
        self.perfect = perfect
        self.grid = [[ Cell() for _ in range(width)] for  _ in range(height)]
        self.cell_size = Maze.calculate_cell_size(width, height)
        self.color = Colors.UNKNOWN.value

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
