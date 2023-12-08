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
seeds = [[seeds[i], seeds[i] + seeds[i + 1]]
         for i in range(len(seeds)) if i % 2 == 0]
# print(seeds)

# maplsts = []
# for mapl in maps:
#     lst = []
#     for l in mapl:
#         lst.append([l[0], l[2]])
#     lst.append([mapl[-1][1], 0])
#     maplsts.append(lst)
# print(maplsts)


def process_num_range(seeds, maplst):
    # nlist = [[left, right],...]
    # maplst = [[breakpoint, xxx], [breakpoint, xxx], ....]
    res = []
    for nlist in seeds:
        left = nlist[0]
        right = nlist[1]
        currentl = 0
        currentr = -1
        if right < maplst[currentl][0] or left > maplst[currentr][0]:
            res.append([left, right])
            print("bp1")
            break

        if left < maplst[currentl][0] and maplst[currentl][0] < right < maplst[currentl + 1][0]:
            res.append([left, maplst[currentl][0]])
            res.append([(maplst[currentl][0] + maplst[currentl][1]),
                       (right + maplst[currentl][1])])
            print("bp2")
            break

        if maplst[currentr - 1][0] < left < maplst[currentr][0] and right > maplst[currentr][0]:
            res.append([(left + maplst[currentr - 1][1]),
                       (maplst[currentr - 1][0] + maplst[currentr - 1][1])])
            res.append([maplst[currentr][0],
                       right])
            print("bp3")
            break

        while left >= maplst[currentl][0]:
            currentl += 1
        while right < maplst[currentr][0]:
            currentr -= 1
        # left l r right
        # l是起点右边的break点，r是终点左边的break点
        # 如果l大于r里说明起始点在一个区间(currentr, currentl)内
        if maplst[currentl] > maplst[currentr]:
            res.append([(left + maplst[currentr][1]),
                        (right + maplst[currentr][1])])
        # 如果l等于r说明起始点被同一个点分开
        elif maplst[currentl] == maplst[currentr]:
            res.append([(left + maplst[currentl - 1][1]),
                        (maplst[currentl][0] + maplst[currentl][1])])
            res.append([(maplst[currentr][0] + maplst[currentr][1]),
                        (right + maplst[currentr][1])])
        # 如果l小于r说明中间有很多break点
        else:
            res.append([(left + maplst[currentl - 1][1]),
                        (maplst[currentl][0] + maplst[currentl][1])])
            res.append([(maplst[currentr][0] + maplst[currentr][1]),
                        (right + maplst[currentr][1])])
            for idx in range(currentl, currentr):
                res.append([maplst[idx][0], (maplst[idx][0] + maplst[idx][1])])
    return res


# while maplsts:
#     maplst = maplsts.pop(0)
#     seeds = process_num_range(seeds, maplst)

# print(seeds)

# part2 longtime
res_lst = []
for seedset in seeds:
    # print(seed)
    for seed in range(seedset[0], seedset[1]):
        for maplst in maps:
            # print(map)
            seed = process_num(seed, maplst)
        res_lst.append(seed)

print(min(res_lst))
