def parse_input(num_list_str):
    num_str_list = num_list_str.split(",")
    return list(map(int, num_str_list))


def abs_diff_weighted(val, nums):
    result = 0
    for n in nums:
        abs_diff = abs(n - val)
        result += sum(range(abs_diff + 1))
    return result


file = open("day7-input.txt", "r")
lines = file.read().splitlines()
positions = parse_input(lines[0])
# positions = parse_input("16,1,2,0,4,2,7,1,2,14")

min_pos = min(positions)
max_pos = max(positions)
pos_range = list(range(min_pos, max_pos + 1))

result_position = min(pos_range, key=lambda p: abs_diff_weighted(p, positions))
result_abs_diff = abs_diff_weighted(result_position, positions)
print(result_abs_diff)
