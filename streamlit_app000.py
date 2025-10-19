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
from utils.bubble_validator import validate_bubbles, draw_validation_overlay
from utils.grid_mapper import generate_question_grid, draw_grid_overlay

# Page setup
st.set_page_config(page_title="OMR Result Generator", layout="wide")
st.title("📄 OMR Result Generator")

# Sidebar Uploads
with st.sidebar:
    uploaded_params = st.file_uploader("Upload parameters.yaml", type=["yaml", "yml"])
    uploaded_files = st.file_uploader("Upload OMR Sheets", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Load Parameters
if uploaded_params:
    parameters = load_parameters(uploaded_params)
    st.success("✅ parameters.yaml loaded.")
else:
    st.warning("⚠️ Please upload parameters.yaml.")
    parameters = load_parameters(None)

# Dynamic Splash Screen
st.markdown(f"### Welcome to **{parameters['school_name']}** OMR Showcase!")

# Load Answer Key
answer_key = load_answer_key()

# Process Uploaded Sheets
if uploaded_files:
    results = []
    expected = parameters.get("expected_questions", 108)

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
        bubbles = extracted.get("bubbles", [])
        actual = len(responses)
        missing = expected - actual

        # Bubble Validation Overlay
        summary = validate_bubbles(bubbles, expected_count=expected, actual_count=actual)
        debug_img = draw_validation_overlay(img.copy(), bubbles, summary)
        st.image(debug_img, caption=f"🧪 Bubble Validation Overlay for {metadata['name']}")

        # Student Header
        st.markdown(f"#### 🎓 Student: **{metadata['name']}** | Roll No: **{metadata['roll_no']}**")

        # Poetic Feedback
        if missing > 0:
            st.markdown(f"""
> *Some bubbles wandered, some stayed shy —  
Let’s guide them gently, before they fly.*  
🕳️ **Missing responses:** {missing}
""")
        else:
            st.success("✅ All responses captured with clarity!")

        # Validation + Feedback
        issues = validate_sheet(responses, expected_questions=expected)
        poetic_feedback(issues)

        # Evaluation
        evaluation = evaluate_responses(responses, answer_key)
        result = {
            "Name": metadata["name"],
            "Roll No": metadata["roll_no"],
            "Score": evaluation["score"]
        }
        results.append(result)

    # Export + Admin Panel
    if results:
        st.success(f"✅ Processed {len(results)} students")
        export_to_excel(results)
        with open("class_results.xlsx", "rb") as f:
            st.download_button("📥 Download Excel", f, file_name=parameters.get("export_filename", "class_results.xlsx"))
        launch_admin_panel(results)

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
# from utils.bubble_validator import validate_bubbles, draw_validation_overlay

# # 🌟 Page setup
# st.set_page_config(page_title="OMR Result Generator", layout="wide")
# st.title("📄 OMR Result Generator")

# # 📂 Sidebar Uploads
# with st.sidebar:
#     uploaded_params = st.file_uploader("Upload parameters.yaml", type=["yaml", "yml"])
#     uploaded_files = st.file_uploader("Upload OMR Sheets", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# # 🧠 Load Parameters
# if uploaded_params:
#     parameters = load_parameters(uploaded_params)
#     st.success("✅ parameters.yaml loaded.")
# else:
#     st.warning("⚠️ Please upload parameters.yaml.")
#     parameters = load_parameters(None)

# # 🌈 Dynamic Splash Screen
# st.markdown(f"### 🌟 Welcome to {parameters['school_name']} OMR Showcase!")

# # 🧮 Load Answer Key
# answer_key = load_answer_key()

# # 📊 Process Uploaded Sheets
# if uploaded_files:
#     results = []
#     expected = parameters.get("expected_questions", 108)

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
#         bubbles = extracted.get("bubbles", [])

#         actual = len(responses)
#         missing = expected - actual

#         # 🧪 Bubble Validation Overlay
#         summary = validate_bubbles(bubbles, expected_count=expected, actual_count=actual)
#         debug_img = draw_validation_overlay(img.copy(), bubbles, summary)
#         st.image(debug_img, caption=f"🧪 Bubble Validation Overlay for {metadata['name']}")

#         # 🎓 Student Header
#         st.markdown(f"#### 🎓 Student: {metadata['name']} | Roll No: {metadata['roll_no']}")

#         # 🌈 Poetic Feedback
#         if missing > 0:
#             st.markdown(f"""
#             > ✨ *Some bubbles wandered, some stayed shy —  
#             > Let’s guide them gently, before they fly.*  
#             > **Missing responses:** {missing}
#             """)
#         else:
#             st.success("🌟 All responses captured with clarity!")

#         # 🧠 Validation + Feedback
#         issues = validate_sheet(responses)
#         poetic_feedback(issues)

#         # 🧮 Evaluation
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
#             st.download_button("📥 Download Excel", f, file_name=parameters.get("export_filename", "class_results.xlsx"))

#         # 🧑‍🏫 Launch Admin Panel
#         launch_admin_panel(results)
