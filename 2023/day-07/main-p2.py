with open(r'2023/day-07/input.txt') as f:
    hands = f.readlines()

hands = [[string[:5], int(string[6:])] for string in hands]
print(hands)


def char_to_num(char):
    if char == 'A':
        return 14
    if char == 'K':
        return 13
    if char == 'Q':
        return 12
    if char == 'J':  # J rule
        return 1
    if char == 'T':
        return 10


def comp_hand(hand1, hand2):
    # use when they are same type
    for i in range(len(hand1)):
        h1 = hand1[i]
        h2 = hand2[i]
        if h1 == h2:
            continue

        if not h1.isdigit():
            h1 = char_to_num(h1)
        if not h2.isdigit():
            h2 = char_to_num(h2)

        if int(h1) > int(h2):
            return True
        else:
            return False


def check_hand(hand):
    # hand likes "32T3K"
    # hands.keys()
    # return type, level
    charl = {}
    for c in hand:
        if c not in charl:
            charl[c] = 1
            continue
        charl[c] += 1
    if len(charl) > 1 and 'J' in charl:
        n = charl.pop('J')
        max_key = max(charl, key=charl.get)
        charl[max_key] += n
    # print(charl)
    if len(charl) == 1:
        return 6  # five
    elif len(charl) == 2:
        if min(list(charl.values())) == 1:
            return 5  # four
        else:
            return 4  # full house
    elif len(charl) == 3:
        if max(list(charl.values())) == 3:
            return 3  # three
        else:
            return 2  # two pair
    elif len(charl) == 4:
        return 1  # one pair
    else:
        return 0  # high


# check_hand("T55J5")


# print(hands)
for i in range(len(hands)):
    for j in range(i + 1, len(hands)):
        if check_hand(hands[i][0]) > check_hand(hands[j][0]):
            hands[i], hands[j] = hands[j], hands[i]
        elif check_hand(hands[i][0]) == check_hand(hands[j][0]):
            if comp_hand(hands[i][0], hands[j][0]):
                hands[i], hands[j] = hands[j], hands[i]
        else:
            pass
# print(hands)

res = 0
for i, v in enumerate(hands):
    res += (i + 1) * v[1]
print(res)
