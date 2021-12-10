from statistics import median


def parse_input(num_list_str):
    num_str_list = num_list_str.split(",")
    return list(map(int, num_str_list))


file = open('day7-input.txt', 'r')
lines = file.read().splitlines()
positions = parse_input(lines[0])
# positions = parse_input("16,1,2,0,4,2,7,1,2,14")

# The median minimizes the sum of absolute deviations
# https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
med = median(positions)
abs_diff = 0
for p in positions:
    abs_diff += abs(p - med)

print(abs_diff)