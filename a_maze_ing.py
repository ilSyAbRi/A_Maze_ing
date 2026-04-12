import sys
from parsing.parsing import config_parser
from Display import Displayer

# try:
maze = config_parser()
Displayer.display_maze(maze)
path = maze.solve_maze()
maze.generate_output_file(path)

# except KeyboardInterrupt as e:
#     print("main file",e)
#     sys.exit(1)
# except Exception as d:
#     print("main file", d)
#     sys.exit(1)
