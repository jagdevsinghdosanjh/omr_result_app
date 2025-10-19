import json

def load_answer_key(path="data/answer_key.json") -> dict:
    """
    Loads and flattens the answer key JSON.
    Returns a dictionary: {question_number: correct_option_index}
    Also supports subject-wise mapping for future badge logic.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        print("❌ answer_key.json not found.")
        return {}
    except json.JSONDecodeError:
        print("⚠️ Malformed answer_key.json.")
        return {}

    flat_key = {}
    subject_map = {}

    for subject, block in raw.items():
        answers = block.get("answers", {})
        for q_str, ans_str in answers.items():
            try:
                q_no = int(q_str)
                ans_idx = int(ans_str)
                flat_key[q_no] = ans_idx
                subject_map[q_no] = subject
            except ValueError:
                print(f"⚠️ Skipping malformed entry: {q_str} → {ans_str}")

    print(f"✅ Loaded {len(flat_key)} answers across subjects")
    return {
        "flat": flat_key,
        "subject_map": subject_map
    }


# # Loads and flattens answer key JSON
# import json

# def load_answer_key(path="data/answer_key.json") -> dict:
#     with open(path, "r") as f:
#         raw = json.load(f)

#     flat_key = {}
#     for subject_block in raw.values():
#         flat_key.update(subject_block["answers"])
#     return {int(k): int(v) for k, v in flat_key.items()}
