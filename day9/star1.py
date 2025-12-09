import math
from collections import Counter

is_simple_example = False

red_titles = []
all_possible_areas = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    red_titles = [list(map(int, line.strip().split(","))) for line in lines]

# print(red_titles)

for i in range(len(red_titles)):
    for j in range(i + 1, len(red_titles)):
        x1, y1 = red_titles[i]
        x2, y2 = red_titles[j]
        area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
        all_possible_areas.append([area, (red_titles[i], red_titles[j])])

all_possible_areas.sort()

# for area in all_possible_areas:
#     print(area)
print(all_possible_areas[-1][0])



