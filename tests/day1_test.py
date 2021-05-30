from src.day1 import part1, solution_part_1


def example1():
    assert part1([1, -2, 3, 1]) == 3


def example2():
    assert part1([1, 1, 1]) == 3


def example3():
    assert part1([1, 1, -2]) == 0


def example4():
    assert part1([-1, -2, -3]) == -6


def solution1():
    assert solution_part_1() == 525
