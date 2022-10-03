def mode(values, preference):
    zero_count = 0
    one_count = 0
    for value in values:
        if value == "0":
            zero_count += 1
        else:
            one_count += 1
    if zero_count == one_count:
        return preference
    elif zero_count > one_count:
        return "0"
    else:
        return "1"


def mode_at_index(index, collections, preference):
    vals = map(lambda x: x[index], collections)
    return mode(vals, preference)


def inverse(binary_str):
    result = ""
    for c in binary_str:
        if c == "0":
            result += "1"
        else:
            result += "0"
    return result


def filter_char_at_pos(strs, char, pos):
    return list(filter(lambda str: str[pos] == char, strs))


file = open("day3-input.txt", "r")
binary_strs = file.read().splitlines()
num_len = len(binary_strs[0])

oxygen_rating_potentials = binary_strs.copy()
for i in range(0, num_len):
    modal_bit = mode_at_index(i, oxygen_rating_potentials, "1")
    oxygen_rating_potentials = filter_char_at_pos(
        oxygen_rating_potentials, modal_bit, i
    )
    if len(oxygen_rating_potentials) == 1:
        break
oxygen_rating_str = oxygen_rating_potentials[0]
oxygen_rating = int(oxygen_rating_str, 2)

co2_rating_potentials = binary_strs.copy()
for i in range(0, num_len):
    modal_bit = mode_at_index(i, co2_rating_potentials, "1")
    inverse_bit = "0" if modal_bit == "1" else "1"
    co2_rating_potentials = filter_char_at_pos(co2_rating_potentials, inverse_bit, i)
    if len(co2_rating_potentials) == 1:
        break
co2_rating_str = co2_rating_potentials[0]
co2_rating = int(co2_rating_str, 2)

print(oxygen_rating_str)
print(co2_rating_str)
print(co2_rating * oxygen_rating)
