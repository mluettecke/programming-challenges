""" Advent of Code {{year}}
    Day {{ day }}:
    https://adventofcode.com/{{year}}/day/{{day}}
"""
import os


def part_one(instructions):
    """
    """
    i = 0
    accumulator = 0
    run_instructions = set()
    while i < len(instructions) and i not in run_instructions:
        operation, argument = instructions[i].split(" ")
        argument = int(argument)
        run_instructions.add(i)
        if operation == "acc":
            accumulator += argument
            i += 1
        elif operation == "jmp":
            i += argument
        elif operation == "nop":
            i += 1
    return accumulator


def part_two(input_data):
    """
    """
    pass


def read_input():
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        return [line for line in f.read().splitlines()]


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
