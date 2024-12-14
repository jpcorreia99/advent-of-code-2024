from collections import defaultdict

source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.read().splitlines()

n_rows, n_cols = len(all_lines), len(all_lines[0])

# Part 1
# Collect all locations for each antenna
# for each pair, compute the distance vector and apply it to one of the elements

antenna_locations = defaultdict(list)

for i in range(n_rows):
    for j in range(n_cols):
        char = all_lines[i][j]
        if char != ".":
            antenna_locations[char].append([i, j])

solutions = set()
for _, locations in antenna_locations.items():
    for antenna in locations:
        for other_antenna in locations:
            if antenna == other_antenna:
                continue

            vector_i, vector_j = (
                antenna[0] - other_antenna[0],
                antenna[1] - other_antenna[1],
            )
            antinode_i, antinode_j = antenna[0] + vector_i, antenna[1] + vector_j

            if 0 <= antinode_i < n_rows and 0 <= antinode_j < n_cols:
                solutions.add((antinode_i, antinode_j))

# 291
print(len(solutions))

# Part 2
# continuously apply the vector until out of bounds

solutions = set()
for _, locations in antenna_locations.items():
    for antenna in locations:
        for other_antenna in locations:
            if antenna == other_antenna:
                continue

            # Antennas now also count because they're within a line
            solutions.add((antenna[0], antenna[1]))

            vector_i, vector_j = (
                antenna[0] - other_antenna[0],
                antenna[1] - other_antenna[1],
            )

            antinode_i, antinode_j = antenna[0] + vector_i, antenna[1] + vector_j

            while 0 <= antinode_i < n_rows and 0 <= antinode_j < n_cols:
                solutions.add((antinode_i, antinode_j))
                antinode_i, antinode_j = antinode_i + vector_i, antinode_j + vector_j

print(len(solutions))
