from day3 import part1, part2, solution_part_1, solution_part_2


def part1_example():
    claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    assert part1(claims) == 4


def part2_example():
    claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    assert part2(claims) == 3


def part1_solution():
    assert solution_part_1() == 112418


def part2_solution():
    assert solution_part_2() == 560
