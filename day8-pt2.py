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
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}

uniq_lens = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

all_potential_mapppings = {
    'a': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'b': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'c': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'd': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'e': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'f': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'g': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
}


def parse_line(line):
    signal, output = line.split(" | ")
    return signal.split(), output.split()


def parse_input(lines):
    return list(map(parse_line, lines))


def keep(input, to_keep):
    return set(input).intersection(set(to_keep))


def remove_all(input, to_remove):
    return list(set(input).difference(set(to_remove)))


def apply_uniq_num_segment_rules(potential_mappings, scrambled_displays):
    updated_mappings = potential_mappings.copy()
    for display in scrambled_displays:
        if len(display) in uniq_lens.keys():
            for c in display:
                potentials = display_config[uniq_lens[len(display)]]
                updated_mappings[c] = keep(updated_mappings[c], potentials)
    return updated_mappings


def apply_generic_deduction(potential_mappings):
    updated_mappings = potential_mappings.copy()
    n = 1

    while n < 10:
        reset = False
        mappings_with_n_potentials = dict(filter(lambda kv: len(kv[1]) == n, updated_mappings.items()))
        if len(mappings_with_n_potentials) >= n:
            new_mappings = updated_mappings.copy()
            vals_to_remove = list(itertools.chain(*mappings_with_n_potentials.values()))
            for k, v in updated_mappings.items():
                if k not in mappings_with_n_potentials.keys():
                    new_potentials = remove_all(v, vals_to_remove)
                    if len(new_potentials) < len(v):
                        new_mappings[k] = new_potentials
                        reset = True
            updated_mappings = new_mappings
        if reset:
            n = 1
        else:
            n += 1
    return updated_mappings


def determine_potential_wire_mappings(scrambled_displays):
    potential_mappings = all_potential_mapppings.copy()
    potential_mappings = apply_uniq_num_segment_rules(potential_mappings, scrambled_displays)
    potential_mappings = apply_generic_deduction(potential_mappings)
    return potential_mappings


def decypher(signal, wire_mapping):
    potential_wires = distinct_combos(signal, wire_mapping)
    potential_wires = list(filter(lambda x: len(x) == len(signal), potential_wires))
    for digit, segments in display_config.items():
        for potential in potential_wires:
            if set(segments) == set(potential):
                return digit


def distinct_combos(iter, mapping):
    combos2d = list(map(lambda signal_char: mapping[signal_char], iter))
    combos = list(map(frozenset, list(itertools.product(*combos2d))))
    return list(set(combos))


def solve_line(signal, output):
    potential_mappings = determine_potential_wire_mappings(signal + output)
    ints = list(map(lambda output_signal: decypher(output_signal, potential_mappings), output))
    return int("".join(list(map(str, ints))))


file = open('day8-input.txt', 'r')
lines = file.read().splitlines()
pairs = parse_input(lines)
# pairs = parse_input(test_data.split("\n"))

actual_outputs = list(map(lambda pair: solve_line(pair[0], pair[1]), pairs))
print(sum(actual_outputs))
