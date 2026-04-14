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

    ilsyabri(the legend): DFS generation, BFS solving, imperfect maze, parsing, output file
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
