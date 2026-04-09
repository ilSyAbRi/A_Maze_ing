import sys
from parsing.parsing import config_parser
from generation import MazeGenerator, Displayer, Maze 

maze = config_parser()
Displayer.display_maze(maze)
