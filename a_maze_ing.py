import sys
from parsing.parsing import config_parser
from generation import MazeGenerator, Displayer, Maze 

maze = config_parser()
MazeGenerator.generate_maze(maze)
Displayer.display_maze(maze)
