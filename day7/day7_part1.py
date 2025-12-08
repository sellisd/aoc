#!/usr/bin/env python3
import re

def draw_line(line, indexes):
    for n, i in enumerate(line):
        if n in indexes:
            print("|", end="")
        else:
            print(i, end="")

with open("../data/day7_input.txt") as f:
    lines = f.readlines()

entrypoint = lines[0].find("S")
indexes = {}
indexes[entrypoint] = 1
tachyon_splits = 0
for line in lines[1:]:
    to_process = []
    for i, v in enumerate(line.strip()):
        if v == "^" and i in indexes:
            tachyon_splits += 1
            to_process.append(i)
    for i in to_process:
        indexes[i-1] = 1
        indexes[i+1] = 1
        del indexes[i]
    draw_line(line, indexes)


print(f"\nTachyon splits: {tachyon_splits}")