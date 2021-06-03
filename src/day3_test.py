from day3 import part1, solution_part_1


def part1_example():
    claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    assert part1(claims) == 4


def part1_solution():
    assert solution_part_1() == 112418
