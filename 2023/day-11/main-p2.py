grid = open(r'2023/day-11/input.txt').read().strip().splitlines()
# print grid


n = 1000000  # 1030


def transfer(grid):
    grid_t = []
    for i in range(len(grid[0])):
        temp = []
        for row in grid:
            temp.append(row[i])
        grid_t.append(temp)
    return grid_t


def get_empty_row_idx(grid):
    eri = []
    for i, row in enumerate(grid):
        if row.count('#') == 0:
            eri.append(i)
    return eri


empty_row = get_empty_row_idx(grid)
grid = transfer(grid)
empty_col = get_empty_row_idx(grid)
grid = transfer(grid)


# for x in grid:
#     print(x, end='')
#     print()
print(empty_row)
print(empty_col)


def get_empty(pos1, pos2):
    # return how many empty row between positions
    def helper(idx, lst):
        mi, ma = (pos1[idx], pos2[idx]) if pos1[idx] < pos2[idx] else (
            pos2[idx], pos1[idx])
        e = 0
        for i in lst:
            if mi < i < ma:
                e += 1
        return e

    return helper(0, empty_row), helper(1, empty_col)


# caculate the distance
distance = 0
postions = []
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '#':
            if postions:
                for p in postions:
                    # print((r, c), p)
                    er, ec = get_empty((r, c), (p[0], p[1]))
                    # print(er, ec)
                    h = abs(r - p[0]) - er + n * er
                    v = abs(c - p[1]) - ec + n * ec

                    distance += (h + v)
            postions.append((r, c))  # position should be tuple
print(distance)

# 2 times 4 - r + n*r
#         3 - c + n*c
