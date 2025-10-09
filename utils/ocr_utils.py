# OCR logic for metadata extraction
import pytesseract

# Explicit fallback path for Windows systems
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_metadata(img):
    """
    Extracts student name and roll number from a decoded OpenCV image.
    Returns a dictionary with metadata.
    """
    text = pytesseract.image_to_string(img)

    name = roll_no = ""
    for line in text.split("\n"):
        if "Name" in line:
            name = line.split(":")[-1].strip()
        elif "Roll" in line:
            roll_no = line.split(":")[-1].strip()

    return {"name": name, "roll_no": roll_no}
