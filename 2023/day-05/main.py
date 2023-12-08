with open(r'2023/day-05/input.txt', 'r') as file:
    file_content = file.read()

sections = file_content.split('\n\n')

seeds = sections[0].split(': ')[1].split(' ')
seeds = [int(x) for x in seeds]
print(seeds)

maps = []
for _map in sections[1:]:
    map_list = _map.split(':\n')[1].strip('\n').split('\n')

    rules = []
    for strings in map_list:
        rule = strings.split(' ')
        cha = int(rule[0]) - int(rule[1])
        start = int(rule[1])
        end = int(rule[1]) + int(rule[2])
        rules.append([start, end, cha])

    sortrule = sorted(rules, key=lambda x: x[0])
    maps.append(sortrule)


def process_num(num, maplst):
    for lst in maplst:
        if num >= lst[0] and num < lst[1]:
            return int(num + lst[2])
    return num


res_lst = []
for seed in seeds:
    for maplst in maps:
        seed = process_num(seed, maplst)
    res_lst.append(seed)

print(min(res_lst))

# part 2
seeds = [(seeds[i], seeds[i] + seeds[i + 1])
         for i in range(len(seeds)) if i % 2 == 0]
print(seeds)


def process_num_range(seed_range, maplst):
    # maplst: start end cha
    #         b     b+c a-b
    seeds_to_extand = []
    res_to_extand = []
    seed_start = seed_range[0]
    seed_end = seed_range[1]
    for start, end, cha in maplst:
        # 取得横跨的区间
        over_start = max(seed_start, start)
        over_end = min(seed_end, end)
        if over_start < over_end:
            res_to_extand.append((over_start + cha, over_end + cha))
            if over_start > seed_start:
                seeds_to_extand.append((seed_start, over_start))
            if seed_end > over_end:
                seeds_to_extand.append((over_end, seed_end))
            break
    else:
        res_to_extand.append((seed_start, seed_end))
    return seeds_to_extand, res_to_extand


for maplst in maps:
    res = []
    while len(seeds) > 0:
        seed_range = seeds.pop()
        seeds_to_extand, res_to_extand = process_num_range(seed_range, maplst)
        seeds.extend(seeds_to_extand)
        res.extend(res_to_extand)
    seeds = res

print(min(seeds)[0])
