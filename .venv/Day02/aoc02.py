import numpy

# Part 1
input_matrix = []

with open('../Day02/aoc02_input1', 'r') as f:
    for line in f.readlines():
        numbers = [int(x) for x in line.split()]  # For integers
        input_matrix.append(numbers)

increasing = False

safe_counter = 0

for item in input_matrix:

    lvl_diff_list = abs(numpy.diff(item))

    # check wether to check for increase or decrease
    if item[0] > item[1]:
        # only decreasing check
        res = all(i > j for i, j in zip(item, item[1:]))
    else:
        # only increase check
        res = all(i < j for i, j in zip(item, item[1:]))

    # check for level difference between 1 and 3
    lvl_diff = all(1 <= x <= 3 for x in lvl_diff_list)

    if res and lvl_diff: safe_counter += 1

print(safe_counter)

# Part 2
safe_counter = 0

for item in input_matrix:

    res = False
    changed_value = False
    lvl_diff_list = abs(numpy.diff(item))

    # check if only decreasing or increasing
    res = all(i > j for i, j in zip(item, item[1:])) or all(i < j for i, j in zip(item, item[1:]))

    if not res:
        # dampener rule
        for i in range(len(item)):
            # current element remove
            modified_item = item[:i] + item[i + 1:]

            # könnte man in methode auslagern
            if (all(x < y for x, y in zip(modified_item, modified_item[1:])) or
                    all(x > y for x, y in zip(modified_item, modified_item[1:]))):
                res = True
                changed_value = True
                break

    # check for level difference between 1 and 3 + dampener
    diff_counter = 0

    for foo in lvl_diff_list:
        if foo >= 4: diff_counter += 1

    lvl_diff = diff_counter <= 1 if not changed_value else diff_counter == 0

    # print(f"list: {item}, diff list: {lvl_diff_list}, oneway: {res}, difc: {diff_counter}, lvldiff: {lvl_diff}")

    if res and lvl_diff:
        safe_counter += 1

print(safe_counter)
