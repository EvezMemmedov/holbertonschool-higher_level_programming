#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers or floats
        div (int or float): The number to divide each element by

    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if matrix is empty
    if not matrix or not all(row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create new matrix with divided elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    
    return new_matrix
