from mlx import Mlx
import inspect
from generation.Generator import MazeGenerator
from generation.Maze import Maze, Colors
class Displayer:

    @staticmethod
    def display_maze(maze: Maze):
        mlx_inst = Mlx()
        mlx = mlx_inst.mlx_init()
        win = mlx_inst.mlx_new_window(mlx, (maze.width * maze.cell_size) + 20, (maze.height * maze.cell_size) + 20, "A_Maze_Ing")
        Displayer.draw_grid(mlx_inst, mlx, win, maze, maze.cell_size)
        Displayer.fill_42(mlx_inst, mlx, win, maze)
        path = MazeGenerator.generate_maze(maze)
        Displayer.animate(mlx_inst, mlx, win , path, maze)
        mlx_inst.mlx_do_sync(mlx)
        Displayer.draw_grid(mlx_inst, mlx, win, maze, maze.cell_size)
        mlx_inst.mlx_loop(mlx)

    @staticmethod
    def draw_cell(mlx_inst, mlx, win, x, y, cell, cell_size):
        start_x = x * cell_size
        start_y = y * cell_size
        if cell.north:
            Displayer.draw_horizontal_wall(mlx_inst, mlx, win, start_x, start_y, cell_size, Colors.GREEN.value)
        if cell.south:
            Displayer.draw_horizontal_wall(mlx_inst, mlx, win, start_x, start_y + cell_size, cell_size, Colors.GREEN.value)
        if cell.west:
            Displayer.draw_vertical_wall(mlx_inst, mlx, win, start_x, start_y, cell_size, Colors.GREEN.value)
        if cell.east:
            Displayer.draw_vertical_wall(mlx_inst, mlx, win, start_x + cell_size, start_y, cell_size, Colors.GREEN.value)

    @staticmethod
    def draw_grid(mlx_inst, mlx, win, maze, cell_size):
        for y, row in enumerate(maze.grid):
            for x, cell in enumerate(row):
                Displayer.draw_cell(mlx_inst, mlx, win,x, y, cell, cell_size)

    @staticmethod
    def draw_horizontal_wall(mlx_inst, mlx, win, start_x, start_y, cell_size, color):
        end_x = start_x + cell_size
        for x in range(start_x, end_x):
            mlx_inst.mlx_pixel_put(mlx, win, x, start_y, color)
    
    @staticmethod
    def draw_vertical_wall(mlx_inst, mlx, win, start_x, start_y, cell_size, color):
        end_y = start_y + cell_size
        for y in range(start_y, end_y):
            mlx_inst.mlx_pixel_put(mlx, win, start_x, y, color) 
    
    @staticmethod
    def fill_cell(mlx_inst, mlx, win, x, y, cell_size, color):
        start_x = x * cell_size
        start_y = y * cell_size
        for i in range(start_x + 1, start_x + cell_size):
            for j in range(start_y + 1, start_y + cell_size):
                mlx_inst.mlx_pixel_put(mlx, win, i, j, color)

    @staticmethod
    def fill_42(mlx_inst, mlx, win, maze):
        lst2, lst4 = maze.find_42()
        for x, y in lst4:
            if 0 <= x < maze.width and 0 <= y < maze.height:
                Displayer.fill_cell(mlx_inst, mlx, win, x, y, maze.cell_size, Colors.PURPLE.value)
        for x, y in lst2:
            if 0 <= x < maze.width and 0 <= y < maze.height:
                Displayer.fill_cell(mlx_inst, mlx, win, x, y, maze.cell_size, Colors.PURPLE.value)

    @staticmethod
    def animate(mlx_inst, mlx, win , path, maze):
        i = 0
        for y, x, d in path:
            start_x = x * maze.cell_size
            start_y = y * maze.cell_size
            if d == "N":
                end_x = start_x + maze.cell_size
                for x in range(start_x + 1, end_x):
                    mlx_inst.mlx_pixel_put(mlx, win, x, start_y, Colors.BLACK.value)
            if d == "E":
                start_x += maze.cell_size
                end_y = start_y + maze.cell_size
                for y in range(start_y + 1, end_y):
                    mlx_inst.mlx_pixel_put(mlx, win, start_x, y, Colors.BLACK.value) 
            if d == "S":
                start_y += maze.cell_size
                end_x = start_x + maze.cell_size
                for x in range(start_x + 1, end_x):
                    mlx_inst.mlx_pixel_put(mlx, win, x, start_y, Colors.BLACK.value)
            if d == "W":
                end_y = start_y + maze.cell_size
                for y in range(start_y + 1, end_y):
                    mlx_inst.mlx_pixel_put(mlx, win, start_x, y, Colors.BLACK.value) 
            if i % 2 == 0:
                mlx_inst.mlx_do_sync(mlx)
            i += 1
