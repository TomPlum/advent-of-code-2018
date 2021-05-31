from day1 import solution_part_1, solution_part_2


def execute():
    run(1, 1, solution_part_1)
    run(1, 2, solution_part_2)


def run(day: int, part: int, func):
    print(f"Day {day} [P{part}]: {func()}")


if __name__ == '__main__':
    execute()
