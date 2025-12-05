#!/usr/bin/env python3
from  loguru import logger

def add_entry(database, range):
    if database.get(range[0]):
        if range[1] > database[range[0]]:
            database[range[0]] = range[1]
    else:
        database[range[0]] = range[1]

def expand_range(database, range):
    database[range[0]]

def should_update_database(database, range: tuple[int, int]):
    logger.info(f"Database state: {database}")
    logger.info(f"Checking for updates for range: {range}")
    for begin, end in sorted(database.items()):
        logger.info(f"Comparing with range: {begin, end}")
        left, right = (begin, end)
        changed = False
        if range[0] < begin and range[1] >= begin:
            left = range[0]
            changed = True
        if range[1] > end and range[0] <= end:
            right = range[1]
            changed = True
        if changed:
            logger.info(f"returning range {left, right}")
            return (left, right), begin
    logger.info("No updates found")
    return None, None


with open("../data/day5_input.txt") as f:
    lines = f.readlines()

database = {}

# build database with ranges
for line in lines:
    if line.strip() == "":
        break
    else:
        begin, end = line.rstrip().split("-")
        add_entry(database, (int(begin), int(end)))

# find overlapping ranges
## TODO:
# 2. think if we need a second pass on values
counter = 0
logger.info(f"Initial database: {database}")
while True:
    current_range = sorted(database.items())[counter]
    logger.info(f"database: {database}")
    logger.info(f"{counter} Current range: {current_range}")
    new_range, key_to_delete = should_update_database(database, current_range)
    logger.info(f"New range: {new_range}, key to delete: {key_to_delete}")
    if new_range:
        del database[key_to_delete]
        add_entry(database, new_range)
    else:
        counter+=1
    if counter >= len(database):
        break

fresh = 0
for begin, end in database.items():
    logger.info(f"{begin}-{end} {end-begin+1} {fresh}")
    fresh+=end-begin+1
print(fresh)