with open(r'2023/day-05/input.txt', 'r') as file:
    file_content = file.read()

sections = file_content.split('\n\n')
# print(sections)

seeds = sections[0].split(': ')[1].split(' ')
seeds = [int(x) for x in seeds]
# print(seeds)

maps = []
for _map in sections[1:]:
    # map_name = map.split(':\n')[0]
    map_list = _map.split(':\n')[1].strip('\n').split('\n')

    rules = []
    for strings in map_list:
        # print(strings)
        rule = strings.split(' ')
        cha = int(rule[0]) - int(rule[1])
        start = int(rule[1])
        end = int(rule[1]) + int(rule[2])
        rules.append([start, end, cha])

    sortrule = sorted(rules, key=lambda x: x[0])
    # if sortrule[0][0] != 0:
    #     sortrule.insert(0, [0, sortrule[0][0], 0])
    # sortrule.append([sortrule[-1][1], float('inf'), 0])
    maps.append(sortrule)
# print(maps)


def process_num(num, maplst):
    for lst in maplst:
        if num >= lst[0] and num < lst[1]:
            return int(num + lst[2])
    return num


res_lst = []
for seed in seeds:
    # print(seed)
    for maplst in maps:
        # print(map)
        seed = process_num(seed, maplst)
    res_lst.append(seed)

print(min(res_lst))

# part 2
seeds = [[seeds[i], seeds[i + 1]] for i in range(len(seeds)) if i % 2 == 0]
print(seeds)
