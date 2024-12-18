source = "input.txt"

line = ""
with open(source, "r") as file:
    line = file.read().strip()

stones = [int(stone) for stone in line.split(" ")]


def is_even_digits(stone):
    return len(str(stone)) % 2 == 0


def split_stones(stone):
    str_stone = str(stone)
    half_stone_len = len(str_stone) // 2

    left_stone, right_stone = str_stone[:half_stone_len], str_stone[half_stone_len:]

    return [int(left_stone), int(right_stone)]


for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif is_even_digits(stone):
            new_stones += split_stones(stone)
        else:
            new_stones.append(stone * 2024)

    stones = new_stones

# 187738
print(len(stones))
