#!/usr/bin/env python3

'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
'''

from pprint import pprint

def rotate_matrix(matrix):
    # reverse matrix rows then transpose
    return [list(x) for x in [*zip(*matrix[::-1])]]

def rotate_matrix_1(matrix):
    n = len(matrix)
    out = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = matrix[n - j - 1][i]
    return out

def make_matrix(n):
    matrix = [[0]*5 for i in range(5)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = (i * n + j)
    return matrix

if __name__ == '__main__':
    n = 5
    m = make_matrix(n)
    pprint(m)
    pprint(rotate_matrix(m))
    pprint(m)
