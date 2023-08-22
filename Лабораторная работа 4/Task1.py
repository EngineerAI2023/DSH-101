# TODO решите задачу
import json

def task() -> float:
    total = 0
    for d in data:
        score = d['score']
        weight = d['weight']
        total += score * weight
    return total


with open('data.json', 'r') as f:
    data = json.load(f)

print(round(task().3))