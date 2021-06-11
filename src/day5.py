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

    # print(f"{data} -> {polymer}")
    return len(polymer)


def part2(data: str) -> int:
    unique = set(map(lambda c: c.lower(), data))

    results = []
    for unit in unique:
        units_removed = data.replace(unit, "").replace(unit.capitalize(), "")
        results.append(part1(units_removed))

    return min(results)


def solution_part_1():
    return part1(read(5).toString()[0])


def solution_part_2():
    return part2(read(5).toString()[0])
