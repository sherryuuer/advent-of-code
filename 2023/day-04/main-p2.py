with open(r"2023/day-04/input.txt") as f:
    data = f.readlines()

card_dict = {}


def check_score(nums):
    if nums == 0:
        return 0
    return 2 ** (nums - 1)


def get_right_nums(lst, mylst):
    result = []
    for n in lst:
        if n in mylst:
            result.append(n)
    return result


for card in data:
    card = card.rstrip('\n')
    ci = card.index(':')
    cd = card.index('|')
    card_num = card[ci - 3: ci].strip()
    # print(card[ci + 1: cd].strip().split(' '))
    win_nums = [int(n) for n in card[ci + 1: cd].strip().split(' ') if n != '']
    my_nums = [int(n) for n in card[cd + 1:].strip().split(' ') if n != '']
    result_lst = get_right_nums(win_nums, my_nums)
    keyname = card_num
    card_dict[int(keyname)] = len(result_lst)

print(card_dict)

result = {}

for k, v in card_dict.items():
    if k not in result:
        result[k] = 1

    for n in range(k + 1, k + v + 1):
        result[n] = result.get(n, 1) + result[k]


print(sum(result.values()))
