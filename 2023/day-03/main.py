def check_num(grid, row, col):
    return (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or not grid[row][col].isdigit())


grid = open(r"2023/day-03/input.txt").read().splitlines()

# p1
first_num_list_p1 = set()
for ridx, row in enumerate(grid):
    for cidx, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue

        for char_row in [ridx - 1, ridx, ridx + 1]:
            for char_col in [cidx - 1, cidx, cidx + 1]:
                if check_num(grid, char_row, char_col):
                    continue

                while char_col > 0 and grid[char_row][char_col - 1].isdigit():
                    char_col -= 1
                first_num_list_p1.add((char_row, char_col))

num_list = []
for (row, col) in first_num_list_p1:
    string = ""
    while col < len(grid[row]) and grid[row][col].isdigit():
        string += grid[row][col]
        col += 1
    num_list.append(int(string))

print(sum(num_list))


# p2
total = 0
for ridx, row in enumerate(grid):
    for cidx, char in enumerate(row):
        if char != "*":
            continue

        first_num_list_p2 = set()
        for char_row in [ridx - 1, ridx, ridx + 1]:
            for char_col in [cidx - 1, cidx, cidx + 1]:
                if check_num(grid, char_row, char_col):
                    continue

                while char_col > 0 and grid[char_row][char_col - 1].isdigit():
                    char_col -= 1
                first_num_list_p2.add((char_row, char_col))

        if len(first_num_list_p2) != 2:
            continue

        num_list = []
        for (row, col) in first_num_list_p2:
            string = ""
            while col < len(grid[row]) and grid[row][col].isdigit():
                string += grid[row][col]
                col += 1
            num_list.append(int(string))

        total += num_list[0] * num_list[1]
print(total)
