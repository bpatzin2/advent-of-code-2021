from functools import reduce

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


def remove_all(input, to_remove):
    return list(set(input).difference(set(to_remove)))


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
            if x_dir != 0 and y_dir != 0:
                continue
            if (0 <= adj_coord[0] < len(grid[0])) and (0 <= adj_coord[1] < len(grid)):
                result.append(adj_coord)
    return result


def get_basin(basin_seed, basin_points, grid):
    to_visit = []
    visited = []
    to_visit.append(basin_seed)
    visited.append(basin_seed)

    while to_visit:
        coord = to_visit.pop(0)
        for neighbour in get_adj_coords(coord, grid):
            if neighbour in visited:
                continue
            if neighbour not in basin_points:
                continue
            visited.append(neighbour)
            to_visit.append(neighbour)
    return visited


def get_basin_points(grid):
    basin_points = []
    row_len = len(grid[0])
    col_len = len(grid)
    for x in range(0, row_len):
        for y in range(0, col_len):
            if get_height((x, y), grid) < 9:
                basin_points.append((x, y))
    return basin_points


def get_basins(grid):
    basin_points = get_basin_points(grid)
    basins = []
    while len(basin_points) > 0:
        basin_seed = basin_points[0]
        basin = get_basin(basin_seed, basin_points, grid)
        basins.append(basin)
        basin_points = remove_all(basin_points, basin)
    return basins


file = open("day9-input.txt", "r")
lines = file.read().splitlines()
grid = parse_input(lines)
# grid = parse_input(test_data.split("\n"))

basins = get_basins(grid)

basins.sort(reverse=True, key=len)
top3 = basins[0:3]
sizes = list(map(len, top3))
print(reduce(lambda x, y: x * y, sizes))
