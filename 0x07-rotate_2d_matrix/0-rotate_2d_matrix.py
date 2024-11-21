#!/usr/bin/python3
'''

Rotate 2d matrix

'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix'''
    matrix = [[matrix[j][i] for j in range(len(matrix))]
              for i in range(len(matrix[0]))]
    matrix = [row[::-1] for row in matrix]
