# Part 1
def get_min_value(sequence):
    low = sequence[0]
    for i in sequence:
        if i < low:
            low = i
    return low

input_left = []
input_right = []
distance = 0

with open('aoc01_input1', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        input_left.append(x)
        input_right.append(y)

while len(input_left) > 0:
    min_left = get_min_value(input_left)
    min_right = get_min_value(input_right)
    distance += abs(min_left - min_right)
    input_left.remove(min_left)
    input_right.remove(min_right)

print(f"total distance: {distance}")

# Part 2
similarity = 0

with open('aoc01_input2', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        input_left.append(x)
        input_right.append(y)

while len(input_left) > 0:
    counter = 0
    item = input_left[0]
    for j in input_right:
        if item == j:
            counter += 1

    similarity += counter * item
    input_left.remove(item)

print(f"similarity: {similarity}")
