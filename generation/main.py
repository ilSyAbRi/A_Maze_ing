from Maze import Maze 
from Cell import Cell # Maze parameters 
width = 5 
height = 5 
entry = (0, 0) 
# top-left corner 
exit = (4, 4) # bottom-right corner 
output_file = "maze.txt" 
perfect = True # for now, you just pass it, not used in DFS 
# Create maze instance 
maze = Maze(width, height, entry, exit, output_file, perfect) # Run DFS algorithm 
path = maze.do_dfs_algo()


print("DFS Path:")
print(path)

# Optional: simple ASCII visual of the maze
print("\nMaze layout (N=North wall, W=West wall):")
for i in range(height):
    # Print north walls
    for j in range(width):
        print("_" if maze.grid[i][j].north else " ", end=" ")
    print()
    # Print west walls
    for j in range(width):
        print("|" if maze.grid[i][j].west else " ", end=" ")
    print("|")


