import streamlit as st
import numpy as np
import cv2

from utils.parameter_loader import load_parameters
from omr_parser import extract_responses
from answer_key_loader import load_answer_key
from result_evaluator import evaluate_responses
from excel_exporter import export_to_excel
from validator_module import validate_sheet, poetic_feedback
from admin_panel import launch_admin_panel
from utils.ocr_utils import extract_metadata
from utils.bubble_debug_overlay import draw_detected_bubbles

# After bubble detection
detected_bubbles = extracted.get("bubbles", [])  # You’ll need to return this from extract_responses
missing_count = parameters["expected_questions"] - len(responses)

debug_img = draw_detected_bubbles(img.copy(), detected_bubbles, missing_count)
st.image(debug_img, caption="🧪 Bubble Detection Overlay")


# 🌟 Page setup
st.set_page_config(page_title="OMR Result Generator", layout="wide")
st.title("📄 OMR Result Generator")

# 📂 Sidebar Uploads
with st.sidebar:
    uploaded_params = st.file_uploader("Upload parameters.yaml", type=["yaml", "yml"])
    uploaded_files = st.file_uploader("Upload OMR Sheets", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# 🧠 Load Parameters
if uploaded_params:
    parameters = load_parameters(uploaded_params)
    st.success("✅ parameters.yaml loaded.")
else:
    st.warning("⚠️ Please upload parameters.yaml.")
    parameters = load_parameters(None)

# 🌈 Dynamic Splash Screen
st.markdown(f"### 🌟 Welcome to {parameters['school_name']} OMR Showcase!")

# 🧮 Load Answer Key
answer_key = load_answer_key()

# 📊 Process Uploaded Sheets
if uploaded_files:
    results = []

    for file in uploaded_files:
        file.seek(0)
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            st.error(f"❌ Failed to decode image: {file.name}")
            continue

        extracted = extract_responses(img)
        metadata = extract_metadata(img)
        responses = extracted["responses"]

        issues = validate_sheet(responses)
        poetic_feedback(issues)

        evaluation = evaluate_responses(responses, answer_key)
        result = {
            "Name": metadata["name"],
            "Roll No": metadata["roll_no"],
            "Score": evaluation["score"]
        }
        results.append(result)

    if results:
        st.success(f"✅ Processed {len(results)} students")
        export_to_excel(results)
        with open("class_results.xlsx", "rb") as f:
            st.download_button("📥 Download Excel", f, file_name=parameters.get("export_filename", "class_results.xlsx"))

        # 🧑‍🏫 Launch Admin Panel with badge theme
        launch_admin_panel(results, theme=parameters.get("badge_theme", "constellation"))

# import streamlit as st
# import numpy as np
# import cv2
# from utils.parameter_loader import load_parameters

# from omr_parser import extract_responses
# from answer_key_loader import load_answer_key
# from result_evaluator import evaluate_responses
# from excel_exporter import export_to_excel
# from validator_module import validate_sheet, poetic_feedback
# from admin_panel import launch_admin_panel
# from utils.ocr_utils import extract_metadata


# st.set_page_config(page_title="OMR Result Generator", layout="wide")
# st.title("📄 OMR Result Generator")


# uploaded_params = st.file_uploader("Upload parameters.yaml", type=["yaml", "yml"])
# parameters = load_parameters(uploaded_params)



# uploaded_files = st.file_uploader(
#     "Upload OMR Sheets", type=["jpg", "jpeg", "png"], accept_multiple_files=True
# )
# answer_key = load_answer_key()

# if uploaded_files:
#     results = []

#     for file in uploaded_files:
#         file.seek(0)
#         file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
#         img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

#         if img is None:
#             st.error(f"❌ Failed to decode image: {file.name}")
#             continue

#         extracted = extract_responses(img)
#         metadata = extract_metadata(img)
#         responses = extracted["responses"]

#         issues = validate_sheet(responses)
#         poetic_feedback(issues)

#         evaluation = evaluate_responses(responses, answer_key)
#         result = {
#             "Name": metadata["name"],
#             "Roll No": metadata["roll_no"],
#             "Score": evaluation["score"]
#         }
#         results.append(result)

#     if results:
#         st.success(f"✅ Processed {len(results)} students")
#         export_to_excel(results)
#         with open("class_results.xlsx", "rb") as f:
#             st.download_button("📥 Download Excel", f, file_name="class_results.xlsx")

#         launch_admin_panel(results)
