import functools

source = "input.txt"
left = []
right = []

all_lines = []
with open(source, "r") as file:
    all_lines = file.readlines()

for line in all_lines:
    left_val, right_val = line.split("   ")
    left.append(int(left_val))
    right.append(int(right_val))

# or 
# left, right = map(list,zip(*[map(int, line.split("   ")) for line in all_lines]))

left.sort()
right.sort()


print(functools.reduce(lambda cum_sum, pair: cum_sum + abs(pair[0] - pair[1]), zip(left, right), 0))
# or sum(abs(left_val - right_val) for left_val, right_val in zip(left, right))


# Part 2 - similarity score
from collections import Counter
right_counter = Counter(right)
left_set = set(left)

print(sum(right_counter[num] * num for num in left_set))
