import time

from day1 import solution_part_1 as d1p1, solution_part_2 as d1p2
from day2 import solution_part_1 as d2p1

def execute():
    run(1, d1p1, d1p2)
    run(2, d2p1, d2p1)


def run(day: int, part1, part2):
    print(f"[Day {day}]")
    p1_result = measure(part1)
    print(f"Part 1: {p1_result[0]}")
    print(f"Execution Time: {p1_result[1]}s\n")
    p2_result = measure(part2)
    print(f"Part 2: {p2_result[0]}")
    print(f"Execution Time: {p2_result[1]}s\n")
    return p1_result[1], p2_result[1]


def measure(func):
    start = time.time()
    answer = func()
    return answer, time.time() - start


if __name__ == '__main__':
    execute()
