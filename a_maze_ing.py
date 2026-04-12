import sys
from parsing.parsing import config_parser
from generation import MazeGenerator, Displayer, Maze 

try:
    maze = config_parser()
    Displayer.display_maze(maze)
    path = MazeGenerator.solve_maze(maze)
    MazeGenerator.generate_output_file(maze, path)

except KeyboardInterrupt as e:
    print("main file",e)
    sys.exit(1)
except Exception as d:
    print("main file", d)
    sys.exit(1)
