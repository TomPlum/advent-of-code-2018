from typing import Any

from reader import read
from utility import Point2D


def part1(data: [str]) -> int:
    """Calculates the total square inches of fabric that overlaps with two or more claims."""
    claims = map(lambda d: Claim(d), data)
    fabric = create_fabric(claims)
    return len(list(filter(lambda k: len(fabric.get(k)) >= 2, fabric.values)))


def part2(data: [str]) -> int:
    """Finds the ID of the claim that does not overlap with any other."""
    claims = {}
    for d in data:
        claim = Claim(d)
        claims[claim.id] = claim

    fabric = create_fabric(claims.values())
    single_claims = list(filter(lambda it: len(it) == 1, fabric.values.values()))

    non_overlapping = {}
    for i in single_claims:
        claim_id = i[0]
        existing = non_overlapping.get(claim_id, 0)
        non_overlapping[claim_id] = existing + 1

    for k, v in non_overlapping.items():
        claim = claims[k]
        if claim.width * claim.height == v:
            return claim.id

    return 0


def create_fabric(claims):
    fabric = Grid()
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                pos = Point2D(x, y)
                ids = fabric.get(pos)
                ids.append(claim.id)
                fabric.add(pos, ids)
    return fabric


def solution_part_1() -> int:
    return part1(read(3).toString())


def solution_part_2() -> int:
    return part2(read(3).toString())


class Claim:
    """A claim made by an Elf about an area of fabric in the format #2 @ 3,1: 4x4"""

    def __init__(self, value: str):
        data = value.split(" @ ")
        info = data[1].split(": ")
        sides = info[0].split(",")
        dim = info[1].split("x")

        self.id = int(data[0][1:])
        self.left = int(sides[0])
        self.top = int(sides[1])
        self.width = int(dim[0])
        self.height = int(dim[1])

    def __repr__(self):
        return f"#{self.id} @ {self.left}, {self.top}: {self.width}x{self.height}"


class Grid:
    def __init__(self):
        self.values = {}

    def add(self, pos: Point2D, value: Any) -> None:
        self.values[pos] = value

    def get(self, pos: Point2D) -> Any:
        return self.values.get(pos, [])

    def values(self):
        return self.values

    def __repr__(self):
        s = ""
        keys = self.values.keys()
        x = list(map(lambda pos: pos.x, keys))
        y = list(map(lambda pos: pos.y, keys))
        y_min = min(y, default=0)
        y_max = max(y, default=0)
        x_min = min(x, default=0)
        x_max = max(x, default=0)
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                if Point2D(x, y) in keys:
                    ids = self.values[Point2D(x, y)]
                    if len(ids) > 1:
                        s += "X "
                    else:
                        s += ids[0] + " "
                else:
                    s += ". "
            s += "\n"
        return s
