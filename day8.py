import itertools


test_data = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".strip()

display_config = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

def parse_line(line):
    signal, output = line.split(" | ")
    return signal, output


def parse_input(lines):
    return list(map(parse_line, lines))

file = open('day8-input.txt', 'r')
lines = file.read().splitlines()
pairs = parse_input(lines)
# pairs = parse_input(test_data.split("\n"))
outputs = list(map(lambda x: x[1], pairs))
output_lists = list(map(lambda x: x.split(), outputs))
flat_list = list(itertools.chain(*output_lists))
selected_outputs = list(filter(lambda x: len(x) in display_config.values(), flat_list))
print(len(selected_outputs))