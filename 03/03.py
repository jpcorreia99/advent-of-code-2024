import re

source = "input.txt"
content  = ""

with open(source, "r") as file:
    content = file.read()


MUL_MATCHER = r"mul\((\d+),(\d+)\)"

res = 0
for match in re.finditer(MUL_MATCHER, content):
    num1 = int(match.group(1))
    num2 = int(match.group(2))

    res += num1 * num2

print(res)



# Part 2
# approach 1: get ranges for enablement and binary search if match is in enablement
# sol: 127092535

ENABLEMENT_MATCHER = r"do\(\)|don\'t\(\)"

enablement_ranges = []
is_enabled = True
start = 0

for match in re.finditer(ENABLEMENT_MATCHER, content):
    control_word = match.group(0)
    if control_word == 'do()':
        if not is_enabled:
            is_enabled = True
            start = match.start()
    else: #don't()
        if is_enabled:
            is_enabled = False
            enablement_ranges.append([start, match.start()])

if is_enabled:
    enablement_ranges.append([start, len(content)-1])

def match_is_enabled(match_index, enablement_range):
    left = 0
    right = len(enablement_range) - 1

    while left <= right:
        mid = (left + right) // 2
        start, end = enablement_range[mid]
        if start <= match_index <= end:
            return True 
        elif start > match_index:
            right = mid - 1
        elif end < match_index:
            left = mid + 1
    
    return False


res = 0
for match in re.finditer(MUL_MATCHER, content):
    start = match.start()
    if match_is_enabled(start, enablement_ranges):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        res += num1 * num2

print(res)

# part 2 sol 2: regex matches everything and we switch on and off as we match

ENABLEMENT_AND_MUL_MATCHER = r"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)"
is_enabled = True

res = 0
for match in re.finditer(ENABLEMENT_AND_MUL_MATCHER, content):
    if match.group(0) == "do()":
        is_enabled = True
    elif match.group(0) == "don't()":
        is_enabled = False
    elif is_enabled:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        res += num1 * num2

print(res)
