from utils import *
import copy

is_simple_example = False

segments = []
nums_to_check = []

with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    line = lines[0].strip()
    i = 0

    while line != "":
        segments.append(list(map(int, line.split("-"))))
        i += 1
        line = lines[i].strip()

    i += 1
    for j in range(i, len(lines)):
        nums_to_check.append(int(lines[j].strip()))


def sort_and_merge_segments():
    global segments
    segments.sort()
    for i in range(1, len(segments)):
        if segments[i][0] <= segments[i - 1][1] + 1:
            segments[i - 1][1] = max(segments[i - 1][1], segments[i][1])
            segments[i] = segments[i - 1]

    segments = list(set([tuple(segment) for segment in segments]))
    segments.sort()

def bin_search(num, left, right):
    if left > right:
        return False

    mid = (left + right) // 2
    seg = segments[mid]

    if seg[0] <= num <= seg[1]:
        return True
    elif num < seg[0]:
        return bin_search(num, left, mid - 1)
    else:
        return bin_search(num, mid + 1, right)

sum_ = 0

sort_and_merge_segments()
for num in nums_to_check:
    if bin_search(num, 0, len(segments) - 1):
        sum_ += 1

print("res: ", sum_)
