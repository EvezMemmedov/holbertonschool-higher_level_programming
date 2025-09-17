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
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initialize a new Square.
        Args:
            size: initial size of the square (no type/value checks).
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """
        this module return area
        """
        return self.__size * self.__size
