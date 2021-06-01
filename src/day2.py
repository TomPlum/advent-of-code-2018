import difflib

from reader import read


def part1(ids: [str]) -> int:
    twice = list(map((lambda box: occurrences(box, 2)), ids)).count(True)
    thrice = list(map((lambda box: occurrences(box, 3)), ids)).count(True)
    return twice * thrice


def part2(ids: [str]) -> str:
    for a in ids:
        for b in ids:
            diff = list(difflib.ndiff(a, b))
            remaining = list(filter(lambda it: it[0] == ' ', diff))
            deltas = list(map(lambda it: it[0], diff))
            if deltas.count('+') == 1 and deltas.count('-') == 1:
                return ''.join(list(map(lambda it: it.strip(), remaining)))


def occurrences(string: str, goal: int) -> bool:
    for c in set(string):
        if string.count(c) == goal:
            return True
    return False


def solution_part_1() -> int:
    return part1(read(2).toString())


def solution_part_2() -> str:
    return part2(read(2).toString())
