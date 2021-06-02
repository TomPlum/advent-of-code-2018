from typing import Any


def part1(data: [str]) -> int:
    claims = map(lambda d: Claim(d), data)
    fabric = Grid()
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                pos = Point2D(x, y)
                ids = fabric.get(pos) or []
                ids.extend(claim.id)
                fabric.add(pos, ids)
    print(fabric)
    return 0


# Example: "#2 @ 3,1: 4x4"
class Claim:
    def __init__(self, value: str):
        data = value.split(" @ ")
        info = data[1].split(": ")
        sides = info[0].split(",")
        dim = info[1].split("x")

        self.id = data[0][1]
        self.left = int(sides[0])
        self.top = int(sides[1])
        self.width = int(dim[0])
        self.height = int(dim[1])

    def __str__(self):
        return f"#{self.id} @ {self.left}, {self.top}: {self.width}x{self.height}"

    def __repr__(self):
        return f"#{self.id} @ {self.left}, {self.top}: {self.width}x{self.height}"


class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash(self.x) + hash(self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Grid:
    def __init__(self):
        self.values = {}

    def add(self, pos: Point2D, value: Any) -> None:
        self.values[pos] = value

    def get(self, pos: Point2D) -> Any:
        return self.values.get(pos, None)

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
