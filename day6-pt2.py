from collections import Counter, defaultdict


def parse_input(num_list_str):
    num_str_list = num_list_str.split(",")
    return dict(Counter(map(int, num_str_list)))


def simulate_day(fish_day_counts):
    result = defaultdict(int)
    for day, count in fish_day_counts.items():
        if day > 0:
            result[day-1] += count
        else:
            result[8] += count
            result[6] += count
    return result


# fish_day_counts = parse_input("3,4,3,1,2")

file = open('day6-input.txt', 'r')
lines = file.read().splitlines()
fish_day_counts = parse_input(lines[0])

for i in range(256):
    fish_day_counts = simulate_day(fish_day_counts)

result = 0
for v in fish_day_counts.values():
    result += v

print(result)