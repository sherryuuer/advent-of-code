with open(r'2023/day-09/input.txt') as f:
    lines = f.read().splitlines()

lines = [string.split(' ') for string in lines]
lines = [list(map(int, inner_list)) for inner_list in lines]
print(lines)

res = 0
for lst in lines:
    # init add num
    num = lst[-1]
    flag = True
    while flag:
        clst = []
        for i in range(1, len(lst)):
            clst.append(lst[i] - lst[i - 1])
        if all(n == 0 for n in clst):
            flag = False
        num += clst[-1]
        lst = clst[:]
    res += num
print(res)
