import sys
from parsing.parsing import config_parser
from generation.Display import Displayer
from generation.Maze import Maze 

conf_dict = config_parser()
maze = Maze(
            width = conf_dict["WIDTH"],
            height = conf_dict["HEIGHT"],
            entry = conf_dict["ENTRY"],
            exit = conf_dict["EXIT"], 
            output_file = conf_dict["OUTPUT_FILE"],
            perfect = conf_dict["PERFECT"]
        )


Displayer.display_maze(maze)
