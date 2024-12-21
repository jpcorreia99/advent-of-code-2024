# Area -> count of elements
# Perimeter -> count of how many positions we don't have a neighbour of the same type

source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.read().splitlines()

n_rows, n_cols = len(all_lines), len(all_lines[0])
# Part 1
# Visit the whole graph, collecting into sets the groups


# returns area and perimeter of plot
def visit_plot(all_lines, i, j, visited, flower_type):
    if (i, j) in visited:
        return 0, 0

    visited.add((i, j))

    area = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    perimeter = 0

    for i_dev, j_dev in directions:
        new_i, new_j = i + i_dev, j + j_dev
        if not (0 <= new_i < n_rows and 0 <= new_j < n_cols):
            perimeter += 1
        elif all_lines[new_i][new_j] != flower_type:
            perimeter += 1
        elif (new_i, new_j) in visited:
            continue
        else:  # same flower type, unvisited
            sub_area, sub_perimeter = visit_plot(
                all_lines, new_i, new_j, visited, flower_type
            )

            area += sub_area
            perimeter += sub_perimeter
    return area, perimeter


visited = set()
res = 0
for i in range(n_rows):
    for j in range(n_cols):
        if (i, j) not in visited:
            flower_type = all_lines[i][j]
            area, perimeter = visit_plot(all_lines, i, j, visited, flower_type)
            res += area * perimeter

# 1522850
print(res)

# Part 2
