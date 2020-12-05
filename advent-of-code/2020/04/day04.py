""" Advent of Code 2020
    Day 04:
    https://adventofcode.com/2020/day/04
"""
import os
import re


def validate_byr(value):
    return 1902 <= int(value) <= 2002


def validate_iyr(value):
    return 2010 <= int(value) <= 2020


def validate_eyr(value):
    return 2020 <= int(value) <= 2030


def validate_hgt(value):
    if value[-2:] == "cm":
        return 150 <= int(value[:-2]) <= 193
    if value[-2:] == "in":
        return 59 <= int(value[:-2]) <= 76
    return False


def validate_hcl(value):
    return bool(re.search("^#[a-fA-F0-9]{6}", value))


def validate_ecl(value):
    return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_pid(value):
    if not len(value) == 9:
        return False
    if not int(value):
        return False
    return True


required_fields = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
}


def validate_passport(passport, validate_values=False):
    for field in required_fields.keys():
        if not field in passport.keys():
            return False
        if validate_values:
            if not required_fields[field](passport[field]):
                print(f"field: {field} in {passport} invalid")
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
    valid_passports = 0
    for passport in input_data:
        if validate_passport(passport, True):
            valid_passports = valid_passports + 1
    return valid_passports


def read_input():
    passports = []
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        for values in f.read().split("\n\n"):
            values = values.replace("\n", " ")
            passport = {}
            for key_value in values.split(" "):
                key, value = key_value.split(":")
                passport[key] = value
            passports.append(passport)
    return passports


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
