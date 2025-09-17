#!/usr/bin/python3
"""
This module defien a squere class
"""


class Square:
    """
    Represents a square.
    Private instance attribute:
        __size
    """
    def __init__(self, size):
        """
        Initialize a new Square.
        Args:
            size: initial size of the square (no type/value checks).
        """
        self.__size = size
