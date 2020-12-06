""" Advent of Code {{year}}
    Day {{ day }}:
    https://adventofcode.com/{{year}}/day/{{day}}
"""
import os


def get_row(value):
    upper = 127
    lower = 0
    for letter in value[:7]:
        diff = upper - lower
        if letter == "F":
            upper = int(upper - diff / 2)
        if letter == "B":
            lower = int(lower + diff / 2) + 1
    return lower


def get_column(value):
    upper = 7
    lower = 0
    for letter in value[7:]:
        diff = upper - lower
        if letter == "L":
            upper = int(upper - diff / 2)
        if letter == "R":
            lower = int(lower + diff / 2) + 1
    return lower


def part_one(input_data):
    """
    """
    max_id = 0
    for seat in input_data:
        row = get_row(seat)
        column = get_column(seat)
        seat_id = row * 8 + column
        if seat_id > max_id:
            max_id = seat_id
    return max_id


def part_two(input_data):
    """
    """
    max_id = 100
    min_id = 100
    ids = []
    for seat in input_data:
        row = get_row(seat)
        column = get_column(seat)
        seat_id = row * 8 + column
        if seat_id > max_id:
            max_id = seat_id
        if seat_id < min_id:
            min_id = seat_id
        ids.append(seat_id)
    ids.sort()
    last_id = ids[0] - 1
    for id in ids:
        if not id - 1 == last_id:
            return id - 1
        last_id = id


def read_input():
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
        return [line for line in f.read().splitlines()]


def main():
    input_data = read_input()
    print(f"Solution for part one: {part_one(input_data)}")
    print(f"Solution for part two: {part_two(input_data)}")


if __name__ == "__main__":
    main()
