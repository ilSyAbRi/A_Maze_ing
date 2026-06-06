# 🧩 A-Maze-ing
> Python maze generator & solver — 42 curriculum project by `ibet-lot` & `ilsyabri`

---

## 📖 Description

**A-Maze-ing** is a Python-based maze generator and solver built as part of the 42 curriculum.

The goal of the project is to programmatically generate random mazes from a configuration file, solve them using pathfinding, and visualize the result — both in ASCII and graphically via MiniLibX.

The project is structured around a reusable `MazeGenerator` class that handles generation and solving independently, making it easy to integrate into other projects. It supports both **perfect mazes** (no loops, one unique path) and **imperfect mazes** (with cycles), configurable via the config file.

---

## ⚙️ Instructions

```bash
make install && make run
# or
python3 a_maze_ing.py config.txt
```

## 📚 Resources

### 📄 Documentation & References

- [Python 3 Official Docs](https://docs.python.org/3/) — standard library reference used throughout the project
- [MiniLibX Documentation](https://harm-smits.github.io/42docs/libs/minilibx) — 42 graphic library used for rendering
- [Maze Generation Algorithms — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm) — overview of DFS, Prim, Kruskal and other approaches
- [Breadth-First Search — Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search) — theoretical background for the solving algorithm
- [Recursive Backtracker — Jamis Buck's Blog](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracker) — in-depth walkthrough of the DFS maze generation method
- [flake8 Docs](https://flake8.pycqa.org/en/latest/) — linting tool used to enforce code style
- [mypy Docs](https://mypy.readthedocs.io/en/stable/) — static type checking tool used for code quality

### 🎥 YouTube

- [Maze Generation — Coding Train (Daniel Shiffman)](https://www.youtube.com/watch?v=HyK_Q5rrcr4) — visual walkthrough of recursive backtracking maze generation in JavaScript, great for understanding the core idea
- [BFS Shortest Path — William Fiset](https://www.youtube.com/watch?v=oDqjPvD1e6A) — clear explanation of BFS and how to reconstruct the shortest path
- [DFS Algorithm Explained — Abdul Bari](https://www.youtube.com/watch?v=7fujbpJ0LB4) — theoretical breakdown of depth-first search with examples
- [Python OOP Full Course — Tech With Tim](https://www.youtube.com/watch?v=JeznW_7DlB0) — helped structure the `MazeGenerator` class cleanly
- [MiniLibX Introduction — 42 tutorial](https://www.youtube.com/watch?v=bYS93r6U0zg) — overview of the MLX library window and event system

### 🤝 Peer Learning

- Discussed BFS path reconstruction logic with peers from the 42 network — helped clarify how to trace back the visited map to build the solution path
- Reviewed other students' approaches to config parsing to compare robustness of `KEY=VALUE` handling
- Got feedback from a peer on the MLX event loop structure, which helped fix frame refresh timing issues
- Shared our `MazeGenerator` class interface with teammates from another group for cross-review before finalizing the API

### 🤖 AI Usage

AI assistance (ChatGPT / Claude) was used in the following parts of the project:

| Task | How AI was used |
|------|----------------|
| **DFS implementation** | Used to clarify recursive backtracking logic and edge cases (e.g. boundary handling) |
| **BFS solver** | Used to double-check the queue-based traversal and path reconstruction logic |
| **Config parser** | Asked AI to suggest a clean parsing pattern for `KEY=VALUE` files in Python |
| **MLX rendering** | Used to troubleshoot event loop integration and frame refresh issues |
| **Code review** | AI was used to review code for flake8/mypy compliance before submission |
| **README** | This README structure was drafted with AI assistance and then manually reviewed |

> AI was used as a learning and debugging aid — all code was written, understood, and validated by the team.

---

### 📄 Config File

```ini
# Required
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=19,19
OUTPUT_FILE=out.txt
PERFECT=True

# Optional
SEED=42
```

---

## 🧠 Algorithms

| Step | Algorithm | Why |
|------|-----------|-----|
| Generation | DFS – Recursive Backtracking | Simple, efficient, produces perfect mazes |
| Solving | BFS – Breadth-First Search | Guarantees shortest path from entry to exit |

---

## 📦 Reusable Module

The `MazeGenerator` class can be imported into any project.

- Custom width & height
- Reproducible seeds
- Maze grid access
- Solution path output
- MLX rendering

---

## 👥 Team

| Member | Responsibilities |
|--------|-----------------|
| `ibet-lot` | MLX visualization, animations, menu, Makefile, packaging |
| `ilsyabri` | DFS generation, BFS solving, imperfect maze, parsing, output |

---

## 🔁 Retrospective

**What worked well**
- Clear separation of tasks between teammates
- Efficient DFS + BFS implementation
- Working graphical MLX visualization

**What could be improved**
- Add more algorithms (Prim, Kruskal)
- Better performance on large mazes
- UI improvements

---

## 🛠️ Tools

`Python 3.10+` · `MiniLibX` · `flake8` · `mypy`