""" Advent of Code {{year}}
    Day {{ day }}:
    https://adventofcode.com/{{year}}/day/{{day}}
"""
import os


def part_one(input_data):
    """
    """
    pass


def part_two(input_data):
    """
    """
    pass


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
