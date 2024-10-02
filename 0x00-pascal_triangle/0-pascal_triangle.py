#!/usr/bin/python3
'''
Module to define function for Pascal's triangle
'''


def pascal_triangle(n):
    '''
    Function to return pascal's triangle
    '''
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n-1)
        last_row = triangle[-1]
        new_row = []
        for i in range(n):
            if i == 0 or i == n - 1:
                new_row.append(1)
            else:
                new_row.append(last_row[i-1]+last_row[i])
        triangle.append(new_row)
        return triangle
