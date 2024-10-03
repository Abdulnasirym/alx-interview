#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    triangle = [[1]]
    if n <= 0 or type(n) is not int:
        return []
    for i in range(1, n):
        row = [1]
        
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle