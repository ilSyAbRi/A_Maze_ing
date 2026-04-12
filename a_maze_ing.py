import sys
from parsing.parsing import config_parser
from generation import MazeGenerator, Displayer, Maze 

try:
    maze = config_parser()
    Displayer.display_maze(maze)
    path = MazeGenerator.solve_maze(maze)
    MazeGenerator.generate_output_file(maze, path)

except KeyboardInterrupt as e:
    print("i am a key interrupt in main file:",)
    sys.exit(1)
except Exception as d:
    print("i am the mini honly of the main file:", d)
except BaseException as b:
    print("the holy of the main file:", b)
    sys.exit(1)
