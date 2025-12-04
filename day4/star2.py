from utils import *

is_simple_example = False

grid = []

with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    for line in file.readlines():
        grid.append(list(line.strip()))


def has_less_than_4_adj_rolls(x, y):
    rolls = 0
    for direction in ALL_DIRECTIONS:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] == "@":
                rolls += 1

    if rolls < 4:
        grid[x][y] = "."
        return True

    return False


res = 0
temp_res = 0
while True:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                temp_res += int(has_less_than_4_adj_rolls(i, j))

    if temp_res == 0:
        break

    # beautiful_print(grid)
    # print("Temp res: ", temp_res)
    # print("\n-----------------------\n")
    res += temp_res
    temp_res = 0



# beautiful_print(grid)
print("Res: ", res)

