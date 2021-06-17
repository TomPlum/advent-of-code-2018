import re

from utility import flatten


def part1(data: [str]) -> str:
    directions = {}

    for line in data:
        match = re.search('Step (?P<first>\\w) must be finished before step (?P<second>\\w) can begin.', line)
        first = match.group('first')
        second = match.group('second')
        directions[first] = directions.get(first, []) + [second]

    order = []
    steps = list(directions.keys())
    start = ""
    for step in steps:
        all_dependees = flatten(directions.values())
        if step not in all_dependees:
            start = step
            break

    n = [start]

    while len(n) > 0:
        step = n.pop()
        dependent = directions.get(step, [])
        if len(dependent) == 0 and len(n) > 0:
            continue
        print(f"Found {step} - Depends On {dependent}")
        order.append(step)
        if len(dependent) > 1:
            dependent.sort(reverse=True)
            n = n + dependent
        elif len(dependent) == 1:
            n.append(dependent[0])

    return ''.join(order)
