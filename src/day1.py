from functools import reduce
from itertools import accumulate, cycle

from reader import read


def part1(frequencies: [int]) -> int:
    return reduce((lambda a, b: a + b), frequencies)


def part2(frequencies: [int]) -> int:
    seen = {0}
    return next(f for f in accumulate(cycle(frequencies)) if f in seen or seen.add(f))


def solution_part_1():
    return part1(read(1).toInteger())


def solution_part_2():
    return part2(read(1).toInteger())
