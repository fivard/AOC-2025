from utils import *
import copy

is_simple_example = True

grid = []

with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    for line in file.readlines():
        grid.append(list(line.strip()))

new_map = copy.deepcopy(grid)

def has_less_than_4_adj_rolls(x, y):
    rolls = 0
    for direction in ALL_DIRECTIONS:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] == "@":
                rolls += 1

    if rolls < 4:
        new_map[x][y] = "x"
        return True

    return False

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            res += int(has_less_than_4_adj_rolls(i, j))

beautiful_print(new_map)
print("Res: ", res)

