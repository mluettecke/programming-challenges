""" Advent of Code 2020
    Day 02:
    https://adventofcode.com/2020/day/02
"""
import os


def part_one(input_data):
    """
    """
    valid_passwords = 0
    for min, max, letter, password in input_data:
        if min <= password.count(letter) <= max:
            valid_passwords = valid_passwords + 1
    return valid_passwords


def part_two(input_data):
    """
    """
    valid_passwords = 0
    for pos_one, pos_two, letter, password in input_data:
        if password[pos_one - 1] == letter or password[pos_two - 1] == letter:
            if not (password[pos_one - 1] == letter and password[pos_two - 1] == letter):
                valid_passwords = valid_passwords + 1
    return valid_passwords


def read_input():
    input_data = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        for line in f.read().splitlines():
            password_policy, password = line.split(":")
            range, letter = password_policy.split(" ")
            min, max = range.split("-")
            input_data.append([int(min), int(max), letter, password.lstrip()])
    return input_data


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
