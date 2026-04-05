import sys
from parsing.parsing import config_parser
from generation.Display import Displayer
from generation.Maze import Maze 

conf_dict = config_parser()



Displayer.display_maze(maze)