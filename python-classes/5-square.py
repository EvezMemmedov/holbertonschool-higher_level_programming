#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Represents a square.
    Private instance attribute:
        __size
    """
    def __init__(self, size=0):
        """Initialize a new Square with optional size."""
        self.size = size
    
    @property
    def size(self):
        """
        Retrieve the size of the square.
        """
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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        this module return area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        this prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
