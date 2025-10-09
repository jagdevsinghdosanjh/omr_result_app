# utils/bubble_debug_overlay.py
import cv2

def draw_detected_bubbles(img, bubbles, missing_count=0):
    """
    Draws circles around detected bubbles and overlays a poetic message.
    `bubbles` should be a list of (x, y, r) tuples.
    """
    overlay = img.copy()

    for (x, y, r) in bubbles:
        cv2.circle(overlay, (x, y), r, (0, 255, 0), 2)

    if missing_count > 0:
        poetic_text = f"{missing_count} bubbles drifted into silence.\nLet clarity guide the next scan."
        cv2.putText(overlay, poetic_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    return overlay
