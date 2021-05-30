from functools import reduce
from utility.reader import read


def part1(frequencies: [int]) -> int:
    return reduce((lambda a, b: a + b), frequencies)


def solution_part_1():
    return part1(read(1).toInteger())
