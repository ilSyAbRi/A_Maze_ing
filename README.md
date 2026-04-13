*This project has been created as part of the 42 curriculum by ibet-lot, ilsyabri*

# 🧩 A-Maze-ing — This is the way

## 📖 Description

A-Maze-ing is a Python project that generates, solves, and visualizes mazes based on a configuration file.

The program:

- Reads parameters from a configuration file
- Generates a random maze (perfect or imperfect)
- Ensures structural validity and constraints
- Computes the shortest path from entry to exit
- Outputs the maze in a hexadecimal encoded format
- Displays a visual representation (ASCII or MLX)

This project explores:

- Graph theory (spanning trees)
- Pathfinding algorithms (BFS)
- Procedural generation
- Clean and reusable software design

---

## ⚙️ Instructions

### 🔧 Installation

```bash
make install
```
#### Or manually:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### ▶️ Run the program
```
make run
```
#### Or:
```
python3 a_maze_ing.py config.txt
```
### 🐞 Debug mode
```
make debug
```

### 🧹 Clean project
```
make clean
```
### ✅ Linting
```
make lint
```
#### Optional strict mode:
```
make lint-strict
```👥 Team & Project Management
Roles
Member	Responsibilities
ibet-lot	MLX graphical interface, maze rendering, solution rendering, animations (generation & solving), menu system, packaging, Makefile
ilsyabri	Maze generation (DFS), solving algorithm (BFS), imperfect maze logic, output file, configuration parsing```
