import math

from utility import Point2D


def part1(data: [str]) -> int:
    coords = list(map(lambda s: Point2D(s.split(",")[0].strip(), s.split(",")[1].strip()), data))
    x_max = int(max(pos.x for pos in coords))
    y_max = int(max(pos.y for pos in coords))

    distances = {}

    for y in range(0, y_max):
        for x in range(0, x_max):
            shortest_distance = math.inf
            chosen_point = None
            pos = Point2D(x, y)
            for coord in coords:
                distance = abs(coord.manhattan_distance(pos))
                if distance < shortest_distance:
                    shortest_distance = distance
                    chosen_point = coord

            distances[chosen_point] = distances.get(chosen_point, []) + [pos]

    for k, v in distances.items():
        print(f"{k} -> {v}")

    return 0