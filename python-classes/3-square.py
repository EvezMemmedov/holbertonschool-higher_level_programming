#!/usr/bin/python3
"""
this module defien square class
"""


class Square:
    """
    Represents a square.
    Private instance attribute:
        __size
    """
    def __init__(self, size=0):
        """
        Initialize a new Square.
        Args:
            size: initial size of the square (no type/value checks).
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):

        """
        this module return area
        """
        return self.__size * self.__size
