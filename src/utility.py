from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Point2D:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}, {self.y})"
