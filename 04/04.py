source = "input.txt"
all_lines = []

with open(source, "r") as file:
    all_lines = file.readlines()


directions = [[1,0], [-1,0], [0, -1], [0, 1], [1,1], [-1,-1], [1, -1], [-1, 1]]

n_rows, n_cols = len(all_lines), len(all_lines[0])

next_char = {
    'X': 'M',
    'M': 'A',
    'A': 'S',
    'S': True
}

def contains_xmas(all_lines, i, j, direction, expected_char):
    n_rows, n_cols = len(all_lines), len(all_lines[0])

    if expected_char == True:
        return True

    if i < 0 or i >= n_rows or j < 0 or j >= n_cols:
        return False

    if all_lines[i][j] == expected_char:
        i_dev, j_dev = direction
        new_i = i + i_dev
        new_j = j + j_dev
        return contains_xmas(all_lines, new_i, new_j, direction, next_char[expected_char])

    return False     

res = 0

for i in range(n_rows):
    for j in range(n_cols):
        char = all_lines[i][j]
        if char == 'X':
            for direction in directions:
                if contains_xmas(all_lines, i, j, direction, 'X'):
                    res += 1 
print(res)
                


# Part 2

def matches_pattern(all_lines, i, j):
    is_valid = 1 <= i < len(all_lines) - 1 and 1 <= j < len(all_lines[0]) - 1
    if not is_valid:
        return False  

    diagonals = [
        [
            (-1,-1),
             (1,1)
        ],
        [
            (-1,1),
            (1, -1)
        ]
    ]

    for diagonal_directions in diagonals:
        s_count = m_count = 0

        for i_dev, j_dev in diagonal_directions:
            new_i = i + i_dev
            new_j = j + j_dev
            char = all_lines[new_i][new_j]
            if char == 'S':
                s_count += 1
            elif char == 'M':
                m_count += 1
            else:
                return False
        if not (s_count == 1 and m_count == 1):
            return False
    
    return True


res = 0
for i in range(n_rows):
    for j in range(n_cols):
        if all_lines[i][j] == 'A':
          if matches_pattern(all_lines, i, j):
            res += 1


print(res)

    
