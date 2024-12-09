source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.readlines()

for i in range(len(all_lines)):
    all_lines[i] = list(all_lines[i])

right_curve = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0) 
}

direction = (-1, 0)
n_rows, n_cols = len(all_lines), len(all_lines[0])

def find_start(all_lines, n_rows, n_cols):
    for i in range(n_rows):
        for j in range(n_cols):
            if all_lines[i][j] == '^':
                return i,j
i,j = find_start(all_lines, n_rows, n_cols)

def is_in_bounds(i, j, n_rows, n_cols):
    return 0 <= i < n_rows and 0 <= j < n_cols

all_lines[i][j] = 'X'
res = 1
while True:
    if all_lines[i][j] == '.':
        res += 1
        all_lines[i][j] = 'X'
    
    new_i, new_j = i + direction[0], j + direction[1]
    if not is_in_bounds(new_i,new_j, n_rows, n_cols):
        break
    elif all_lines[new_i][new_j] == '#':
        direction = right_curve[direction]
    else:
        i = new_i
        j = new_j
print(res)


