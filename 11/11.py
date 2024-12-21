from functools import cache

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

    return int(left_stone), int(right_stone)


@cache
def blink(stone, level, limit):
    if level >= limit:
        return 1

    if stone == 0:
        return blink(1, level + 1, limit)

    if is_even_digits(stone):
        stone1, stone2 = split_stones(stone)
        return blink(stone1, level + 1, limit) + blink(stone2, level + 1, limit)

    stone *= 2024
    return blink(stone, level + 1, limit)


# Part 1
# 187738
print(sum([blink(stone, 0, 25) for stone in stones]))

# Part 2
print(sum([blink(stone, 0, 75) for stone in stones]))
