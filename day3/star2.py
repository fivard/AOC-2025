is_simple_example = False


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    banks = [list(map(int, list(line.strip()))) for line in file.readlines()]

sum_ = 0
bank_len = len(banks[0])

for bank in banks:
    joltage = 0
    cur_num, cur_ind, prev_ind = 0, 0, 0
    for i in range(11, -1, -1):
        for index_of_battery in range(prev_ind, bank_len - i):
            if bank[index_of_battery] > cur_num:
                cur_num, cur_ind = bank[index_of_battery], index_of_battery

        joltage = joltage * 10 + cur_num
        prev_ind = cur_ind + 1
        cur_num = 0

    sum_ += joltage

print(sum_)