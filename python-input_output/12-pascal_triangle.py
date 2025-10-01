#!/usr/bin/python3
"""that returns a list of lists of integers"""


def pascal_triangle(n):
    """Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prew_row = triangle[i-1]
        row = [1]
        for j in range(1, i):
            row.append(prew_row[j-1] + prew_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
