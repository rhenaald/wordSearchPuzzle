import tkinter as tk
from settings import GRID_SIZE, WORDS
from grid import generate_empty_grid, place_word_in_grid, fill_grid

def highlight_word(word, start_row, start_col, direction, canvas, grid_labels):
    if direction == 'horizontal':
        for i in range(len(word)):
            grid_labels[start_row][start_col + i].config(bg="yellow")
    elif direction == 'vertical':
        for i in range(len(word)):
            grid_labels[start_row + i][start_col].config(bg="yellow")
    elif direction == 'diagonal_down':
        for i in range(len(word)):
            grid_labels[start_row + i][start_col + i].config(bg="yellow")
    elif direction == 'diagonal_up':
        for i in range(len(word)):
            grid_labels[start_row - i][start_col + i].config(bg="yellow")

def create_tkinter_grid():
    root = tk.Tk()
    root.title("Pencarian Kata")

    canvas = tk.Canvas(root, width=GRID_SIZE * 40, height=GRID_SIZE * 40)
    canvas.pack()

    global grid_labels
    grid_labels = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            label = tk.Label(canvas, text=" ", width=4, height=2, relief="solid", font=("Helvetica", 14))
            label.grid(row=row, column=col, padx=2, pady=2)
            grid_labels[row][col] = label

    grid = generate_empty_grid()
    placed_words = []
    for word in WORDS:
        word = word.upper()
        place_word_in_grid(word, grid)
        placed_words.append(word)

    fill_grid(grid)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid_labels[row][col].config(text=grid[row][col])

    start_row = start_col = None
    highlighted_cells = []  # To store the path of the drag

    def on_drag_start(event, row, col):
        nonlocal start_row, start_col
        start_row, start_col = row, col
        clear_highlighted_cells()  # Clear previous highlights

    def on_drag_motion(event, row, col):
        nonlocal highlighted_cells
        clear_highlighted_cells()  # Clear previous path

        if start_row is not None and start_col is not None:
            # Highlight all cells from start to current position
            direction = get_direction(start_row, start_col, row, col)
            cells_to_highlight = get_cells_in_path(start_row, start_col, row, col, direction)

            # Update highlighted cells visually
            for r, c in cells_to_highlight:
                grid_labels[r][c].config(bg="lightblue")
            highlighted_cells = cells_to_highlight  # Store for clearing later

    def on_drag_end(event):
        nonlocal start_row, start_col
        clear_highlighted_cells()  # Clear the path after ending drag
        start_row, start_col = None, None  # Reset start position

    def clear_highlighted_cells():
        for r, c in highlighted_cells:
            grid_labels[r][c].config(bg="white")

    def get_direction(sr, sc, er, ec):
        """Determine the drag direction."""
        if sr == er:
            return 'horizontal'
        elif sc == ec:
            return 'vertical'
        elif er - sr == ec - sc:
            return 'diagonal_down'
        elif er - sr == -(ec - sc):
            return 'diagonal_up'
        return None

    def get_cells_in_path(sr, sc, er, ec, direction):
        """Get all cells from start to end position in the given direction."""
        cells = []
        if direction == 'horizontal':
            for i in range(abs(ec - sc) + 1):
                cells.append((sr, sc + i))
        elif direction == 'vertical':
            for i in range(abs(er - sr) + 1):
                cells.append((sr + i, sc))
        elif direction == 'diagonal_down':
            for i in range(abs(er - sr) + 1):
                cells.append((sr + i, sc + i))
        elif direction == 'diagonal_up':
            for i in range(abs(er - sr) + 1):
                cells.append((sr - i, sc + i))
        return cells

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid_labels[row][col].bind("<ButtonPress-1>", lambda event, row=row, col=col: on_drag_start(event, row, col))
            grid_labels[row][col].bind("<B1-Motion>", lambda event, row=row, col=col: on_drag_motion(event, row, col))
            grid_labels[row][col].bind("<ButtonRelease-1>", on_drag_end)

    word_list_frame = tk.Frame(root)
    word_list_frame.pack()
    tk.Label(word_list_frame, text="Kata yang Harus Ditemukan:", font=("Helvetica", 12)).pack()
    for word in WORDS:
        tk.Label(word_list_frame, text=word.upper(), font=("Helvetica", 12)).pack()

    root.mainloop()
