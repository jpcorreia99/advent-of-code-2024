from collections import defaultdict

source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.read().splitlines()

# Count of how many trails go over a specific place

trails_at_position = defaultdict(int)
n_rows, n_cols = len(all_lines), len(all_lines[0])


grid = [[int(num) for num in line] for line in all_lines]


def count_trails(grid, i, j, visited=None):
    if not visited:
        visited = set()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if (i, j) in visited:
        return 0

    visited.add((i, j))

    if grid[i][j] == 9:
        return 1

    trail_count = 0
    for i_dev, j_dev in directions:
        new_i, new_j = i + i_dev, j + j_dev
        if not (0 <= new_i < n_rows and 0 <= new_j < n_cols):
            continue

        if grid[new_i][new_j] == grid[i][j] + 1:
            trail_count += count_trails(grid, new_i, new_j, visited)

    return trail_count


res = 0
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] == 0:
            res += count_trails(grid, i, j)

# 638
print(res)

# Part 2
# Same thing but we can revisit locations


def count_rating(grid, i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if grid[i][j] == 9:
        return 1

    trail_count = 0
    for i_dev, j_dev in directions:
        new_i, new_j = i + i_dev, j + j_dev
        if not (0 <= new_i < n_rows and 0 <= new_j < n_cols):
            continue

        if grid[new_i][new_j] == grid[i][j] + 1:
            trail_count += count_rating(grid, new_i, new_j)

    return trail_count


res = 0
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] == 0:
            res += count_rating(grid, i, j)

# 1289
print(res)
