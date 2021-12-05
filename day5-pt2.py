import itertools
from collections import Counter


def parse_point(point_str):
    point_strs = point_str.split(",")
    return int(point_strs[0]), int(point_strs[1])


def parse_segment(segment_str):
    point_strs = segment_str.split(" -> ")
    return parse_point(point_strs[0]), parse_point(point_strs[1])


def enumerate(a, b):
    if a > b:
        return range(b, a+1)
    else:
        return range(a, b+1)


def expand_segment(segment):
    point1 = segment[0]
    point2 = segment[1]
    if point1[0] == point2[0]:
        result = []
        for y in enumerate(point1[1], point2[1]):
            result.append((point1[0], y))
        return result
    elif point1[1] == point2[1]:
        result = []
        for x in enumerate(point1[0], point2[0]):
            result.append((x, point1[1]))
        return result
    else:
        x_step = 1 if point1[0] < point2[0] else -1
        y_step = 1 if point1[1] < point2[1] else -1
        result = [point1]
        next_point = point1
        while next_point != point2:
            next_x = next_point[0] + x_step
            next_y = next_point[1] + y_step
            next_point = (next_x, next_y)
            result.append(next_point)
        return result


file = open('day5-input.txt', 'r')
lines = file.read().splitlines()
print(lines)
line_segments = list(map(parse_segment, lines))
expanded_segments = list(map(expand_segment, line_segments))
all_points = list(itertools.chain(*expanded_segments))
count_dict = dict(Counter(all_points))
keys = [key for key, value in count_dict.items() if value > 1]
print(len(keys))
