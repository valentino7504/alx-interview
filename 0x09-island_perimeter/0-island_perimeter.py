#!/usr/bin/python3
'''

Island perimeter module

'''


def check_val(val):
    '''checks if a value is 1 or 0'''
    return val == 0


def island_perimeter(grid):
    '''checks island perimeter'''
    row = len(grid)
    col = len(grid[0])
    val = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i - 1 < 0:
                    val += 1
                else:
                    val += check_val(grid[i - 1][j])
                if j - 1 < 0:
                    val += 1
                else:
                    val += check_val(grid[i][j - 1])
                try:
                    val += check_val(grid[i + 1][j])
                except IndexError:
                    val += 1
                try:
                    val += check_val(grid[i][j + 1])
                except IndexError:
                    val += 1
    return val
