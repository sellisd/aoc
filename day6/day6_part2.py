#!/usr/bin/env python3
from functools import reduce
from operator import mul

def ceph_operation(numbers, operator):
    if operator == "*":
        return reduce(mul,numbers)
    elif operator == "+":
        return sum(numbers)
    else:
        breakpoint()
        print(numbers, operator)
        exit(1)

with open("../data/day6_input.txt") as f:
    data = f.readlines()

grand_total = 0
numbers = []
for n, v in enumerate(data[-1]):
    if data[-1][n] in ["*", "+"]:
        operator = data[-1][n]
    number = ""
    for i in data[:-1]:
        number+=i[n]
    if number.isspace():
        grand_total += ceph_operation(numbers, operator)
        numbers=[]
    else:
        numbers.append(int(number.strip()))
    if n == len(data[0])-1:
        grand_total += ceph_operation(numbers, operator)

print(f"Grand_total {grand_total}")
