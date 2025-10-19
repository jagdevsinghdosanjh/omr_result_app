def evaluate_responses(student_responses, answer_key_bundle, grading_scheme="standard", subject_weights=None):
    """
    Compares student responses to the answer key.
    Supports standard and weighted scoring.
    Returns score, correct/incorrect maps, and subject-wise breakdown.
    """
    flat_key = answer_key_bundle.get("flat", {})
    subject_map = answer_key_bundle.get("subject_map", {})

    score = 0
    correct = {}
    incorrect = {}
    subject_scores = {}

    for q_no, selected in student_responses.items():
        correct_ans = flat_key.get(q_no)
        subject = subject_map.get(q_no, "General")
        weight = subject_weights.get(subject, 1.0) if grading_scheme == "weighted" else 1.0

        if selected == correct_ans:
            score += weight
            correct[q_no] = selected
            subject_scores[subject] = subject_scores.get(subject, 0) + weight
        else:
            incorrect[q_no] = selected

    return {
        "score": round(score, 2),
        "correct": correct,
        "incorrect": incorrect,
        "subject_scores": subject_scores
    }


# # Compares student responses and scores
# def evaluate_responses(student_responses, answer_key):
#     score = 0
#     correct = {}
#     incorrect = {}

#     for q_no, selected in student_responses.items():
#         correct_ans = answer_key.get(q_no)
#         if selected == correct_ans:
#             score += 1
#             correct[q_no] = selected
#         else:
#             incorrect[q_no] = selected

#     return {
#         "score": score,
#         "correct": correct,
#         "incorrect": incorrect
#     }
