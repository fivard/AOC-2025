import time

is_simple_example = False


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    ranges = [list(map(int, line.split("-"))) for line in file.read().split(",")]

def _is_invalid_number(number: int) -> bool:
    str_num = str(number)
    length = len(str_num)
    # print(f" {length}")
    for i in range(1, length // 2 + 1):
        if length % i != 0:
            continue
        parts = [str_num[j:j + i] for j in range(0, length, i)]
        # print(f" {parts}")

        if len(set(parts)) == 1:
            return True

    return False

res = 0

for _range in ranges:
    start, end = _range[0], _range[1]
    # print(f"Processing range: {start}-{end}")
    for i in range(start, end + 1):
        if _is_invalid_number(number=i):
            # print(f" Found matching number: {i}")
            res += i

print("Total:", res)