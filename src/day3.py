def part1(data: [str]) -> int:
    claims = map(lambda d: Claim(d), data)
    fabric = {}
    return 0


# Example: "#2 @ 3,1: 4x4"
class Claim:
    def __init__(self, value: str):
        data = value.split(" @ ")
        info = data[1].split(": ")
        sides = info[0].split(",")
        dim = info[1].split("x")

        self.id = data[0][1]
        self.left = sides[0]
        self.top = sides[1]
        self.width = dim[0]
        self.height = dim[1]


class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
