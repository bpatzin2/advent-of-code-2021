test_data = """
2199943210
3987894921
9856789892
8767896789
9899965678""".strip()


def parse_line(line):
    return list(map(int, line))


def parse_input(lines):
    return list(map(parse_line, lines))


def get_height(coord, grid):
    return grid[coord[1]][coord[0]]


def get_adj_coords(coord, grid):
    result = []
    dirs = [-1, 0, 1]
    for x_dir in dirs:
        for y_dir in dirs:
            adj_coord = (coord[0] + x_dir, coord[1] + y_dir)
            if adj_coord == coord:
                continue
            if (0 <= adj_coord[0] < len(grid[0])) and (0 <= adj_coord[1] < len(grid)):
                result.append(adj_coord)
    return result


def is_lowpoint(coord, grid):
    h = get_height(coord, grid)
    adj_coords = get_adj_coords(coord, grid)
    return all(get_height(adj_coord, grid) > h for adj_coord in adj_coords)


def risk_level(coord, grid):
    return 1 + get_height(coord, grid)


file = open('day9-input.txt', 'r')
lines = file.read().splitlines()
grid = parse_input(lines)
# grid = parse_input(test_data.split("\n"))
row_len = len(grid[0])
col_len = len(grid)

lowpoints = []

for x in range(0, row_len):
    for y in range(0, col_len):
        if is_lowpoint((x, y), grid):
            lowpoints.append((x, y))
print(lowpoints)

risk_levels = list(map(lambda x: risk_level(x, grid), lowpoints))
print(sum(risk_levels))