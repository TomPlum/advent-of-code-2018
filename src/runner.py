import time

from day1 import solution_part_1 as d1p1, solution_part_2 as d1p2
from day2 import solution_part_1 as d2p1, solution_part_2 as d2p2
from day3 import solution_part_1 as d3p1, solution_part_2 as d3p2
from day4 import solution_part_1 as d4p1, solution_part_2 as d4p2
from day5 import solution_part_1 as d5p1, solution_part_2 as d5p2
from day7 import solution_part_1 as d7p1


def execute():
    run(1, d1p1, d1p2)
    run(2, d2p1, d2p2)
    run(3, d3p1, d3p2)
    run(4, d4p1, d4p2)
    run(5, d5p1, d5p2)
    run(7, d7p1, not_implemented)


def run(day: int, part1, part2):
    print(f"[Day {day}]")

    p1_result = measure(part1)
    print(f"Part 1: {p1_result[0]}")
    print(f"Execution Time: {p1_result[1]}\n")

    p2_result = measure(part2)
    print(f"Part 2: {p2_result[0]}")
    print(f"Execution Time: {p2_result[1]}\n")

    return p1_result[1], p2_result[1]


def measure(func):
    start = time.time_ns()
    answer = func()
    return answer, format_nanos(time.time_ns() - start)


def format_nanos(nanos: int):
    s = round(nanos / 1_000_000_000)
    ms = nanos / 1_000_000
    remaining_nanos = nanos % 1_000_000_000
    remaining_millis = remaining_nanos / 1_000_000
    micro = round(nanos / 1000)

    if abs(s) > 0:
        return f"{s}s {round(remaining_millis)}ms"
    elif abs(ms) >= 1:
        return f"{round(ms)}ms"
    else:
        return f"{micro}μs"

def not_implemented():
    return "Not Implemented"

if __name__ == '__main__':
    execute()
