from pprint import pprint

with open("2023\day-02\input.txt") as f:
    data = f.readlines()


# Turn the game list into a dict
games = {}
for game in data:
    key_part, value_part = game.rstrip("\n").split(':')
    key = key_part.split(' ')[1]
    value_list = value_part.split(';')
    value = []
    for v in value_list:
        v = v.split(',')
        v_dict = {}
        for ele in v:
            num, color = ele.split(' ')[1:]
            v_dict[color] = num
        value.append(v_dict)
    games[key] = value
pprint(games)

########### ↑from part 1↑#############################


def get_power(lst):
    # in order to do power init num as 1
    red = 1
    green = 1
    blue = 1
    for game in lst:
        for color, num in game.items():
            if color == "red":
                if int(num) >= red:
                    red = int(num)
            elif color == "green":
                if int(num) >= green:
                    green = int(num)
            else:
                if int(num) >= blue:
                    blue = int(num)
    return red*green*blue


result = 0
for game in games:
    result += get_power(games[game])

print(result)
