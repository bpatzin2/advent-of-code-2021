from collections import defaultdict, Counter

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


def is_path_invalid(path):
    count_dict = dict(Counter(path))
    num2s = 0
    for node, c in count_dict.items():
        if node.isupper():
            continue
        if c > 2:
            return True
        if c > 1:
            num2s += 1
        if num2s > 1:
            return True
    return False


def dfs(graph, node, path=[]):
    # print(path)
    if node == "start" and node in path:
        return []

    new_path = path.copy()

    if node.islower() and is_path_invalid(new_path):
        return []

    new_path.append(node)
    if node == "end":
        return [new_path]
    results = []
    for neighbour in graph[node]:
        tmp_results = dfs(graph, neighbour, new_path)
        results.extend(tmp_results)
    return results


file = open('day12-input.txt', 'r')
lines = file.read().splitlines()
connections = parse_input(lines)
# connections = parse_input(test_data.split("\n"))

graph = to_graph(connections)
paths = dfs(graph, "start")
print(len(paths))



