from queue import LifoQueue

test_data = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".strip()

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

file = open('day10-input.txt', 'r')
lines = file.read().splitlines()
# lines = test_data.split("\n")

stack = LifoQueue()
corrupted = []

for line in lines:
    for c in line:
        if c in pairs.keys():
            stack.put(c)
        else:
            open_c = stack.get()
            if pairs[open_c] != c:
                corrupted.append((line, c))
print(corrupted)

score = sum(list(map(lambda x: scoring[x[1]], corrupted)))
print(score)