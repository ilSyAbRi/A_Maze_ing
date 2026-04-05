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
