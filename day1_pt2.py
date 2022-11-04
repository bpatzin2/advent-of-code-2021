from more_itertools import windowed
from typing import Dict, Iterator, List, Tuple


def run() -> int:
    depths = depths_from_file()
    windowDepths = window_depth_sums(depths)
    return num_increases(windowDepths)


def window_depth_sums(depths: List[int]) -> List[int]:
    windows: Iterator = windowed(depths, n=3)
    return [sum([d for d in window if d is not None]) for window in windows]


def num_increases(ints: List[int]) -> int:
    result = 0
    prev = None
    for num in ints:
        if prev is not None and num > prev:
            result += 1
        prev = num
    return result


def depths_from_file() -> List[int]:
    file = open("day1-input.txt", "r")
    depthStrs = file.readlines()
    return [int(depthStr) for depthStr in depthStrs]


if __name__ == "__main__":
    print(run())
