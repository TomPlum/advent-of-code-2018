from reader import read


def part1(ids: [str]) -> int:
    twice = list(map((lambda box: occurrences(box, 2)), ids)).count(True)
    thrice = list(map((lambda box: occurrences(box, 3)), ids)).count(True)
    return twice * thrice


def occurrences(string: str, goal: int) -> bool:
    for c in set(string):
        if string.count(c) == goal:
            return True
    return False


def solution_part_1() -> int:
    return part1(read(2).toString())
