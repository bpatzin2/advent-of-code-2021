test_data = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".strip()


def parse_line(line):
    return list(map(int, line))


def parse_input(lines):
    return list(map(parse_line, lines))


def val(coord, grid):
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


def simulate_day(grid):
    row_len = len(grid[0])
    col_len = len(grid)
    for x in range(0, row_len):
        for y in range(0, col_len):
            grid[y][x] += 1

    flashed = []
    any_flashed = True
    while any_flashed:
        any_flashed = False
        for x in range(0, row_len):
            for y in range(0, col_len):
                coord = (x, y)
                energy = val(coord, grid)
                if energy > 9:
                    any_flashed = True
                    flashed.append(coord)
                    grid[y][x] = 0
                    adjs = get_adj_coords(coord, grid)
                    for adj in adjs:
                        if adj not in flashed:
                            x, y = adj
                            grid[y][x] += 1
    return flashed



file = open('day11-input.txt', 'r')
lines = file.read().splitlines()
grid = parse_input(lines)
# grid = parse_input(test_data.split("\n"))

row_len = len(grid[0])
col_len = len(grid)

done = False
i = 0
while not done:
    i += 1
    flashed = simulate_day(grid)
    if len(flashed) == (row_len * col_len):
        done = True

print(i)


