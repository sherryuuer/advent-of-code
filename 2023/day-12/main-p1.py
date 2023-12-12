# recurion
lines = open(r'2023/day-12/testinput.txt').read().strip().splitlines()

for line in lines:
    springs, nums = line.split(' ')
    nums = tuple(map(int, nums.split(',')))
    print(springs)
    print(nums)
