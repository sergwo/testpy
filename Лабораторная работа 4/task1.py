# TODO решите задачу
import json
FILE="input.json"
def task() -> float:
    with open(FILE, "r") as src:
        src_json = json.load(src)
        res = round(sum(map(lambda item: item["score"] * item["weight"], src_json)),3)
        return res

print(task())
