# utils/grid_mapper.py
def generate_question_grid(start_x, start_y, dx, dy, rows, cols):
    """
    Generates a grid of bubble centers for mapping.
    Each row = one question, each col = one option (A–D).
    """
    grid = {}
    for q in range(rows):
        grid[q] = []
        for o in range(cols):
            x = start_x + o * dx
            y = start_y + q * dy
            grid[q].append((x, y))  # Option A–D
    return grid
