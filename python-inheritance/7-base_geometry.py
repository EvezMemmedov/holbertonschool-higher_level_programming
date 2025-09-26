#!/usr/bin/python3
"""
this module create an empty Square class
"""


class BaseGeometry:
    """
    This is an empty class that defines a square.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
