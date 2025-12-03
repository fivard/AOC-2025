is_simple_example = False


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    banks = [list(map(int, list(line.strip()))) for line in file.readlines()]

sum_ = 0
bank_len = len(banks[0])

for bank in banks:
    first_elem, second_elem = 0, 0
    first_elem_ind, second_elem_ind = -1, -1

    for index_of_battery in range(bank_len - 1):
        if bank[index_of_battery] > first_elem:
            first_elem, first_elem_ind = bank[index_of_battery], first_elem_ind
            second_elem, second_elem_ind = bank[index_of_battery + 1], index_of_battery + 1
            continue

        if bank[index_of_battery+1] > second_elem:
            second_elem, second_elem_ind = bank[index_of_battery+1], index_of_battery + 1

    sum_ += first_elem * 10 + second_elem

print(sum_)