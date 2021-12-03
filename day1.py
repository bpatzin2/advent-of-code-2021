file = open('day1-input.txt', 'r')
depthsStrs = file.readlines()
depths = map(int, depthsStrs)

result = 0
prev = None
for depth in depths:
    if prev is not None and depth > prev:
        result += 1
    prev = depth

print(result)
