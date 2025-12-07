import math

is_simple_example = True

current_streams = set()
list_of_splitters = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    current_streams.add(lines[0].find("S"))
    for line in lines[1:]:
        cur_splitter = {i for i in range(len(line)) if line[i] == "^"}
        list_of_splitters.append(cur_splitter)

sum_ = 0

for splitters in list_of_splitters:
    if not splitters:
        continue

    for stream in current_streams.copy():
        if stream in splitters:
            sum_ += 1
            current_streams.remove(stream)
            current_streams.add(stream+1)
            current_streams.add(stream-1)
            print(f"Met splitter at {stream}, new streams: {current_streams}")

print(sum_)
