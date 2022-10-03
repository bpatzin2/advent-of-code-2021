from more_itertools import windowed
from typing import Dict, List, Tuple


def window_depth_sums(depths: List[int]):
    windows = windowed(depths, n=3)
    return [sum(window) for window in windows]


def num_increases(ints: List[int]):
    result = 0
    prev = None
    for num in ints:
        if prev is not None and num > prev:
            result += 1
        prev = num
    return result


def depths_from_file():
    file = open("day1-input.txt", "r")
    depthStrs = file.readlines()
    return [int(depthStr) for depthStr in depthStrs]


def run():
    depths = depths_from_file()
    windowDepths = window_depth_sums(depths)
    return num_increases(windowDepths)


if __name__ == "__main__":
    print(run())
