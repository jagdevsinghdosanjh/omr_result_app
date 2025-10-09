# utils/bubble_validator.py

import cv2

def validate_bubbles(bubbles, expected_count=None, actual_count=None):
    malformed = [b for b in bubbles if len(b) != 3]
    valid = [b for b in bubbles if len(b) == 3]

    summary = {
        "valid": len(valid),
        "malformed": len(malformed),
        "missing": expected_count - actual_count if expected_count and actual_count is not None else None
    }

    return summary

# def validate_bubbles(bubbles, expected_count=None, actual_count=None):
#     malformed = [b for b in bubbles if len(b) != 3]
#     valid = [b for b in bubbles if len(b) == 3]

#     summary = {
#         "valid": len(valid),
#         "malformed": len(malformed),
#         "missing": expected_count - actual_count if expected_count and actual_count is not None else None
#     }

#     return summary

# def validate_bubbles(bubbles, expected_count=None):
#     """
#     Logs malformed bubbles and returns a poetic summary.
#     """
#     malformed = [b for b in bubbles if len(b) != 3]
#     valid = [b for b in bubbles if len(b) == 3]

#     summary = {
#         "valid": len(valid),
#         "malformed": len(malformed),
#         "missing": max(0, expected_count - len(valid)) if expected_count else None
#     }

#     return summary

def draw_validation_overlay(img, bubbles, summary):
    overlay = img.copy()

    for b in bubbles:
        if len(b) == 3:
            x, y, r = b
            cv2.circle(overlay, (x, y), r, (0, 255, 0), 2)
        else:
            x, y = b[:2] if len(b) >= 2 else (30, 30)
            cv2.circle(overlay, (x, y), 10, (0, 0, 255), 2)

    if summary.get("missing", 0) > 0:
        poetic_text = f"{summary['missing']} bubbles drifted into silence.\nLet clarity guide the next scan."
        cv2.putText(overlay, poetic_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    return overlay


# def draw_validation_overlay(img, bubbles, summary):
#     """
#     Overlays green circles for valid bubbles, red for malformed.
#     Adds poetic annotation for missing bubbles.
#     """
#     overlay = img.copy()

#     for b in bubbles:
#         if len(b) == 3:
#             x, y, r = b
#             cv2.circle(overlay, (x, y), r, (0, 255, 0), 2)
#         else:
#             x, y = b[:2] if len(b) >= 2 else (30, 30)
#             cv2.circle(overlay, (x, y), 10, (0, 0, 255), 2)

#     if summary.get("missing", 0) > 0:
#         poetic_text = f"{summary['missing']} bubbles drifted into silence.\nLet clarity guide the next scan."
#         cv2.putText(overlay, poetic_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

#     return overlay
