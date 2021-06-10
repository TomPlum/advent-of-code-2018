import re

from reader import read


def part1(data: str) -> int:
    polymer = data
    reactions_remaining = True
    while reactions_remaining:
        index = 0
        for i, c in enumerate(polymer):
            index = i
            if i == 0:
                continue

            last = polymer[i - 1]
            equal = c.lower() == last.lower()
            different_case = c != last
            if equal and different_case:
                polymer = re.sub(last + c, "", polymer)
                break

        if index == len(polymer) - 1:
            reactions_remaining = False

    return len(polymer)


def solution_part_1():
    return part1(read(5).toString()[0])
