source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.readlines()

# Part 1
#for each line, explore the solution space until a match is found or all
# possibilities are exhausted
nums_lines = []
for line in all_lines:
    total, nums = line.split(": ")
    nums = nums.strip()
    nums_lines.append([int(total), [int(num) for num in nums.split(" ")]])


def verify_operation(total, operation, nums, cur_total):
    if not nums:
        return total == cur_total

    cur_total = cur_total + nums[0] if operation == '+' else cur_total * nums[0]
    nums = nums[1:]
    
    return (verify_operation(total, '+', nums, cur_total) or verify_operation(total, '*', nums, cur_total))


res = 0
for total, nums  in nums_lines:
    if verify_operation(total, '+', nums, 0) or verify_operation(total, '*', nums, 1):
        res += total

print(res) 
