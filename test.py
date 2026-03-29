from mlx import Mlx
def main():
    """Initializes MiniLibX, creates a window, draws a rectangle, and starts the event loop."""

    # 1. Initialize the library
    mlx_inst = Mlx()
    mlx_ptr = mlx_inst.mlx_init()


    # 2. Create a window
    win_width = 800
    win_height = 600
    win_ptr = mlx_inst.mlx_new_window(mlx_ptr, win_width, win_height, "A_Maze_Ing")
    
    mlx_inst.mlx_clear_window(mlx_ptr, win_ptr)
    for i in range(100, 550):   
        for j in range(150, 203):
            mlx_inst.mlx_pixel_put(mlx_ptr, win_ptr, i, j, 0xF800F0F0)
        if i % 3 == 0:
            # mlx_inst.mlx_do_sync(mlx_ptr)
            pass
    if not win_ptr:
        print("Failed to create a new window.")
        return

    # 3. Clear window and draw something
    mlx_inst.mlx_string_put(mlx_ptr, win_ptr, 500, 300, 0xFFFFFFFF, "Hello, MiniLibX!")

    # Draw a red rectangle at (50, 50) with size 100x150
    # draw_rectangle(mlx_inst, mlx_ptr, win_ptr, 100, 100, 180, 1530, 0xFF0000)

    # 4. Synchronize the drawing to the window
  

    # 5. Start the event loop to keep the window open
    mlx_inst.mlx_loop(mlx_ptr)


if __name__ == "__main__":
    main()