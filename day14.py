from collections import Counter

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

def run_step(template, rules):
    new_template = ""
    for i in range(len(template) - 1):
        first = template[i]
        second = template[i+1]
        new_template += first
        pair = first + second
        if pair in rules.keys():
            new_template += rules[pair]
    new_template += template[-1]
    return new_template



file = open('day14-input.txt', 'r')
lines = file.read().splitlines()
template, rules = parse_input(lines)
# template, rules = parse_input(test_data.split("\n"))
num_steps = 10

new_template = template
for n in range(num_steps):
    new_template = run_step(new_template, rules)
print(new_template)

counter = dict(Counter(new_template))
print(counter)

most = 0
least = list(counter.values())[0]
for x in counter.values():
    if x > most:
        most = x
    if x < least:
        least = x

print(most - least)


