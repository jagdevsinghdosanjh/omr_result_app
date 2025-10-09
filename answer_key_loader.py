# Loads and flattens answer key JSON
import json

def load_answer_key(path="data/answer_key.json") -> dict:
    with open(path, "r") as f:
        raw = json.load(f)

    flat_key = {}
    for subject_block in raw.values():
        flat_key.update(subject_block["answers"])
    return {int(k): int(v) for k, v in flat_key.items()}
