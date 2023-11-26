# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
    result = sum([item['score'] * item['weight'] for item in data])
    return round(result, 3)


print(task())
