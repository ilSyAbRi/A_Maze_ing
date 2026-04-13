import os
import random
from typing import Any

from mlx import Mlx
from PIL import Image

from mazegen import Colors, MazeGenerator


class Displayer:
    """Render and interact with the maze window."""

    @staticmethod
    def display_maze(maze: MazeGenerator) -> None:
        """Create windows and start the rendering loop."""
        mlx_inst = Mlx()
        mlx = mlx_inst.mlx_init()
        win = mlx_inst.mlx_new_window(
            mlx,
            (maze.width * maze.cell_size) + 2,
            (maze.height * maze.cell_size) + 2,
            "A_Maze_Ing",
        )
        Displayer.draw_menu(mlx_inst, mlx, win, maze)
        Displayer.draw_grid(mlx_inst, mlx, win, maze)
        Displayer.fill_42(mlx_inst, mlx, win, maze)
        path = maze.generate_maze()
        maze.solve_maze()
        Displayer.animate(mlx_inst, mlx, win, path, maze)
        y, x = maze.entry
        Displayer.draw_ball(mlx_inst, mlx, win, x, y, maze.cell_size)
        Displayer.draw_gate(mlx_inst, mlx, win, maze, Colors.WHITE.value)
        Displayer.draw_grid(mlx_inst, mlx, win, maze)
        mlx_inst.mlx_do_sync(mlx)
        mlx_inst.mlx_loop(mlx)

    @staticmethod
    def draw_cell(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        x: int,
        y: int,
        cell: Any,
        cell_size: int,
        color: int,
    ) -> None:
        """Draw all active walls of one maze cell."""
        start_x = x * cell_size
        start_y = y * cell_size
        if cell.north:
            Displayer.draw_horizontal_wall(
                mlx_inst, mlx, win, start_x, start_y, cell_size, color
            )
        if cell.south:
            Displayer.draw_horizontal_wall(
                mlx_inst,
                mlx,
                win,
                start_x,
                start_y + cell_size,
                cell_size,
                color,
            )
        if cell.west:
            Displayer.draw_vertical_wall(
                mlx_inst, mlx, win, start_x, start_y, cell_size, color
            )
        if cell.east:
            Displayer.draw_vertical_wall(
                mlx_inst,
                mlx,
                win,
                start_x + cell_size,
                start_y,
                cell_size,
                color,
            )

    @staticmethod
    def draw_grid(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
    ) -> None:
        """Draw every cell wall in the maze."""
        cell_size = maze.cell_size
        for y, row in enumerate(maze.grid):
            for x, cell in enumerate(row):
                Displayer.draw_cell(
                    mlx_inst, mlx, win, x, y, cell, cell_size, maze.color
                )
        mlx_inst.mlx_do_sync(mlx)

    @staticmethod
    def draw_horizontal_wall(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        start_x: int,
        start_y: int,
        cell_size: int,
        color: int,
    ) -> None:
        """Draw one horizontal wall segment."""
        end_x = start_x + cell_size
        for x in range(start_x, end_x):
            mlx_inst.mlx_pixel_put(mlx, win, x, start_y, color)

    @staticmethod
    def draw_vertical_wall(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        start_x: int,
        start_y: int,
        cell_size: int,
        color: int,
    ) -> None:
        """Draw one vertical wall segment."""
        end_y = start_y + cell_size
        for y in range(start_y, end_y):
            mlx_inst.mlx_pixel_put(mlx, win, start_x, y, color)

    @staticmethod
    def fill_cell(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        x: int,
        y: int,
        cell_size: int,
        color: int,
    ) -> None:
        """Fill one cell interior with a color."""
        start_x = x * cell_size
        start_y = y * cell_size
        for i in range(start_x + 1, start_x + cell_size):
            for j in range(start_y + 1, start_y + cell_size):
                mlx_inst.mlx_pixel_put(mlx, win, i, j, color)

    @staticmethod
    def fill_42(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
    ) -> None:
        """Fill cells that form the 42 marker."""
        lst2, lst4 = maze.find_42()
        for x, y in lst4:
            if 0 <= x < maze.width and 0 <= y < maze.height:
                Displayer.fill_cell(
                    mlx_inst,
                    mlx,
                    win,
                    x,
                    y,
                    maze.cell_size,
                    Colors.PURPLE.value,
                )
        for x, y in lst2:
            if 0 <= x < maze.width and 0 <= y < maze.height:
                Displayer.fill_cell(
                    mlx_inst,
                    mlx,
                    win,
                    x,
                    y,
                    maze.cell_size,
                    Colors.PURPLE.value,
                )

    @staticmethod
    def animate(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        path: list[tuple[int, int, str]],
        maze: MazeGenerator,
    ) -> None:
        """Animate wall removals along the generated path."""
        i = 0
        for y, x, direction in path:
            start_x = x * maze.cell_size
            start_y = y * maze.cell_size
            if direction == "N":
                end_x = start_x + maze.cell_size
                for px in range(start_x + 1, end_x):
                    mlx_inst.mlx_pixel_put(
                        mlx, win, px, start_y, Colors.BLACK.value
                    )
            if direction == "E":
                start_x += maze.cell_size
                end_y = start_y + maze.cell_size
                for py in range(start_y, end_y):
                    mlx_inst.mlx_pixel_put(
                        mlx, win, start_x, py, Colors.BLACK.value
                    )
            if direction == "S":
                start_y += maze.cell_size
                end_x = start_x + maze.cell_size
                for px in range(start_x + 1, end_x):
                    mlx_inst.mlx_pixel_put(
                        mlx, win, px, start_y, Colors.BLACK.value
                    )
            if direction == "W":
                end_y = start_y + maze.cell_size
                for py in range(start_y, end_y):
                    mlx_inst.mlx_pixel_put(
                        mlx, win, start_x, py, Colors.BLACK.value
                    )
            if i % 2 == 0:
                mlx_inst.mlx_do_sync(mlx)
            i += 1

    @staticmethod
    def draw_ball(
        mlx_inst: Any, mlx: Any, win: Any, x: int, y: int, cell_size: int
    ) -> None:
        """Draw the player ball at a cell location."""
        center_x = x * cell_size + cell_size // 2
        center_y = y * cell_size + cell_size // 2
        radius = cell_size // 3
        for i in range(center_x - radius, center_x + radius):
            for j in range(center_y - radius, center_y + radius):
                if (i - center_x) ** 2 + (j - center_y) ** 2 <= radius ** 2:
                    mlx_inst.mlx_pixel_put(mlx, win, i, j, Colors.BLUE.value)
        mlx_inst.mlx_do_sync(mlx)

    @staticmethod
    def draw_gate(
        mlx_inst: Any, mlx: Any, win: Any, maze: MazeGenerator, color: int
    ) -> None:
        """Draw the exit gate pattern inside the exit cell."""
        y, x = maze.exit
        cell_size = maze.cell_size
        start_x = x * cell_size
        start_y = y * cell_size
        end_x = start_x + cell_size
        end_y = start_y + cell_size
        for i in range(start_x + 1, end_x):
            for j in range(start_y + 1, end_y):
                if (
                    (i - start_x) % (cell_size // 9) >= 2
                    or (j - start_y) % (cell_size // 3) >= 2
                ):
                    mlx_inst.mlx_pixel_put(mlx, win, i, j, color)
        mlx_inst.mlx_do_sync(mlx)

    @staticmethod
    def draw_menu(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
    ) -> None:
        """Draw the menu window and register interaction hooks."""
        colors = [
            0xFF0A9F2C,
            0xFF102ADE,
            0xFF0CDFA4,
            0xFFCB0CDF,
            0xFFDF0C1C,
            0xFF2A3AC7,
            0xFFE6E7F1,
            0xFFFFD700,
        ]
        menu: dict[str, Any] = {
            "1-option": False,
            "2-option": 4,
            "3-option": False,
            "4-option": False,
        }
        try:
            menu_ptr = mlx_inst.mlx_new_window(mlx, 300, 650, "menu")
            resized_img = Displayer.resize_image_to_window(
                "./assests/b_g.png", False
            )
            img_ptr, _, _ = mlx_inst.mlx_png_file_to_image(mlx, resized_img)
            mlx_inst.mlx_put_image_to_window(mlx, menu_ptr, img_ptr, -150, 0)
            mlx_inst.mlx_do_sync(mlx)
            resized_tit = Displayer.resize_image_to_window(
                "./assests/title.png", True
            )
            img_tit_ptr, _, _ = mlx_inst.mlx_png_file_to_image(
                mlx, resized_tit
                )
            mlx_inst.mlx_put_image_to_window(
                mlx, menu_ptr, img_tit_ptr, 50, 10
                )
            mlx_inst.mlx_do_sync(mlx)
            Displayer.draw_rectangle_border(
                mlx_inst,
                mlx,
                menu_ptr,
                30,
                210,
                250,
                60,
                Colors.YELLOW.value,
            )
            mlx_inst.mlx_string_put(
                mlx,
                menu_ptr,
                50,
                230,
                Colors.YELLOW.value,
                "1 - (Re)Generate Maze",
            )

            Displayer.draw_rectangle_border(
                mlx_inst,
                mlx,
                menu_ptr,
                30,
                290,
                250,
                60,
                Colors.YELLOW.value,
            )
            mlx_inst.mlx_string_put(
                mlx,
                menu_ptr,
                50,
                310,
                Colors.YELLOW.value,
                "2 - Show/Hide Path",
            )

            Displayer.draw_rectangle_border(
                mlx_inst,
                mlx,
                menu_ptr,
                30,
                370,
                250,
                60,
                Colors.YELLOW.value,
            )
            mlx_inst.mlx_string_put(
                mlx,
                menu_ptr,
                50,
                390,
                Colors.YELLOW.value,
                "3 - Change Color",
            )

            Displayer.draw_rectangle_border(
                mlx_inst,
                mlx,
                menu_ptr,
                30,
                450,
                250,
                60,
                Colors.YELLOW.value,
            )
            mlx_inst.mlx_string_put(
                mlx,
                menu_ptr,
                50,
                470,
                Colors.YELLOW.value,
                "4 - Exit",
            )
            mlx_inst.mlx_do_sync(mlx)
            
            def on_key(key: int, _data: Any) -> int:
                if key == 49:
                    menu["1-option"] = True
                if key == 50:
                    menu["2-option"] = 1 if menu["2-option"] == 4 else 2
                if key == 51:
                    menu["3-option"] = True
                if key == 52:
                    menu["4-option"] = True
                return 0

            def on_mouse(
                clicked: int, x: int, y: int, _data: Any
            ) -> int:
                if clicked != 1:
                    return 0
                mlx_inst.mlx_do_sync(mlx)
                if Displayer.find_area((x, y), 30, 210, 250, 60):
                    menu["1-option"] = True
                if Displayer.find_area((x, y), 30, 290, 250, 60):
                    menu["2-option"] = 1 if menu["2-option"] == 4 else 2
                if Displayer.find_area((x, y), 30, 370, 250, 60):
                    menu["3-option"] = True
                if Displayer.find_area((x, y), 30, 450, 250, 60):
                    menu["4-option"] = True
                return 0

            def on_loop(_data: Any) -> int:
                try:
                    if menu["1-option"]:
                        Displayer.regenerate(mlx_inst, mlx, win, maze, menu)
                    if menu["2-option"] == 1:
                        Displayer.show_solve_path(
                            mlx_inst,
                            mlx,
                            win,
                            maze,
                            menu,
                        )
                    if menu["2-option"] == 2:
                        Displayer.hide_path(
                            mlx_inst,
                            mlx,
                            win,
                            maze,
                            menu,
                        )
                    if menu["3-option"]:
                        maze.color = random.choice(colors)
                        Displayer.maze_switch_color(
                            mlx_inst,
                            mlx,
                            win,
                            maze,
                            menu,
                        )
                    if menu["4-option"]:
                        Displayer.quit_program(mlx_inst, mlx)
                        menu["4-option"] = False
                except KeyboardInterrupt:
                    print("try exit button")
                return 0

            def on_close(_data: Any) -> int:
                mlx_inst.mlx_loop_exit(mlx)
                return 0
            mlx_inst.mlx_hook(win, 33, 0, on_close, None)
            mlx_inst.mlx_key_hook(menu_ptr, on_key, None)
            mlx_inst.mlx_mouse_hook(menu_ptr, on_mouse, None)
            mlx_inst.mlx_loop_hook(mlx, on_loop, None)
            mlx_inst.mlx_do_sync(mlx)
        except KeyboardInterrupt:
            print("try exit button")
        return

    @staticmethod
    def resize_image_to_window(input_path: str, title: bool) -> str:
        """Resize an image to title or menu dimensions and save it."""
        img = Image.open(input_path)
        img = img.resize((200, 150) if title else (600, 800))
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_fullscreen{ext}"
        img.save(output_path)
        return output_path

    @staticmethod
    def draw_rectangle_border(
        mlx: Any,
        mlx_ptr: Any,
        win_ptr: Any,
        x: int,
        y: int,
        w: int,
        h: int,
        color: Any,
    ) -> None:
        """it literaly draw the rectangle border"""
        for i in range(w):
            mlx.mlx_pixel_put(mlx_ptr, win_ptr, x + i, y, color)
            mlx.mlx_pixel_put(mlx_ptr, win_ptr, x + i, y + h, color)

        for j in range(h):
            mlx.mlx_pixel_put(mlx_ptr, win_ptr, x, y + j, color)
            mlx.mlx_pixel_put(mlx_ptr, win_ptr, x + w, y + j, color)
        mlx.mlx_do_sync(mlx_ptr)

    @staticmethod
    def regenerate(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
        menu: dict[str, Any],
    ) -> None:
        """Regenerate and redraw the maze scene."""
        mlx_inst.mlx_clear_window(mlx, win)
        mlx_inst.mlx_do_sync(mlx)
        Displayer.maze_reset(maze)
        Displayer.draw_grid(mlx_inst, mlx, win, maze)
        mlx_inst.mlx_do_sync(mlx)
        Displayer.fill_42(mlx_inst, mlx, win, maze)
        path = maze.generate_maze()
        Displayer.animate(mlx_inst, mlx, win, path, maze)
        mlx_inst.mlx_do_sync(mlx)
        Displayer.draw_grid(mlx_inst, mlx, win, maze)
        mlx_inst.mlx_do_sync(mlx)
        y, x = maze.entry
        Displayer.draw_ball(mlx_inst, mlx, win, x, y, maze.cell_size)
        Displayer.draw_gate(mlx_inst, mlx, win, maze, Colors.WHITE.value)
        menu["1-option"] = False

    @staticmethod
    def quit_program(mlx_inst: Any, mlx: Any) -> int:
        """Stop the MLX event loop."""
        mlx_inst.mlx_loop_exit(mlx)
        return 0

    @staticmethod
    def maze_switch_color(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
        menu: dict[str, Any],
    ) -> None:
        """Redraw maze walls using the selected color."""
        Displayer.draw_grid(mlx_inst, mlx, win, maze)
        mlx_inst.mlx_do_sync(mlx)
        menu["3-option"] = False

    @staticmethod
    def maze_reset(maze: MazeGenerator) -> None:
        """Reset all cell walls and visited flags."""
        for row in maze.grid:
            for cell in row:
                cell.north = True
                cell.east = True
                cell.south = True
                cell.west = True
                cell.visited = False
        maze.mark_42()

    @staticmethod
    def find_area(
        button: tuple[int, int],
        x: int,
        y: int,
        w: int,
        h: int,
    ) -> bool:
        """Check whether a click is inside a button rectangle."""
        nx, ny = button
        return (
            ((x + 1) <= nx <= (x + w - 1))
            and ((y + 1) <= ny <= (y + h - 1))
        )

    @staticmethod
    def show_solve_path(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
        menu: dict[str, Any],
    ) -> None:
        """Draw the solved path over the current maze."""
        path = maze.solve_maze()
        for y, x, _ in path:
            Displayer.draw_ball(mlx_inst, mlx, win, x, y, maze.cell_size)
            mlx_inst.mlx_do_sync(mlx)
            menu["2-option"] = 3

    @staticmethod
    def hide_path(
        mlx_inst: Any,
        mlx: Any,
        win: Any,
        maze: MazeGenerator,
        menu: dict[str, Any],
    ) -> None:
        """Hide the solved path by repainting traversed cells."""
        path = maze.solve_maze()
        for y, x, _ in path:
            Displayer.fill_cell(
                mlx_inst, mlx, win, x, y, maze.cell_size, Colors.BLACK.value
            )
        y, x = maze.entry
        Displayer.draw_ball(mlx_inst, mlx, win, x, y, maze.cell_size)
        mlx_inst.mlx_do_sync(mlx)
        menu["2-option"] = 4
