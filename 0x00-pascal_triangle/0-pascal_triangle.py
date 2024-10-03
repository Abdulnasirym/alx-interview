#!/usr/bin/python3
"""
Pascal's Triangle
A module for generating Pascal's triangle up to n rows.
"""

def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing the triangle.
              Returns an empty list if n is not a positive integer.
    """
    triangle = []
    
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return triangle
    
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    
    return triangle
