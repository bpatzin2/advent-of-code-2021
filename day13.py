simple_data = """
0,0
2,0
0,2
2,0

fold along x=1""".strip()

test_data = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".strip()


def parse_input(lines):
    points = []
    i = 0
    line = lines[i]
    while line != "":
        nums = line.split(",")
        points.append((int(nums[0]), int(nums[1])))
        i += 1
        line = lines[i]

    i += 1
    instructions = []
    while i in range(len(lines)):
        line = lines[i]
        instruction_parts = line.split("=")
        axis = instruction_parts[0][-1]
        num = int(instruction_parts[1])
        instructions.append((axis, num))
        i += 1

    return (points, instructions)


def fold_up(points, x_axis):
    new_points = set()
    for point in points:
        x, y = point
        if y < x_axis:
            new_points.add(point)
        elif y == x_axis:
            continue
        else:
            dist = y - x_axis
            new_y = x_axis - dist
            new_points.add((x, new_y))
    return new_points


def fold_left(points, y_axis):
    new_points = set()
    for point in points:
        x, y = point
        if x < y_axis:
            new_points.add(point)
        elif x == y_axis:
            continue
        else:
            dist = x - y_axis
            new_x = y_axis - dist
            new_points.add((new_x, y))
    return new_points


def dems(points):
    max_x = 0
    max_y = 0
    for x, y in points:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return max_x, max_y


def print_paper(points):
    result = []
    max_x, max_y = dems(points)
    for y in range(0, max_y + 1):
        row = []
        for x in range(0, max_x + 1):
            row.append("#" if (x, y) in points else ".")
        result.append(row)

    for row in result:
        print(row)
    return

file = open('day13-input.txt', 'r')
lines = file.read().splitlines()
points, instructions = parse_input(lines)
# points, instructions = parse_input(test_data.split("\n"))
# points, instructions = parse_input(simple_data.split("\n"))

max_x, max_y = dems(points)
print(max_x)
print(max_y)

print_paper(points)

print(points)
print(instructions)

new_points = fold_left(points, 655)
print_paper(new_points)
print(len(new_points))

# new_points = fold_up(points, 7, max_y)
# print_paper(new_points)
# print(len(new_points))

# new_points = fold_left(new_points, 5, 10)
# print_paper(new_points)
# print(len(new_points))
#
# new_points = fold_left(new_points, 3, 4)
# print_paper(new_points)
# print(len(new_points))

