# outside : cross pipe even times
# inside : cross pipe odd times

from collections import deque
grid = open(
    r'2023/day-10-graph-bfs-queue/input.txt').read().strip().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'S':
            sr = r
            sc = c
            break
    else:
        continue
    break

print(sr, sc)

seen = {(sr, sc)}
q = deque([(sr, sc)])


# give the Start 'S' a direction
maybe_s = {'|', '-', 'J', 'L', '7', 'F'}

while q:
    r, c = q.popleft()
    ch = grid[r][c]
    # |-LJ7F
    # if want to go up
    if r > 0 and ch in 'S|JL' and grid[r - 1][c] in '|7F' and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))
        if ch == 'S':
            maybe_s &= {'|', 'J', 'L'}
    # if want to go down
    if r < len(grid) - 1 and ch in 'S|7F' and grid[r + 1][c] in '|JL' and (r + 1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))
        if ch == 'S':
            maybe_s &= {'|', '7', 'F'}
    # if want to go left
    if c > 0 and ch in 'S-J7' and grid[r][c - 1] in '-LF' and (r, c - 1) not in seen:
        seen.add((r, c - 1))
        q.append((r, c - 1))
        if ch == 'S':
            maybe_s &= {'-', 'J', '7'}
    # if want to go right:
    if c < len(grid[r]) - 1 and ch in 'S-LF' and grid[r][c + 1] in '-J7' and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))
        if ch == 'S':
            maybe_s &= {'-', 'L', 'F'}

assert len(maybe_s) == 1
(S,) = maybe_s

grid = [row.replace('S', S) for row in grid]
# print(grid)

# turn the garbage pipe into '.'
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if (r, c) not in seen:
            ch = '.'


outside = set()  # get the outside world
for r, row in enumerate(grid):
    within = False
    # inside piece need to ride the wall (direct to different directions)
    up = None
    for c, ch in enumerate(row):
        if ch == '|':
            assert up is None
            within = not within
        elif ch == '-':
            assert up is not None
        elif ch in 'LF':
            assert up is None
            up = (ch == 'L')
        elif ch in '7J':
            assert up is not None
            if ch != ('J' if up else '7'):
                within = not within
            up = None
        elif ch == '.':
            pass
        else:
            raise RuntimeError(f'Unexpected charactor (horizontal) :{ch}.')

        if not within:
            outside.add((r, c))

print(outside)

# visualize the outside world
for r in range(len(grid)):
    for c in range(len(grid[r])):
        print('#' if (r, c) in outside else '.', end='')
    print()

res = len(grid) * len(grid[0]) - len(outside | seen)
# res = len(grid) * len(grid[0]) - len(outside) - len(seen)
print(res)
