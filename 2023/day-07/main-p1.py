with open(r'2023/day-07/testinput.txt') as f:
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
    if char == 'J':
        return 11
    if char == 'T':
        return 10


def comp_hand(hand1, hand2):
    pass


def check_hand(hand):
    # hand likes "32T3K"
    # hands.keys()
    # return type, level
    charl = {}
    for c in hand:
        if c not in charl:
            charl[c] = 1
        charl[c] += 1

    if len(charl) == 1:
        return "five", 6
    elif len(charl) == 2:
        if min(charl.values()) == 1:
            return "four", 5
        else:
            return "full", 4
    elif len(charl) == 3:
        if max(charl.values()) == 3:
            return "three", 3
        else:
            return "twop", 2
    elif len(charl) == 4:
        return "onep", 1
    else:
        return "high", 0


for hand in hands:
    type, level = check_hand(hand[0])
    hand.append(level)


print(hands)
