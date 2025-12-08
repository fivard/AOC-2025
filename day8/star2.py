import math
from collections import Counter

is_simple_example = False

current_available_circuit = 1


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    boxes = [list(map(int, line.strip().split(","))) for line in lines]


circuts = {i: i for i in range(1, len(boxes))}
print(circuts)

def distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

sorted_boxes = []

for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        sorted_boxes.append([distance(boxes[i], boxes[j]), i, j])

sorted_boxes.sort()
# print(sorted_boxes)
for dist, i, j in sorted_boxes:
    box1_circuit = circuts.get(i, None)
    box2_circuit = circuts.get(j, None)

    if box1_circuit is None and box2_circuit is None:
        circuts[i] = current_available_circuit
        circuts[j] = current_available_circuit
        current_available_circuit += 1
    elif box1_circuit is not None and box2_circuit is None:
        circuts[j] = box1_circuit
    elif box1_circuit is None and box2_circuit is not None:
        circuts[i] = box2_circuit
    elif box1_circuit != box2_circuit:
        to_replace = box2_circuit
        for key in circuts:
            if circuts[key] == to_replace:
                circuts[key] = box1_circuit

    if len(Counter(circuts.values()).most_common(2)) == 1:
        print(boxes[i])
        print(boxes[j])
        print(circuts)
        print("Res, ", boxes[i][0] * boxes[j][0])
        break
