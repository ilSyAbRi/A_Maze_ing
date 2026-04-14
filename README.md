# 🧩 A-Maze-ing

*This project has been created as part of the 42 curriculum by ibet-lot, ilsyabri*

## 📖 Description

A-Maze-ing is a Python maze generator and solver.

It generates a random maze from a config file, solves it using BFS, and supports visualization (ASCII / MLX).

---

## ⚙️ Instructions

```bash
make install
make run
```
or

python3 a_maze_ing.py config.txt

📄 Config File Format

Each line is:

KEY=VALUE

Required:

    WIDTH

    HEIGHT

    ENTRY (x,y)

    EXIT (x,y)

    OUTPUT_FILE

    PERFECT (True/False)

Optional:

    SEED

🧠 Algorithm

    Maze generation: DFS (Recursive Backtracking)

    Maze solving: BFS (Shortest path)

Why DFS?

Simple, efficient, and naturally produces perfect mazes.
Why BFS?

Guarantees the shortest path from entry to exit.
🔁 Reusable Code

The generator is implemented in a reusable class:

    MazeGenerator

    Can be imported in other projects

    Supports custom size and seed

    Provides maze grid and solution path

👥 Team & Management
Roles

    ibet-lot (Leader and the structer): 
        MLX visualization, rendering, animations, menu, Makefile, packaging
        take input from the legend to display a beautiful maze

    ilsyabri(the legend): 
    DFS generation, BFS solving, imperfect maze, parsing, output file
        make input perfect and easy for use by the leader to display

Planning

    Started with config parsing and maze generation

    Added solving (BFS)

    Added MLX visualization and animations

    Improved structure and packaging

What worked well

    Clear separation of tasks

    Efficient DFS + BFS implementation

    Working graphical visualization

What could be improved

    More algorithms (Prim/Kruskal)

    Better performance on large mazes

    UI improvements

Tools used

    Python 3.10+

    MiniLibX (MLX)

    flake8 / mypy

🧩 Maze Generator & Solver Documentation
📌 Overview

```
This project implements a complete maze system in Python, including:

Maze generation (perfect & imperfect)
Maze solving using BFS
Exporting the maze to a file in a specific hexadecimal encoding format

The maze is represented as a grid of cells, where each cell has walls in four directions.

🏗️ Core Concepts
🔲 Cell Structure

Each cell contains:

north, south, east, west → walls (boolean)
visited → used during generation
True  = wall exists
False = wall is open
🎯 MazeGenerator Class

The MazeGenerator class is responsible for:

Creating the grid
Generating the maze
Solving the maze
Exporting the result
⚙️ Initialization
MazeGenerator(
    width,
    height,
    entry,
    exit,
    output_file,
    seed,
    perfect
)
Parameters
Parameter	Description
width	Maze width
height	Maze height
entry	Start coordinate (row, col)
exit	End coordinate (row, col)
output_file	File where maze is saved
seed	Random seed (for reproducibility)
perfect	"true" or "false"
🧱 Maze Generation Algorithm
🧠 Algorithm Used: Depth-First Search (DFS) with Backtracking
Steps:
Start from the entry cell
Mark it as visited
While stack is not empty:
Get unvisited neighbors
Choose one randomly
Remove the wall between cells
Push neighbor to stack
If no neighbors → backtrack
🔁 Function
generate_maze()
🔓 Imperfect Maze (Cycles)

If perfect == "false":

Additional walls are randomly removed
Creates loops (multiple paths)
Steps:
Reset visited cells
Protect special "42" pattern
Randomly break walls if safe
Restore outer borders
🔍 Maze Solving Algorithm
🧠 Algorithm Used: Breadth-First Search (BFS)
Why BFS?
Guarantees shortest path
Explores level by level
🔁 Function
solve_maze()
How it works:
Start from entry
Use a queue
Track visited cells
Store path using came_from
Reconstruct path from exit → entry
🧭 Path Representation

Each step is:

(row, col, direction)

Example directions:

N = North
S = South
E = East
W = West
🔢 Maze Encoding (VERY IMPORTANT)

Each cell is converted into a hexadecimal value based on its walls.

Bit Mapping
Direction	Bit	Value
North	1	0b0001
East	2	0b0010
South	4	0b0100
West	8	0b1000
Function
from_bool_to_decimal()
Example

If a cell has:

North wall
West wall
1 (north) + 8 (west) = 9 → "9" in hex
📄 Output File Format

Generated using:

generate_output_file(path)
Structure:
[MAZE GRID]

[EMPTY LINE]

entry_row, entry_col
exit_row, exit_col

PATH
🧱 Example Grid Line
D9595933...

Each character = one cell (hex value)

📍 Entry / Exit
0, 0
9, 9
🧭 Path
SSENNESSENNE...
🔄 Wall Consistency Rule

When removing a wall:

If you remove EAST from (A)
You must remove WEST from neighbor (B)

Handled in:

check_and_break_direction()
🧪 Neighbor Functions
Unvisited neighbors (for generation)
get_unvisited_neighbors()
Accessible neighbors (for solving)
get_right_wall_neighbors()
🎨 Extra Features
🎯 "42" Marker
Special pattern drawn in the center
Protected during imperfect generation

Functions:

find_42()
mark_42()
🚀 Usage Example
maze = MazeGenerator(
    width=40,
    height=40,
    entry=(0, 0),
    exit=(39, 39),
    output_file="maze.txt",
    seed=42,
    perfect="true"
)

path = maze.generate_maze()
solution = maze.solve_maze()
maze.generate_output_file(solution)
⚠️ Common Errors
❌ Wrong Encoding
Caused by incorrect bit mapping
Must follow: N=1, E=2, S=4, W=8
❌ Broken Walls
Must always update both cells
✅ Summary
Feature	Algorithm
Generation	DFS
Solving	BFS
Encoding	Bitmask (Hex)
Imperfect	Random wall removal
🏁 Final Notes
The maze is guaranteed solvable
BFS ensures shortest path
Encoding must match validator expectations exactly
```
