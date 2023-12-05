with open(r"2023/day-04/input.txt") as f:
    data = f.readlines()

card_lst = []

for card in data:
    card = card.rstrip('\n')
    ci = card.index(':')
    cd = card.index('|')
    card_num = card[ci - 3: ci].strip()
    # print(card[ci + 1: cd].strip().split(' '))
    win_nums = [int(n) for n in card[ci + 1: cd].strip().split(' ') if n != '']
    my_nums = [int(n) for n in card[cd + 1:].strip().split(' ') if n != '']
    card_lst.append({card_num: {'win_nums': win_nums, 'my_nums': my_nums}})
# {'20': {'win_nums': [34, 88, 44, 16, 90, 6, 58, 94, 64, 73], 'my_nums': [5, 70, 76, 53, 15, 68, 28, 4, 32, 65, 92, 91, 24, 86, 85, 31, 36, 67, 83, 18, 95, 45, 8, 51, 74]}}
# print(card_lst)

# p1


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


result = 0
for card in card_lst:
    cardl = list(card.values())[0]['win_nums']
    # print(cardl)
    mylst = list(card.values())[0]['my_nums']
    # print(mylst)
    result_lst = get_right_nums(cardl, mylst)
    # print(result_lst)
    scores = check_score(len(result_lst))
    # print(scores)
    result += scores
print(result)
