import cv2

def generate_question_grid(start_x, start_y, dx, dy, rows, cols):
    """
    Generates a grid of bubble centers for mapping.
    Each row = one question, each col = one option (A-D).
    Returns a dictionary: {question_index: [(x1, y1), (x2, y2), ...]}
    """
    grid = {}
    for q in range(rows):
        grid[q] = []
        for o in range(cols):
            x = start_x + o * dx
            y = start_y + q * dy
            grid[q].append((x, y))  # Option A-D
    return grid

def draw_grid_overlay(img, grid, radius=10):
    """
    Optional: Draws the generated grid on the image for visual calibration.
    Useful for debugging misalignment between grid and actual bubbles.
    """
    overlay = img.copy()
    for options in grid.values():
        for (x, y) in options:
            cv2.circle(overlay, (x, y), radius, (255, 0, 0), 1)  # Blue grid dots
    return overlay


# # utils/grid_mapper.py
# def generate_question_grid(start_x, start_y, dx, dy, rows, cols):
#     """
#     Generates a grid of bubble centers for mapping.
#     Each row = one question, each col = one option (A–D).
#     """
#     grid = {}
#     for q in range(rows):
#         grid[q] = []
#         for o in range(cols):
#             x = start_x + o * dx
#             y = start_y + q * dy
#             grid[q].append((x, y))  # Option A–D
#     return grid
