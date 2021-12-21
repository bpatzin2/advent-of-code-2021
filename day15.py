import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

test_data = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".strip()


def parse_input(lines):
    result = []
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        result.append(row)
    return result


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


def vert_num(coord, grid):
    row_len = len(grid[0])
    x, y = coord
    return x + (y * row_len)


def bottom_right_vert_num(grid):
    row_len = len(grid[0])
    col_len = len(grid)
    return vert_num((row_len - 1, col_len - 1), grid)


def to_matrix(grid):
    row_len = len(grid[0])
    col_len = len(grid)
    n = row_len * col_len
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html
    row = []
    col = []
    risk = []
    for y in range(col_len):
        for x in range(row_len):
            this_vert_num = vert_num((x, y), grid)
            adjs = get_adj_coords((x, y), grid)
            for a in adjs:
                a_num = vert_num(a, grid)
                row.append(a_num)
                col.append(this_vert_num)
                risk.append(grid[y][x])
    row_a = np.array(row)
    col_a = np.array(col)
    data_a = np.array(risk)
    return csr_matrix((data_a, (row_a, col_a)), shape=(n, n))



file = open('day15-input.txt', 'r')
lines = file.read().splitlines()
grid = parse_input(lines)
# grid = parse_input(test_data.split("\n"))

matrix = to_matrix(grid)
dist_matrix = shortest_path(csgraph=matrix, directed=True)
print(dist_matrix[0][bottom_right_vert_num(grid)])
