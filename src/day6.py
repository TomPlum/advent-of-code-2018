from utility import Point2D


def part1(data: [str]) -> int:
    coords = map(lambda s: Point2D(s.split(",")[0].strip(), s.split(",")[1].strip()), data)
    x_max = max(pos.x for pos in coords)
    y_max = max(pos.y for pos in coords)

    all_coords = {}

    for y in range(0, y_max):
        for x in range(0, x_max):
            all_coords[Point2D(x, y)] = "."
    for pos in coords:
        print(pos)
    return 0