is_simple_example = False
lines = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.read().splitlines()

# print(lines)

start_number = 50
res = 0

for line in lines:
    direction, count = line[0], int(line[1:])

    if direction == "R":
        start_number = (start_number + count) % 100
    elif direction == "L":
        start_number = (start_number - count) % 100

    if start_number == 0:
        res += 1

print(res)