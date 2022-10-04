from typing import List


def run() -> int:
    depths = depths_from_file()
    return num_increases(depths)


def num_increases(depths):
    result = 0
    prev = None
    for depth in depths:
        if prev is not None and depth > prev:
            result += 1
        prev = depth
    return result


def depths_from_file() -> List[int]:
    file = open("day1-input.txt", "r")
    depthStrs = file.readlines()
    return [int(depthStr) for depthStr in depthStrs]


if __name__ == "__main__":
    print(run())
