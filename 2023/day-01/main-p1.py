import re
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
# print(str_list)


# need first number search from index 0
# need second number search from index -1
# conbinate the nums and turn them into num
# add to the sum
def get_number(string):
    # get number
    numbers = re.findall(r'\d+', string)
    first = numbers[0][0]
    second = numbers[-1][-1]
    num = int(first + second)
    return num


# init total = 0
total = 0
for string in str_list:
    num = get_number(string)
    total += num

print(total)
