from typing import List


def run():
    result = 0
    prev = None
    depths = depths_from_file()
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
