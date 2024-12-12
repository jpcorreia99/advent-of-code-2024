source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.readlines()

for i in range(len(all_lines)):
    all_lines[i] = list(all_lines[i])


grid =  [[all_lines[i][j] for j in range(len(all_lines[0]))] for i in range(len(all_lines))]


right_curve = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0) 
}

direction = (-1, 0)
n_rows, n_cols = len(grid), len(grid[0])

def find_start(grid, n_rows, n_cols):
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == '^':
                return i,j
i,j = find_start(grid, n_rows, n_cols)

def is_in_bounds(i, j, n_rows, n_cols):
    return 0 <= i < n_rows and 0 <= j < n_cols

grid[i][j] = 'X'
res = 1
while True:
    if grid[i][j] == '.':
        res += 1
        grid[i][j] = 'X'
    
    new_i, new_j = i + direction[0], j + direction[1]
    if not is_in_bounds(new_i,new_j, n_rows, n_cols):
        break
    elif grid[new_i][new_j] == '#':
        direction = right_curve[direction]
    else:
        i = new_i
        j = new_j

print(res) # 5101 


# Part 2
# For each travelled position, attempt obstacles in all 4 directions and detect if we could travel a loop from there

def has_loop(i, j, obs_i, obs_j, grid_to_copy, initial_direction):
    grid = [[grid_to_copy[i][j] for j in range(len(grid_to_copy[0]))] for i in range(len(grid_to_copy))]
    grid[obs_i][obs_j] = '#'
    direction = initial_direction
    grid[i][j] = '.'


    while True:
        if grid[i][j] == 'X' and direction == initial_direction:
            return True

        if grid[i][j] == '.':
            grid[i][j] = 'X'
        
        new_i, new_j = i + direction[0], j + direction[1]
        if not is_in_bounds(new_i,new_j, n_rows, n_cols):
            return False
        elif grid[new_i][new_j] == '#':
            direction = right_curve[direction]
        else:
            i = new_i
            j = new_j
    
    print(".")
    return False


grid =  [[all_lines[i][j] for j in range(len(all_lines[0]))] for i in range(len(all_lines))]
direction = (-1, 0)
i,j = find_start(grid, n_rows, n_cols)
res = 0


while True:
    new_i, new_j = i + direction[0], j + direction[1]
    if not is_in_bounds(new_i,new_j, n_rows, n_cols):
        break

    if grid[new_i][new_j] == '#':
        direction = right_curve[direction]
    else:
        print("Testin has loop for", i, j, new_i, new_j, direction)
        if has_loop(i, j, new_i, new_j, grid, direction):
            res += 1

        i = new_i
        j = new_j

#1951
print(res)
