from parsing.parsing import config_parser
import mlx

class MazeGenerator:
    @staticmethod 
    def generate_maze(config_file: str):
        config = config_parser(config_file)
        width = config['width']
        height = config['height']
        # Here you would implement your maze generation algorithm
        # For demonstration, we will just create a simple maze structure
        maze = [[0 for _ in range(width)] for _ in range(height)]
        # You can add walls and paths to the maze as needed
        return maze