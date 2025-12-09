import math
from collections import Counter

is_simple_example = False

red_titles = []
all_possible_areas = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    red_titles = [list(map(int, line.strip().split(","))) for line in lines]

for i in range(len(red_titles)):
    for j in range(i + 1, len(red_titles)):
        x1, y1 = red_titles[i]
        x2, y2 = red_titles[j]
        area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
        all_possible_areas.append([area, (i, j)])

all_possible_areas.sort(reverse=True)

def does_line_intersect_rect(start_line, end_line, rect_edge1, rect_edge2):
    y1, x1 = start_line
    y2, x2 = end_line
    ry1, rx1 = rect_edge1
    ry2, rx2 = rect_edge2

    y_min, y_max, x_min, x_max = min(y1, y2), max(y1, y2), min(x1, x2), max(x1, x2)
    rect_y_min, rect_y_max, rect_x_min, rect_x_max = min(ry1, ry2), max(ry1, ry2), min(rx1, rx2), max(rx1, rx2)

    return not (
        x_max <= rect_x_min
        or rect_x_max <= x_min
        or y_max <= rect_y_min
        or rect_y_max <= y_min
    )

def find_valid_area():
    for area_, [first_title_index, second_title_index] in all_possible_areas:
        # print(area, first_title_index, second_title_index)
        has_intersection = False
        for k in range(1, len(red_titles)):
            if does_line_intersect_rect(
                start_line=red_titles[k],
                end_line=red_titles[k-1],
                rect_edge1=red_titles[first_title_index],
                rect_edge2=red_titles[second_title_index],
            ):
                has_intersection = True
                break
        if not has_intersection:
            return area_, red_titles[first_title_index], red_titles[second_title_index]
    return None


print(find_valid_area())



