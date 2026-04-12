import sys
from parsing.parsing import config_parser
from generation import MazeGenerator, Displayer, Maze 

try:
    maze = config_parser()
    Displayer.display_maze(maze)
    MazeGenerator.solve_maze(maze)

except KeyboardInterrupt as e:
    sys.exit(1)
except BaseException as b:
    sys.exit(1)
