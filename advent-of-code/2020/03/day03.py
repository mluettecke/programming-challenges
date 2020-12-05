""" Advent of Code {{year}}
    Day {{ day }}:
    https://adventofcode.com/{{year}}/day/{{day}}
"""
import os


def part_one(input_data):
    """
    """
    trees = 0
    x = 0
    y = 0
    while y < len(input_data):
        if input_data[y][x % len(input_data[y])] == "#":
            trees = trees + 1
        x = x + 3
        y = y + 1
    return trees


def part_two(input_data):
    """
    """
    slopes = [
        [1, 1, 0],
        [3, 1, 0],
        [5, 1, 0],
        [7, 1, 0],
        [1, 2, 0]
    ]
    result = 1
    for slope in slopes:
        x = 0
        y = 0
        while y < len(input_data):
            if input_data[y][x % len(input_data[y])] == "#":
                slope[2] = slope[2] + 1
            x = x + slope[0]
            y = y + slope[1]
    for slope in slopes:
        result = result * slope[2]
    return result


def read_input():
    input_data = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        for line in f.read().splitlines():
            input_data.append([char for char in line])
    return input_data


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
