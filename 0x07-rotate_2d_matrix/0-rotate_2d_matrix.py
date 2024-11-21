#!/usr/bin/python3
""" A python file that transpose a 2D matrix"""


def rotate_2d_matrix(matrix):
    """ Function that rotates a matrix """
    n = len(matrix)

    """ Reverse each column of the matrix """
    for i in range(n):
        for j in range(n // 2):
            (matrix[j][i], matrix[n - j - 1][i]) = (
                matrix[n - j - 1][i], matrix[j][i]
            )

    """ Performing Transpose """
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
