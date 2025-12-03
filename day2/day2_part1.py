#!/usr/bin/env python3
import re
def not_valid(string):
    if re.match("^0", string):
        return True
    return False

def is_valid(number):
    if len(number)%2 != 0:
        return True
    half = len(number)//2
    if number[0:half] == number[half:len(number)]:
        return False
    return True

invalid = 0
with open("../data/day2_input.txt") as f:
    lines = f.readline()
    ranges = lines.split(",")
    for r in ranges:
        start, end = r.split("-")
        if not_valid(start) or not_valid(end):
            exit(1)

        for i in range(int(start), int(end) + 1):
            if not is_valid(str(i)):
                invalid += i

print(invalid)