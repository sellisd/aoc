#!/usr/bin/env python3

with open("../data/day6_input.txt") as f:
    data = f.readlines()

operations = data[-1].rstrip().split()

splitted = []
for row in data[:-1]:
    splitted.append(row.rstrip().split())
grand_total = 0
for x in range(len(splitted[0])):
    sum = 0
    prod = 1
    for y in splitted:
        print(y[x], end=" ")
        if operations[x] == "+":
            sum+=int(y[x])
        elif operations[x] == "*":
            prod *= int(y[x])
        else:
            exit(1)
    if operations[x] == "+":
        grand_total += sum
    elif operations[x] == "*":
        grand_total += prod
    print(f"=> Sum: {sum}, Prod: {prod}")
print(f"Grand Total: {grand_total}")