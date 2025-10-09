from utils.grid_mapper import generate_question_grid
from utils.image_utils import detect_bubbles, map_bubbles_to_responses
from utils.image_utils import preprocess_image

def extract_responses(img):
    _, thresh = preprocess_image(img)
    bubbles = detect_bubbles(thresh)

    question_grid = generate_question_grid(
        start_x=100, start_y=200, dx=40, dy=30,
        rows=50, cols=4
    )

    responses = map_bubbles_to_responses(bubbles, question_grid)
    return {"responses": responses, "bubbles": bubbles}




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
