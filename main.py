from generation.Maze import Maze
from generation.Generator import MazeGenerator

def print_maze(maze):
    """Simple text representation of the maze."""
    for row in maze.grid:
        # top walls
        line1 = ""
        for cell in row:
            line1 += "+" + ("---" if cell.north else "   ")
        line1 += "+"
        print(line1)

        # side walls
        line2 = ""
        for cell in row:
            line2 += ("|" if cell.west else " ") + "   "
        line2 += "|"  # rightmost wall
        print(line2)
    # bottom wall
    print("+" + "---+" * maze.width)

if __name__ == "__main__":
    # Example config
    width, height = 5, 5
    entry = (0, 0)
    _exit = (4, 4)
    output_file = "maze.txt"
    perfect = "true"

    # Create maze object
    maze = Maze(width, height, entry, _exit, output_file, perfect)

    # Generate maze
    path = MazeGenerator.generate_maze(maze)

    # Print result
    print_maze(maze)
    print("\nDFS path:", path)
    for y, row in enumerate(maze.grid):
        