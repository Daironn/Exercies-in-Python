grid = [['.','.','.','.','.','.','.'],
        ['.','0','0','.','.','.','.'],
        ['0','0','0','0','.','.','.'],
        ['0','0','0','0','0','0','.'],
        ['.','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','.'],
        ['0','0','0','0','.','.','.'],
        ['.','0','0','.','.','.','.'],
        ['.','.','.','.','.','.','.']]

for y in range(0,7):
    for x in range(0,9):
        print(grid[x][y], end='')
    print()