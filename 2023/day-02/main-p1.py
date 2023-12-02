from pprint import pprint

# games = {
#     '1': [{'blue': 3, 'red': 4},
#           {'red': 1, 'green': 2, 'blue': 3},
#           {'green': 2}],
# }
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


def check(color, num):
    # red = 12
    # green = 13
    # blue = 14
    if color == 'red':
        if int(num) <= 12:
            return True
        else:
            return False
    elif color == 'green':
        if int(num) <= 13:
            return True
        else:
            return False
    elif color == 'blue':
        if int(num) <= 14:
            return True
        else:
            return False
    else:
        return False


result = []

for game_num, game_lst in games.items():
    flag = True
    for game in game_lst:
        for k, v in game.items():
            if not check(k, v):
                flag = False
                break
        if not flag:
            break
    if flag:
        result.append(int(game_num))


print(sum(result))
