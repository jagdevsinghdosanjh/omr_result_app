# Compares student responses and scores
def evaluate_responses(student_responses, answer_key):
    score = 0
    correct = {}
    incorrect = {}

    for q_no, selected in student_responses.items():
        correct_ans = answer_key.get(q_no)
        if selected == correct_ans:
            score += 1
            correct[q_no] = selected
        else:
            incorrect[q_no] = selected

    return {
        "score": score,
        "correct": correct,
        "incorrect": incorrect
    }
