from utils.grid_mapper import generate_question_grid
from utils.image_utils import detect_bubbles, map_bubbles_to_responses, preprocess_image

def extract_responses(img):
    original, thresh = preprocess_image(img)
    bubbles = detect_bubbles(thresh)

    # Log bubble count
    print(f"🟢 Detected {len(bubbles)} bubbles")

    # Adjust grid parameters to match actual sheet layout
    question_grid = generate_question_grid(
        start_x=80,     # Calibrated X start
        start_y=180,    # Calibrated Y start
        dx=38,          # Horizontal spacing
        dy=28,          # Vertical spacing
        rows=54,        # Total questions
        cols=2          # Options A-D
    )

    responses = map_bubbles_to_responses(bubbles, question_grid, radius_tolerance=25)
    return {"responses": responses, "bubbles": bubbles}

# from utils.grid_mapper import generate_question_grid
# from utils.image_utils import detect_bubbles, map_bubbles_to_responses
# from utils.image_utils import preprocess_image

# def extract_responses(img):
#     _, thresh = preprocess_image(img)
#     bubbles = detect_bubbles(thresh)

#     question_grid = generate_question_grid(
#         start_x=100, start_y=200, dx=40, dy=30,
#         rows=50, cols=4
#     )

#     responses = map_bubbles_to_responses(bubbles, question_grid)
#     return {"responses": responses, "bubbles": bubbles}




# from utils.image_utils import preprocess_image, detect_bubbles
# def extract_responses(img):
#     _, thresh = preprocess_image(img)
#     responses, bubbles = detect_bubbles(thresh)
#     return {"responses": responses, "bubbles": bubbles}


# def extract_responses(img):
#     _, thresh = preprocess_image(img)
#     responses = detect_bubbles(thresh)
#     return {"responses": responses}

# from utils.image_utils import preprocess_image, detect_bubbles
# from utils.ocr_utils import extract_metadata

# def extract_responses(img):
#     """
#     Extracts student responses from a decoded OpenCV image.
#     Returns a dictionary with bubble responses.
#     """
#     _, thresh = preprocess_image(img)
#     responses = detect_bubbles(thresh)
#     return {"responses": responses}

# def extract_metadata(img):
#     """
#     Extracts student name and roll number from a decoded OpenCV image.
#     Returns a dictionary with metadata.
#     """
#     return extract_metadata(img)
