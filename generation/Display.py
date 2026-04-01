from mlx import Mlx
import inspect
from generation.Maze import Maze
class Displayer:

    @staticmethod
    def display_maze(maze: Maze):
        mlx_inst = Mlx()
        mlx = mlx_inst.mlx_init()
        adjust_width = 1920 // maze.width 
        adjust_height = 1080 // maze.height
        cell_size = min(adjust_width, adjust_height) - 3
        win = mlx_inst.mlx_new_window(mlx, (maze.width * cell_size) + 10, (maze.height * cell_size) + 10, "A_Maze_Ing")
        Displayer.draw_grid(mlx_inst, mlx, win, maze, cell_size)
        Displayer.draw_42(maze, mlx_inst, mlx, win)
        mlx_inst.mlx_loop(mlx)

    @staticmethod
    def draw_cell(mlx_inst, mlx, win, x, y, cell, cell_size):
        start_x = x * cell_size
        start_y = y * cell_size
        if cell.north == True:
            Displayer.draw_horizontal_wall(mlx_inst, mlx, win, start_x, start_y, cell_size)
        if cell.south:
            Displayer.draw_horizontal_wall(mlx_inst, mlx, win, start_x, start_y + cell_size, cell_size)
        if cell.west:
            Displayer.draw_vertical_wall(mlx_inst, mlx, win, start_x, start_y, cell_size)
        if cell.east:
            Displayer.draw_vertical_wall(mlx_inst, mlx, win, start_x + cell_size, start_y, cell_size)

    @staticmethod
    def draw_grid(mlx_inst, mlx, win, maze, cell_size):
        for y, row in enumerate(maze.grid):
            for x, cell in enumerate(row):
                Displayer.draw_cell(mlx_inst, mlx, win,x, y, cell, cell_size)

    @staticmethod
    def draw_horizontal_wall(mlx_inst, mlx, win, start_x, start_y, cell_size):
        end_x = start_x + cell_size
        for x in range(start_x, end_x):
            mlx_inst.mlx_pixel_put(mlx, win, x, start_y, 0xFFFFFFFF)
    
    @staticmethod
    def draw_vertical_wall(mlx_inst, mlx, win, start_x, start_y, cell_size):
        end_y = start_y + cell_size
        for y in range(start_y, end_y):
            mlx_inst.mlx_pixel_put(mlx, win, start_x, y, 0xFFFFFFFF)  
    
    @staticmethod
    def fill_cell(mlx_inst, mlx, win, x, y, cell_size):
        start_x = x * cell_size
        start_y = y * cell_size
        for i in range(start_x + 1, start_x + cell_size):
            for j in range(start_y + 1, start_y + cell_size):
                mlx_inst.mlx_pixel_put(mlx, win, i, j, 0xFF0000FF)

    @staticmethod
    def draw_42(maze: Maze, mlx_inst, mlx, win):
        center = (maze.width // 2, maze.height // 2)
        lst4 = [
            (center[0], center[1]), (center[0] - 1, center[1]), (center[0] - 2, center[1]),
            (center[0] - 2, center[1] - 1), (center[0] - 2, center[1] - 2),
            (center[0], center[1]), (center[0], center[1] + 1), (center[0], center[1] + 2)
        ]
        lst2 = [
            (center[0] - 1, center[1] + 1), (center[0] - 1, center[1] + 2),
            (center[0] - 2, center[1] + 1), (center[0] - 2, center[1] + 2)
        ]
        for x, y in lst4:
            if 0 <= x < maze.width and 0 <= y < maze.height:
                Displayer.fill_cell(mlx_inst, mlx, win, x, y, maze.cell_size - 3)
        for x, y in lst2:
            if 0 <= x < maze.width and 0 <= y < maze.height:
                Displayer.fill_cell(mlx_inst, mlx, win, x, y, maze.cell_size)
