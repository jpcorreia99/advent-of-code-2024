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
# Quadratic :(
def is_valid(nums, lower_bound, higher_bound):
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    valid_diffs = list(filter(lambda diff: lower_bound <= diff <= higher_bound, diffs))
    return len(valid_diffs) == len(diffs) 


safe_count = 0
for line in all_lines:
    nums = [int(num) for num in line.split(" ")]
    permutations_without_element = [nums[:i] + nums[i+1:] for i in range(len(nums))]

    if (any([is_valid(arr, 1, 3) or is_valid(arr, -3, -1) for arr in permutations_without_element])):
        safe_count += 1
    
print(safe_count)

