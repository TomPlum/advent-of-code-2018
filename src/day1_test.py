from day1 import part1, part2, solution_part_1, solution_part_2


def part1_example1():
    assert part1([1, -2, 3, 1]) == 3


def part1_example2():
    assert part1([1, 1, 1]) == 3


def part1_example3():
    assert part1([1, 1, -2]) == 0


def part1_example4():
    assert part1([-1, -2, -3]) == -6


def solution1():
    assert solution_part_1() == 525


def part2_example1():
    assert part2([1, -2, 3, 1]) == 2


def part2_example2():
    assert part2([1, -1]) == 0


def part2_example3():
    assert part2([3, 3, 4, -2, -4]) == 10


def part2_example4():
    assert part2([-6, 3, 8, 5, -6]) == 5


def part2_example5():
    assert part2([7, 7, -2, -7, -4]) == 14


def solution2():
    assert solution_part_2() == 75749
