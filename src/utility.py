from __future__ import annotations

from dataclasses import dataclass


def flatten(arr):
    return [item for sublist in arr for item in sublist]


@dataclass(eq=True, frozen=True)
class Point2D:
    x: int
    y: int

    def manhattan_distance(self, other: 'Point2D'):
        return abs(int(self.x) - int(other.x)) + abs(int(self.y) - int(other.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"
