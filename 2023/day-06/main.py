with open(r'2023/day-06/input.txt', 'r') as file:
    file_content = file.readlines()

times_str = file_content[0].rstrip('\n').split(':')[1].strip().split(' ')
times = [int(x) for x in times_str if x != '']
distances_str = file_content[1].rstrip('\n').split(':')[1].strip().split(' ')
distances = [int(x) for x in distances_str if x != '']
recoder = {times[i]: distances[i] for i in range(0, len(times))}
print(recoder)

ways = 1
for t, d in recoder.items():
    way = 0
    for pushtime in range(t + 1):
        distance = pushtime * (t - pushtime)
        if distance > d:
            way += 1
    ways *= way
print(ways)


# pushtime speed=pushtime time=Time-pushtime Distance=speed*time
# t:0-7    t              T-t                t*(T-t)
# condition:distance > Distance

# part 2
time = int(''.join(times_str))
distance = int(''.join(distances_str))
way = 0
for pushtime in range(time):
    if pushtime * (time - pushtime) > distance:
        way += 1
print(way)
