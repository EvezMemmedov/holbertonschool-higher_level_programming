#!/usr/bin/python3
"""
This module defines a Square class with size and position.
"""

class Square:
    """
    Represents a square.
    Private instance attributes:
        __size
        __position
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type and value checks."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, considering position."""
        if self.size == 0:
            print()
            return

        # print empty lines for vertical offset
        for _ in range(self.position[1]):
            print()

        # print each line of the square
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
