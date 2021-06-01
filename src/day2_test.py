from day2 import part1, part2, solution_part_1, solution_part_2


def part1_example1():
    ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    assert part1(ids) == 12


def part2_example1():
    ids = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
    assert part2(ids) == "fgij"


def part1_solution():
    assert solution_part_1() == 6888


def part2_solution():
    assert solution_part_2() == "icxjvbrobtunlelzpdmfkahgs"
