with open(r'2023/day-08/input.txt') as f:
    steps, space, *lst = f.read().splitlines()

network = {}
for maps in lst:
    position, targets = maps.split(' = ')
    network[position] = targets[1: -1].split(', ')

count = 0
current = 'AAA'

while current != 'ZZZ':
    count += 1
    if steps[0] == 'L':
        current = network[current][0]
    else:
        current = network[current][1]
    steps = steps[1:] + steps[0]

print(count)
