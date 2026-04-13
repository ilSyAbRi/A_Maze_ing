from parsing.parsing import config_parser
from Display import Displayer

try:
    maze = config_parser()
    Displayer.display_maze(maze)
    path = maze.solve_maze()
    maze.generate_output_file(path)
except KeyboardInterrupt:
    print("try exit button")
except Exception as d:
    print(d)
