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
        new_row = [0] * n
        even = n % 2 == 0
        middle = int(n / 2) if even else (n // 2) + 1
        for i in range(middle):
            if i == 0:
                new_row[i] = 1
            else:
                value = last_row[i-1]+last_row[i]
                if even or i != middle:
                    new_row[i] = new_row[n - i - 1] = value
        new_row[-1] = 1
        triangle.append(new_row)
        return triangle
