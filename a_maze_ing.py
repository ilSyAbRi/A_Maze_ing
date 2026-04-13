from parsing.parsing import config_parser
from Display import Displayer

try:
    maze = config_parser()
    Displayer.display_maze(maze)
    path = maze.solve_maze()
    maze.generate_output_file(path)
except KeyboardInterrupt as g:
    print(g)
    sys.exit(1)
except Exception as d:
    print(d)
    sys.exit(1)
except BaseException as e:
    print(e)
    sys.exit(1)
