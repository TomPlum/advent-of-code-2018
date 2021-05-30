from day1 import solution_part_1


def execute():
    run(1, 1, solution_part_1)


def run(day: int, part: int, func):
    print(f"Day {day} [P{part}]: {func()}")


if __name__ == '__main__':
    execute()
