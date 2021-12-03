def mode(values):
    zero_count = 0
    one_count = 0
    for value in values:
        if value == "0":
            zero_count += 1
        else:
            one_count += 1
    if zero_count > one_count:
        return "0"
    else:
        return "1"


def mode_at_index(index, collections):
    vals = map(lambda x: x[index], collections)
    return mode(vals)


def inverse(binary_str):
    result = ""
    for c in binary_str:
        if c == "0":
            result += "1"
        else:
            result += "0"
    return result


file = open('day3-input.txt', 'r')
binary_strs = file.readlines()
num_len = len(binary_strs[0])
gamma = ""
for i in range(0, num_len):
    gamma += mode_at_index(i, binary_strs)

epsilon = inverse(gamma)

print(gamma)
print(epsilon)

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print(gamma_int * epsilon_int)