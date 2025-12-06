import math

is_simple_example = False

problems = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        nums = line.strip().split()
        if len(problems) == 0:
            problems = [0] * len(nums)

        for i in range(len(nums)):
            if problems[i] == 0:
                problems[i] = []
            problems[i].append(int(nums[i]) if nums[i] not in ["*", "+"] else nums[i])

print(problems)


sum_ = 0

for problem in problems:
    sum_ += math.prod(problem[:-1]) if problem[-1] == "*" else sum(problem[:-1])

print("res: ", sum_)
