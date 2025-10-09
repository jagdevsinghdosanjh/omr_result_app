# utils/image_utils.py

import cv2
import numpy as np  # noqa

def preprocess_image(img):
    """
    Converts image to grayscale, applies Gaussian blur, and thresholds using Otsu's method.
    Returns the original image and binary thresholded image.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return img, thresh


def detect_bubbles(thresh):
    """
    Detects circular contours from a thresholded image.
    Returns a list of (x, y, r) tuples representing bubble centers and radii.
    """
    bubbles = []
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if len(cnt) >= 5:  # Ensure contour is valid for enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            if 5 < radius < 20:  # Filter by size
                bubbles.append((int(x), int(y), int(radius)))

    return bubbles


def map_bubbles_to_responses(bubbles, question_grid, radius_tolerance=15):
    """
    Maps detected bubbles to question options using proximity to grid centers.
    Returns a dictionary of responses: {question_number: selected_option_letter}.
    """
    responses = {}

    for q, options in question_grid.items():
        for idx, (x_ref, y_ref) in enumerate(options):
            for bubble in bubbles:
                if len(bubble) == 3:
                    x, y, r = bubble
                    dist = ((x - x_ref)**2 + (y - y_ref)**2)**0.5
                    if dist < radius_tolerance:
                        responses[q] = chr(65 + idx)  # A, B, C, D
                        break  # Stop after first match
                else:
                    print(f"⚠️ Skipping malformed bubble: {bubble}")
    return responses
