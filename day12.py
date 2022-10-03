from collections import defaultdict

test_data = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end""".strip()


def parse_line(line):
    parts = line.split("-")
    return parts[0], parts[1]


def parse_input(lines):
    return list(map(parse_line, lines))


def to_graph(connections):
    c_map = defaultdict(list)
    for connection in connections:
        print(connection)
        c_map[connection[0]].append(connection[1])
        c_map[connection[1]].append(connection[0])
    return c_map


def dfs(graph, node, path=[]):
    if node.islower() and node in path:
        return []
    new_path = path.copy()
    new_path.append(node)
    if node == "end":
        return [new_path]
    results = []
    for neighbour in graph[node]:
        tmp_results = dfs(graph, neighbour, new_path)
        results.extend(tmp_results)
    return results


file = open("day12-input.txt", "r")
lines = file.read().splitlines()
connections = parse_input(lines)
# connections = parse_input(test_data.split("\n"))


graph = to_graph(connections)
print(graph)
paths = dfs(graph, "start")
print(paths)

print(len(paths))
