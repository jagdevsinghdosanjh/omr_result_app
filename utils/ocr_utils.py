import pytesseract
import re
import cv2

# Explicit fallback path for Windows systems
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_metadata(img):
    """
    Extracts student name and roll number from a decoded OpenCV image.
    Focuses on top region and uses flexible regex matching.
    Returns a dictionary with metadata.
    """
    # Crop top region for OCR focus
    header_crop = img[0:250, :]  # Top 250 pixels
    gray = cv2.cvtColor(header_crop, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    name = ""
    roll_no = ""

    # Normalize and split lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    for line in lines:
        # Match variations like "Name: XYZ", "Student Name - XYZ", "Name XYZ"
        name_match = re.search(r"(Name|Student Name)[:\-]?\s*([A-Z\s]{3,})", line, re.IGNORECASE)
        roll_match = re.search(r"(Roll\s*No|Roll Number)[:\-]?\s*(\d{1,6})", line, re.IGNORECASE)

        if name_match and not name:
            name = name_match.group(2).strip()
        if roll_match and not roll_no:
            roll_no = roll_match.group(2).strip()

    # Fallback if not found
    if not name:
        name = "Unknown"
    if not roll_no:
        roll_no = "0000"

    print(f"📋 OCR Extracted — Name: {name}, Roll No: {roll_no}")
    return {"name": name, "roll_no": roll_no}
