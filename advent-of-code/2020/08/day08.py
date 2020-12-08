""" Advent of Code {{year}}
    Day {{ day }}:
    https://adventofcode.com/{{year}}/day/{{day}}
"""
import os


def run_instructions(instructions):
    i = 0
    accumulator = 0
    run_instructions = set()
    while i < len(instructions) and i not in run_instructions:
        operation, argument = instructions[i]
        argument = int(argument)
        run_instructions.add(i)
        if operation == "acc":
            accumulator += argument
            i += 1
        elif operation == "jmp":
            i += argument
        elif operation == "nop":
            i += 1
    finished = i == len(instructions)
    return [finished, accumulator]


def part_one(instructions):
    """
    """
    return run_instructions(instructions)


def part_two(instructions):
    """
    """
    for i in range(len(instructions)):
        operation, argument = instructions[i]
        # switch instructions around til it fits
        if operation == "jmp":
            instructions[i][0] = "nop"
            finished, accumulator = run_instructions(instructions)
            instructions[i][0] = "jmp"
        elif operation == "nop":
            instructions[i][0] = "jmp"
            finished, accumulator = run_instructions(instructions)
            instructions[i][0] = "nop"

        if finished:
            return accumulator


def read_input():
    instructions = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        for line in f.read().splitlines():
            operation, argument = line.split(" ")
            instructions.append([operation, int(argument)])
    return instructions


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
