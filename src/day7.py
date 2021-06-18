import re

from reader import read
from utility import flatten


def part1(data: [str]) -> str:
    directions = parse_directions(data)
    start = find_start(directions)
    end = find_end(directions)

    print(f"Start: {start}")
    print(f"End: {end}")
    #n = [start]
    order = []

    print(directions)

    seen = []

    def traverse(step: str):
        children = directions.get(step, [])
        found = []
        print(f"Step is {step} - Depends On {children}")
        for child in children:
            found = found + traverse(child)

        if step != end:
            found.append(step)

        return found

    response = traverse(start)
    print(f"Response: {''.join(response)}")

    # while len(n) > 0:
    #     step = n.pop()
    #     print(f"Step is {step}")
    #     dependent = directions.get(step, [])
    #
    #     if step != end and step not in order:
    #         order.append(step)
    #         print(f"Adding {step}")
    #
    #     print(f"Found {step} - Depends On {dependent}")
    #     if len(dependent) > 1:
    #         dependent.sort(reverse=True)
    #         # order.append(dependent[len(dependent) - 1])
    #         # print(f"Adding {dependent[len(dependent) - 1]}")
    #         n = n + dependent
    #     elif len(dependent) == 1:
    #         n.append(dependent[0])
    #         # order.append(dependent[0])
    #         # print(f"Adding {dependent[0]}")
    #     print(f"The stack looks like: {n}")
    #     print("\n")

    #return ''.join(order)[::-1] + end


def parse_directions(data: [str]):
    directions = {}

    for line in data:
        match = re.search('Step (?P<first>\\w) must be finished before step (?P<second>\\w) can begin.', line)
        first = match.group('first')
        second = match.group('second')
        directions[first] = directions.get(first, []) + [second]

    return directions


def find_start(directions):
    steps = list(directions.keys())
    print(f"Keys: {steps}")
    start = ""

    for step in steps:
        all_dependees = flatten(directions.values())
        if step not in all_dependees:
            start = step
            break
    return start


def find_end(directions):
    end = ""
    all_dependees = set(flatten(directions.values()))

    for dep in all_dependees:
        if dep not in directions:
            end = dep
            break

    return end


order = []



def solution_part_1():
    return part1(read(7).toString())  # Not GHAIJKLOTYZQUEDSRWNBPX

    # GNPFHCAMVEBWRDSQIUZYJTKOL
