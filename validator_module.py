import streamlit as st

def validate_sheet(responses, expected_questions=108):
    """
    Flags missing or ambiguous responses.
    Returns a list of issue strings for feedback.
    """
    issues = []

    # Missing responses
    missing_count = expected_questions - len(responses)
    if missing_count > 0:
        issues.append(f"🕳️ Missing responses: {missing_count} questions unanswered.")

    # Ambiguous bubbles (multiple options marked for same question)
    duplicates = [q for q, v in responses.items() if isinstance(v, list) and len(v) > 1]
    if duplicates:
        issues.append(f"⚠️ Multiple bubbles detected in: {duplicates}")

    return issues

def poetic_feedback(issues):
    """
    Displays poetic feedback based on validation issues.
    """
    if not issues:
        st.success("🎶 All bubbles aligned. The sheet sings in clarity.")
        return

    st.markdown("> *Some bubbles wandered, some stayed shy —\nLet’s guide them gently, before they fly.*")

    for issue in issues:
        st.warning(issue)

# # Flags incomplete or ambiguous sheets
# import streamlit as st

# def validate_sheet(responses, expected_questions=90):
#     issues = []

#     if len(responses) < expected_questions:
#         issues.append(f"🕳️ Missing responses: {expected_questions - len(responses)} questions unanswered.")

#     duplicates = [q for q, v in responses.items() if isinstance(v, list) and len(v) > 1]
#     if duplicates:
#         issues.append(f"🔁 Multiple bubbles detected in: {duplicates}")

#     return issues

# def poetic_feedback(issues):
#     if not issues:
#         return "✨ All bubbles aligned. The sheet sings in clarity."

#     st.markdown("> _“Some bubbles wandered, some stayed shy—\nLet’s guide them gently, before they fly.”_")
#     for issue in issues:
#         st.warning(issue)
