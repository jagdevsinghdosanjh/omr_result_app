# Flags incomplete or ambiguous sheets
import streamlit as st

def validate_sheet(responses, expected_questions=90):
    issues = []

    if len(responses) < expected_questions:
        issues.append(f"🕳️ Missing responses: {expected_questions - len(responses)} questions unanswered.")

    duplicates = [q for q, v in responses.items() if isinstance(v, list) and len(v) > 1]
    if duplicates:
        issues.append(f"🔁 Multiple bubbles detected in: {duplicates}")

    return issues

def poetic_feedback(issues):
    if not issues:
        return "✨ All bubbles aligned. The sheet sings in clarity."

    st.markdown("> _“Some bubbles wandered, some stayed shy—\nLet’s guide them gently, before they fly.”_")
    for issue in issues:
        st.warning(issue)
