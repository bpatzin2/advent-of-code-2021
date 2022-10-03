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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def score(segment):
    score = 0
    for c in segment:
        score *= 5
        score += scoring[c]
    return score


file = open('day10-input.txt', 'r')
lines = file.read().splitlines()
# lines = test_data.split("\n")
# print(len(lines))

incomplete_stacks = []
for line in lines:
    stack: LifoQueue = LifoQueue()
    corrupt = False
    for c in line:
        if c in pairs.keys():
            stack.put(c)
        else:
            open_c = stack.get()
            if pairs[open_c] != c:
                corrupt = True
                break
    if not stack.empty() and not corrupt:
        incomplete_stacks.append(stack)


completion_segments = []
for stack in incomplete_stacks:
    completion_segment = ""
    while stack.qsize() > 0:
        c = stack.get()
        completion_segment += pairs[c]
    completion_segments.append(completion_segment)

scores = list(map(score, completion_segments))
scores.sort()
score_i = int(len(scores) / 2)
print(scores[score_i])
