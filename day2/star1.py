is_simple_example = False


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    ranges = [list(map(int, line.split("-"))) for line in file.read().split(",")]

sum = 0

for _range in ranges:
    start, end = _range[0], _range[1]
    if len(str(start)) % 2 != 0 and len(str(end)) % 2 != 0:
        continue
    print(f"Processing range: {start}-{end}")
    for i in range(start, end + 1):
        if len(str(i)) % 2 != 0:
            continue
        first_part = i // (10 ** (len(str(i)) // 2))
        second_part = i % (10 ** (len(str(i)) // 2))
        if first_part == second_part:
            print(f" Found matching number: {i}")
            sum += i

print("Total:", sum)