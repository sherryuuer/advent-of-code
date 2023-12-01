number_strs = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
# take the input as data list
with open("2023\day-01\input.txt") as f:
    data = f.readlines()

# print(type(data))
# print(data[:10])

# remove the \n mark
str_list = []
for string in data:
    new_str = string.rstrip("\n")
    str_list.append(new_str)


def first_number(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]
        else:
            for key in number_strs:
                if string[i:].startswith(key):
                    return number_strs[key]


def last_number(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i].isdigit():
            return string[i]
        else:
            for key in number_strs:
                if string[:i+1].endswith(key):
                    return number_strs[key]


def get_num(string):
    first = first_number(string)
    last = last_number(string)
    # print(first)
    # print(last)
    return int(first + last)


# init total = 0
total = 0
for string in str_list:
    print(string)
    num = get_num(string)
    total += num

print(total)
