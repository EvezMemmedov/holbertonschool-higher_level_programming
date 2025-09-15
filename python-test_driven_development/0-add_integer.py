#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""
def add_integer(a, b=98):
    """
    add two integer
    args:
        a first number
        b second number
    return:
        sum of a and b
    raises:
        typeError if a or b not integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
