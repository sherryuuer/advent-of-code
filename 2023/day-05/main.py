# seeds = open(
#     r'2023/day-05/info.txt').read().splitlines()[0].split(': ')[1].split(' ')
# print(seeds)

input = 79
map = [50, 98, 2], [52, 50, 48]
for input in range(map[1], map[1] + map[2]):
    output = 50 + (map[0] - map[1])
