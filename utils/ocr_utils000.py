import pytesseract
import re

# Explicit fallback path for Windows systems
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_metadata(img):
    """
    Extracts student name and roll number from a decoded OpenCV image.
    Returns a dictionary with metadata.
    """
    text = pytesseract.image_to_string(img)
    name = ""
    roll_no = ""

    # Normalize and split lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    for line in lines:
        # Match "Name: XYZ" or "Student Name - XYZ"
        name_match = re.search(r"(Name[:\-]?\s*)([A-Za-z\s]+)", line, re.IGNORECASE)
        roll_match = re.search(r"(Roll\s*No[:\-]?\s*)(\d+)", line, re.IGNORECASE)

        if name_match:
            name = name_match.group(2).strip()
        if roll_match:
            roll_no = roll_match.group(2).strip()

    # Fallback if not found
    if not name:
        name = "Unknown"
    if not roll_no:
        roll_no = "0000"

    print(f"📋 OCR Extracted — Name: {name}, Roll No: {roll_no}")
    return {"name": name, "roll_no": roll_no}

# # OCR logic for metadata extraction
# import pytesseract

# # Explicit fallback path for Windows systems
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def extract_metadata(img):
#     """
#     Extracts student name and roll number from a decoded OpenCV image.
#     Returns a dictionary with metadata.
#     """
#     text = pytesseract.image_to_string(img)

#     name = roll_no = ""
#     for line in text.split("\n"):
#         if "Name" in line:
#             name = line.split(":")[-1].strip()
#         elif "Roll" in line:
#             roll_no = line.split(":")[-1].strip()

#     return {"name": name, "roll_no": roll_no}
