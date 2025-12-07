import math

is_simple_example = False

current_streams = {}
list_of_splitters = []


with open("example.txt" if not is_simple_example else "simple_example.txt", "r") as file:
    lines = file.readlines()
    current_streams[lines[0].find("S")] = 1
    for line in lines[1:]:
        cur_splitter = {i for i in range(len(line)) if line[i] == "^"}
        list_of_splitters.append(cur_splitter)

sum_ = 0

for splitters in list_of_splitters:
    if not splitters:
        continue

    for stream, occur in current_streams.copy().items():
        if stream in splitters:
            del current_streams[stream]
            current_streams[stream-1] = max(occur, current_streams.get(stream-1, 0) + occur)
            current_streams[stream+1] = max(occur, current_streams.get(stream+1, 0) + occur)
            # print(f"Met splitter at {stream}, new streams: {current_streams}")

print(sum(current_streams.values()))
