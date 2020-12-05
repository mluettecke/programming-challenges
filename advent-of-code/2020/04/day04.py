""" Advent of Code 2020
    Day 04:
    https://adventofcode.com/2020/day/04
"""
import os
import re

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

optional_fields = [
    "cid"
]


def validate_passport(passport):
    for field in required_fields:
        if not field in passport.keys():
            return False
    return True


def part_one(input_data):
    """
    """
    valid_passports = 0
    for passport in input_data:
        if validate_passport(passport):
            valid_passports = valid_passports + 1
    return valid_passports


def part_two(input_data):
    """
    """
    pass


def read_input():
    passports = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        for values in f.read().split("\n\n"):
            values = values.replace("\n", " ")
            passport = {}
            for key_value in values.split(" "):
                try:
                    key, value = key_value.split(":")
                    passport[key] = value
                except Exception as e:
                    print(key_value)
            passports.append(passport)
    return passports


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
