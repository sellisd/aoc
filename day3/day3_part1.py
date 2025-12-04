#!/usr/bin/env python3
import re

def max_joltage(line):
    for i in range(99, 1, -1):
        j = str(i)
        pattern = f"{j[0]}.*{j[1]}"
        m = re.search(pattern, line)
        if m:
            return(i)
    exit(1)

total_joltage = 0
with open("../data/day3_input.txt") as f:
    for line in f:
        line = line.strip()
        j = max_joltage(line)
        total_joltage += j
print(f"Total joltage: {total_joltage}")