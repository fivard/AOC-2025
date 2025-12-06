import math

is_simple_example = False

sum_ = 0

with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    line_len = len(lines[0][:-1])
    problem = []
    for i in range(line_len-1, -1, -1):
        num = (lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]).replace(" ", "")
        if num == '':
            continue

        op = lines[4][i]
        # op = lines[3][i] if i < len(lines[3]) else ' '
        problem.append(int(num))
        if op != ' ':
            print(problem, op)
            sum_ += math.prod(problem) if op == '*' else sum(problem)
            problem = []


print("res: ", sum_)
