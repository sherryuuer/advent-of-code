grid = open(r'2023/day-11/input.txt').read().strip().splitlines()
# print grid


# expand the universe
def transfer(grid):
    grid_t = []
    for i in range(len(grid[0])):
        temp = []
        for row in grid:
            temp.append(row[i])
        grid_t.append(temp)
    return grid_t


def expand(grid):
    grid_x = []
    for row in grid:
        grid_x.append(row)
        if row.count('#') == 0:
            grid_x.append(row)
    return grid_x


grid = expand(grid)
grid = transfer(grid)
grid = expand(grid)
grid = transfer(grid)


for x in grid:
    print(x, end='')
    print()

# caculate the distance
distance = 0
postions = []
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '#':
            if postions:
                for p in postions:
                    distance += (abs(r - p[0]) + abs(c - p[1]))
            postions.append((r, c))  # position should be tuple
print(distance)
