source = "input.txt"

line = ""
with open(source, "r") as file:
    line = file.read().strip()

# stop when processing something and the first free is ahead of us
# iterate from the file at the end of the disk and match against free spaces

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


free_space_index = 0
compacted_files = []
for i in range(len(files) - 1, -1, -1):
    file_id, (file_start, file_end) = files[i]

    space_start, space_end = spaces[free_space_index]
    
    # if the leftmost free space is after us, then all compaction has finished
    if file_start < space_start:
        compacted_files += files[0 : i + 1]
        break

    spaces_to_fill = file_end - file_start
    while spaces_to_fill > 0:
        space_start, space_end = spaces[free_space_index]
        spaces_available = space_end - space_start

        if spaces_to_fill >= spaces_available:
            free_space_index += 1
            spaces_to_fill -= spaces_available
            compacted_files.append([file_id, [space_start, space_end]])
        else:
            # shorten the interval
            spaces[free_space_index] = [space_start + spaces_to_fill, space_end]
            compacted_files.append(
                [file_id, [space_start, space_start + spaces_to_fill]]
            )
            spaces_to_fill = 0


res = 0
for num, (int_start, int_end) in compacted_files:
    for i in range(int_start, int_end):
        res += num * i


print(res)

# taken = [0, [0, 5]], [1, [7, 9]], [2, [12, 16]]
# free = [6, 6], [10, 11]
