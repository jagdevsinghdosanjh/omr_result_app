import yaml
import streamlit as st

def load_parameters(uploaded_file=None):
    if uploaded_file:
        return yaml.safe_load(uploaded_file)
    try:
        with open("parameters.yaml", "r", encoding="utf-8") as f:  # ✅ Force UTF-8
            return yaml.safe_load(f)
    except FileNotFoundError:
        st.warning("⚠️ parameters.yaml not found. Using defaults.")
    except UnicodeDecodeError:
        st.error("❌ parameters.yaml contains invalid characters. Please save it as UTF-8.")
    return {
        "school_name": "Unnamed School",
        "grading_scheme": "standard",
        "leaderboard_limit": 10
    }
