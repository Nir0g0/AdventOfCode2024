import re

# Part 1

s = ""

with open('../Day03/aoc03_input1', 'r') as f:
    for line in f.readlines():
        s += line

'''
while True:
    try:
        start_idx = s.index("mul")
        end_idx = s.index(")", start_idx) + 1
        new_s = s[start_idx:]
        list_start_idx.append(s[start_idx:end_idx])
        s = s[:start_idx] + s[end_idx:]
    except Exception as e:
        break
'''
counter = 0

pattern = r'mul\(\d{1,3},\s*\d{1,3}\)'
matches = re.findall(pattern, s)
num_list = []

for str in matches:
    numbers = re.findall(r'\d+', str)
    numbers = [int(num) for num in numbers]
    num_list += numbers

for i in range(0, len(num_list), 2):
    counter += num_list[i] * num_list[i+1]

print(counter)


# Part 2

pattern_do = r"mul\(\d{1,3},\s*\d{1,3}\)|do\(\)|don\'t\(\)"
matches = re.findall(pattern_do, s)

allowed = True
counter = 0
num_list = []

for str in matches:
    if str == "do()": allowed = True
    elif str == "don't()": allowed = False
    else:
        if allowed:
            numbers = re.findall(r'\d+', str)
            numbers = [int(num) for num in numbers]
            num_list += numbers

for i in range(0, len(num_list), 2):
    counter += num_list[i] * num_list[i+1]


print(counter)