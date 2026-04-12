import sys
from parsing.parsing import config_parser
from generation import MazeGenerator, Displayer, Maze 

try:
    maze = config_parser()
    Displayer.display_maze(maze)
    path = MazeGenerator.solve_maze(maze)
    MazeGenerator.generate_output_file(maze, path)

except KeyboardInterrupt as e:
    print("i am a key interrupt in main file")
    sys.exit(1)
except BaseException as b:
    print("the holy base exception")
    sys.exit(1)
