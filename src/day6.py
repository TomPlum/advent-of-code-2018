from utility import Point2D


def part1(data: [str]) -> int:
    coords = map(lambda s: Point2D(s.split(",")[0].strip(), s.split(",")[1].strip()), data)
    for pos in coords:
        print(pos)
    return 0