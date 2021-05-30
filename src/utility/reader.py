import numpy

from input import Input


def read(day: int) -> [str]:
    with open(f"src/input/{day}.txt", "r") as f:
        return Input(numpy.array(f.read().splitlines()))
