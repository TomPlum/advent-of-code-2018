from reader import read


def part1(data: str) -> int:
    polymer = ['.']

    for unit in data:
        last = polymer[-1]
        if last != unit and last.lower() == unit.lower():
            polymer.pop()
        else:
            polymer.append(unit)

    return len(polymer) - 1


def part2(data: str) -> int:
    unique = set(map(lambda c: c.lower(), data))

    results = []
    for unit in unique:
        units_removed = data.replace(unit, "").replace(unit.capitalize(), "")
        results.append(part1(units_removed))

    return min(results)


def solution_part_1():
    return part1(read(5).toString()[0])


def solution_part_2():
    return part2(read(5).toString()[0])
