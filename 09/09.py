source = "input.txt"

line = ""
with open(source, "r") as file:
    line = file.read().strip()

is_file = True
file_id = 0
start = 0
files = []
spaces = []

for num in line:
    end = start + int(num)
    interval = [start, end]
    if is_file:
        files.append([file_id, interval])
        file_id += 1
        is_file = False
    else:
        spaces.append(interval)
        is_file = True

    start = end

# Part 1
# stop when processing something and the first free is ahead of us
# iterate from the file at the end of the disk and match against free spaces

free_space_index = 0
compacted_files = []
free_spaces = [space for space in spaces]
for i in range(len(files) - 1, -1, -1):
    file_id, (file_start, file_end) = files[i]

    space_start, space_end = free_spaces[free_space_index]

    # if the leftmost free space is after us, then all compaction has finished
    if file_start < space_start:
        compacted_files += files[0 : i + 1]
        break

    spaces_to_fill = file_end - file_start
    while spaces_to_fill > 0:
        space_start, space_end = free_spaces[free_space_index]
        spaces_available = space_end - space_start

        if spaces_to_fill >= spaces_available:
            free_space_index += 1
            spaces_to_fill -= spaces_available
            compacted_files.append([file_id, [space_start, space_end]])
        else:
            # shorten the interval
            free_spaces[free_space_index] = [space_start + spaces_to_fill, space_end]
            compacted_files.append(
                [file_id, [space_start, space_start + spaces_to_fill]]
            )
            spaces_to_fill = 0


res = 0
for num, (int_start, int_end) in compacted_files:
    for i in range(int_start, int_end):
        res += num * i


# 6370402949053
print(res)


# Part 2
# Same logic but only allow full blocks instead of fragmenting
# For each file, scan all free spaces
#   - stop once there's a free space where it fits (reallocate)
#   - or stop once we're at a space whose location is already ahead of the
#     file current location (don't reallocate)

free_spaces = [space for space in spaces]
compacted_files = []

for i in range(len(files) - 1, -1, -1):
    file_id, (file_start, file_end) = files[i]

    spaces_to_fill = file_end - file_start
    for free_space_index in range(len(free_spaces)):
        space_start, space_end = free_spaces[free_space_index]

        # We're trying to reallocate ahead of us, time to stop
        if space_start > file_start:
            compacted_files.append(files[i])
            break

        spaces_available = space_end - space_start
        # Skip if this free block cannot allocate the file
        if spaces_to_fill > spaces_available:
            continue

        # Here we know we'll reallocate
        if spaces_to_fill == spaces_available:
            # We no longer consider the space
            free_spaces.pop(free_space_index)
        else:
            # We must shrink the free space
            free_spaces[free_space_index] = [space_start + spaces_to_fill, space_end]

        compacted_files.append([file_id, [space_start, space_start + spaces_to_fill]])
        break

res = 0
for file_id, (file_start, file_end) in compacted_files:
    for i in range(file_start, file_end):
        res += file_id * i

# 6398096697992
print(res)
