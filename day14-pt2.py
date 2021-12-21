from collections import Counter, defaultdict

test_data = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".strip()


def parse_input(lines):
    template = lines[0]

    rules = {}
    for i in range(2, len(lines)):
        line = lines[i]
        rule = line.split(" -> ")
        rules[rule[0]] = rule[1]

    return template, rules


def run_step(pair_counts, rules):
    new_pair_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in rules.keys():
            first_pair = pair[0] + rules[pair]
            new_pair_counts[first_pair] += count
            second_pair = rules[pair] + pair[1]
            new_pair_counts[second_pair] += count
        else:
            new_pair_counts[pair] += count
    return new_pair_counts


def count_pairs(template):
    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pair_counts[pair] += 1
    return pair_counts


file = open('day14-input.txt', 'r')
lines = file.read().splitlines()
template, rules = parse_input(lines)
# template, rules = parse_input(test_data.split("\n"))
num_steps = 40

pair_counts = count_pairs(template)
for n in range(num_steps):
    pair_counts = run_step(pair_counts, rules)

letter_counts = defaultdict(int)
for pair, count in pair_counts.items():
    letter = pair[0]
    letter_counts[letter] += count
# last letter is only one not at the start of a pair
letter_counts[template[-1]] += 1

most = 0
least = list(letter_counts.values())[0]
for x in letter_counts.values():
    if x > most:
        most = x
    if x < least:
        least = x
print(most - least)


