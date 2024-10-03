#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function that returns a list of lists
    of integers representing Pascal’s triangle of n rows.
    
    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []  # Return empty list for non-positive integers

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the completed row to the triangle

    return triangle
