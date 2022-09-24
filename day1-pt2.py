from more_itertools import windowed
from typing import Dict, List, Tuple


file = open('day1-input.txt', 'r')
depthsStrs = file.readlines()
depths = [int(depthStr) for depthStr in depthsStrs]

def window_depth_sums(depths: List[int]):
    windows = windowed(depths, n=3)
    return [sum(window) for window in windows]

windowDepths = window_depth_sums(depths)

result = 0
prev = None
for depth in windowDepths:
    if prev is not None and depth > prev:
        result += 1
    prev = depth

print(result)
print("should be 1571")