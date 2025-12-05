from utils import *
import copy

is_simple_example = False

segments = []

with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    line = lines[0].strip()
    i = 0

    while line != "":
        segments.append(list(map(int, line.split("-"))))
        i += 1
        line = lines[i].strip()


def sort_and_merge_segments():
    global segments
    segments.sort()
    for i in range(1, len(segments)):
        if segments[i][0] <= segments[i - 1][1] + 1:
            segments[i - 1][1] = max(segments[i - 1][1], segments[i][1])
            segments[i] = segments[i - 1]

    segments = list(set([tuple(segment) for segment in segments]))
    segments.sort()

sum_ = 0

sort_and_merge_segments()
for segment in segments:
    sum_ += segment[1] - segment[0] + 1

print("res: ", sum_)
