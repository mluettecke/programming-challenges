""" Advent of Code 2020
    Day 04:
    https://adventofcode.com/2020/day/04
"""
import os
import re


def part_one(input_data):
    """
    """
    sum_of_answers = 0
    for group in input_data:
        answers = set()
        for person in group:
            for answer in person:
                answers.add(answer)
        sum_of_answers = sum_of_answers + len(answers)
    return sum_of_answers


def part_two(input_data):
    """
    """
    sum_of_answers = 0
    for group in input_data:
        # ugly af
        intersection = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
        for person in group:
            answers = set()
            for answer in person:
                answers.add(answer)
            intersection = intersection.intersection(answers)
        sum_of_answers = sum_of_answers + len(intersection)
    return sum_of_answers


def read_input():
    groups = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        for group in f.read().split("\n\n"):
            answers = []
            for answer in group.splitlines():
                answers.append(answer)
            groups.append(answers)
    return groups


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
