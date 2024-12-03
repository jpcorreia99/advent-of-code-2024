# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
#  How many reports are safe?

source = "input.txt"
all_lines  = []

with open(source, "r") as file:
    all_lines = file.readlines()

safe_count = 0

for line in all_lines:
    nums = [int(num) for num in line.split(" ")]
    if nums[0] == nums[1]:
        continue
    orientation = "increasing" if nums[1] > nums[0] else "decreasing"

    is_safe = 1
    for i in range(1, len(nums)):
        if orientation=="increasing":
            diff = nums[i] - nums[i-1]
            if not(diff >= 1 and diff <= 3):
                is_safe = 0
                break
        else:
            diff = nums[i-1] - nums[i]
            if not(diff >= 1 and diff <= 3):
                is_safe = 0
                break
    safe_count += is_safe
    
print(safe_count)



# Part 2

# calculate array of diffs
# count negative, neutral and positive diffs
# Compute absolute diff between positive and negative diffs and determine if we are more inclined to be increasing or decreasing
# check the absolute diff against the neutral count

def is_valid(diffs, lower_bound, higher_bound):
    valid_diffs = list(filter(lambda diff: lower_bound <= diff <= higher_bound, diffs))
    return len(valid_diffs) >= len(diffs) - 1



safe_count = 0
for line in all_lines:
    nums = [int(num) for num in line.split(" ")]

    diff_array = []
    for i in range(1, len(nums)):
        diff_array.append(nums[i] - nums[i-1])
    
    if (is_valid(diff_array, 1, 3) or is_valid(diff_array, -3, -1)):
        safe_count += 1
    
print(safe_count)

