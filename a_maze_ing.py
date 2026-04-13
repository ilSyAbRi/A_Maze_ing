from parsing.parsing import config_parser
from Display import Displayer
import sys

try:
    maze = config_parser()
    Displayer.display_maze(maze)
except KeyboardInterrupt as g:
    print(g)
    sys.exit(1)
except Exception as d:
    print(d)
    sys.exit(1)
except BaseException as e:
    print(e)
    sys.exit(1)
