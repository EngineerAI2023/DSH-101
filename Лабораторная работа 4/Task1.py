# TODO решите задачу
import json

def task() -> float:
    for d in data:
        values = [d['score'] * d['weight'] for d in data]
        total = sum(values)
    return total


with open('data.json', 'r') as f:
    data = json.load(f)

print(round(task().3))