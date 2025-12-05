#!/usr/bin/env python3

with open("../data/day5_input.txt") as f:
    lines = f.readlines()

database = []
fresh_counter = 0
def is_fresh(id):
    for begin, end in database:
        if id>=begin and id<=end:
            return True
    return False


ingredients = False
for line in lines:
    if line.strip() == "":
        ingredients = True
        continue
    if ingredients:
        fresh_counter+=is_fresh(int(line.rstrip()))
    else:
        begin, end = line.rstrip().split("-")
        database.append((int(begin), int(end)))

print(fresh_counter)