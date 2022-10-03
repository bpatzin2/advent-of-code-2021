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


def grow_grid_5(grid):
    result = []
    for i in range(5):
        for row in grid:
            new_row = []
            for j in range(5):
                extension = list(map(lambda x: ((x + i + j - 1) % 9) + 1, row))
                new_row.extend(extension)
            result.append(new_row)
    return result


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


# https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
def dijsktra(grid, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    shortest_path_keys = {initial}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = get_adj_coords(current_node, grid)
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = val(next_node, grid) + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
                shortest_path_keys.add(next_node)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
                    shortest_path_keys.add(next_node)

        # next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        next_destinations = {}
        next_destination_keys = shortest_path_keys.difference(visited)
        for node in next_destination_keys:
            next_destinations[node] = shortest_paths[node]

        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    distance = 0
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        distance += val(current_node, grid)
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path, (distance - val(path[0], grid))


file = open("day15-input.txt", "r")
lines = file.read().splitlines()
grid = parse_input(lines)
# grid = parse_input(test_data.split("\n"))
big_grid = grow_grid_5(grid)
row_len = len(big_grid[0])
col_len = len(big_grid)
bottom_right_coord = (row_len - 1, col_len - 1)

path, distance = dijsktra(big_grid, (0, 0), bottom_right_coord)
print(path)
print(distance)
