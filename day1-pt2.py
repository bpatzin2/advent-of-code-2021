from more_itertools import windowed
file = open('day1-input.txt', 'r')
depthsStrs = file.readlines()
depths = [int(x) for x in depthsStrs]

windows = list(windowed(depths, n=3))
windowDepths = map(sum, windows)

result = 0
prev = None
for depth in windowDepths:
    if prev is not None and depth > prev:
        result += 1
    prev = depth

print(result)
