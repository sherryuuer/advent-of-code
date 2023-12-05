card_dict = {'1': 4, '2': 2, '3': 2, '4': 1, '5': 0, '6': 0}
process = [card_dict.copy()]


def append_cards_dict(current_dict, original_dict):
    max_len = len(original_dict)

    for k, v in current_dict.items():
        new_dict = {}
        if v == 0:
            continue
        if int(k) + 1 > max_len:
            continue
        start = int(k) + 1
        end = int(k) + 1 + v
        if end > max_len:
            end = max_len + 1
        for i in range(start, end):
            new_dict[str(i)] = original_dict[str(i)]
        process.append(new_dict)
    return process


result = 0
while process:
    current_dict = process.pop(0)
    result += len(current_dict)
    process = append_cards_dict(current_dict, card_dict)
    print(process)

print(result)
