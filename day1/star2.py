# is_simple_example = True
is_simple_example = False
lines = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.read().splitlines()

start_number = 50
res = 0

for line in lines:
    direction, count = line[0], int(line[1:])
    temp_res = 0

    if direction == "R":
        if start_number + count >= 100:
            temp_res += (start_number + count) // 100
            print(f"{direction}{count}, {start_number} + {count} = {start_number + count}, added: {temp_res}")
        start_number = (start_number + count) % 100
    elif direction == "L":
        if start_number - count <= 0:
            temp_res += abs((start_number - count) // 100) if (start_number - count) % 100 != 0 else abs((start_number - count) // 100) + 1
            if start_number == 0:
                temp_res -= 1
            print(f"{direction}{count}, {start_number} - {count} = {start_number - count}, added: {temp_res}")
        start_number = (start_number - count) % 100

    res += temp_res

print(res)