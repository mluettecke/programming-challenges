""" Advent of Code 2020
    Day 1: Report Repair
    https://adventofcode.com/2020/day/01
"""
import os


def part_one(input_data):
    """
    """
    for number in input_data:
        if(2020 - number) in input_data:
            return number * (2020 - number)


def part_two(input_data):
    """
    """
    for number_x in input_data:
        for number_y in input_data:
            if (2020 - number_x - number_y) in input_data:
                return (2020 - number_x - number_y) * number_x * number_y


def read_input():
    input_data = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        return [int(line) for line in f.readlines()]


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
