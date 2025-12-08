#!/usr/bin/env python3

def append_path(paths, new_index):
    to_add = []
    for n, i in enumerate(paths):
        if i[-1] == new_index:
            to_add.append(n)
    for i in to_add:
        to_extend = paths[i].copy()
        to_extend.append(new_index-1)
        paths[i].append(new_index+1)
        paths.append(to_extend)
    return paths


with open("../data/day7_input.txt") as f:
    lines = f.readlines()


indexes = {}
entrypoint = lines[0].find("S")
indexes[entrypoint] = True
paths = [[entrypoint]]
for n, line in enumerate(lines[1:]):
    print(f"{len(paths)} {n}/{len(lines)}")
    to_process = []
    for i in indexes:
        if line[i] == "^":
            to_process.append(i)
            paths = append_path(paths, i)
    for i in to_process:
        del indexes[i]
        indexes[i-1] = True
        indexes[i+1] = True

print(len(paths))
