#!/usr/bin/python3
"""
This module defines the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    Width and height are positive integers validated by integer_validator
    """
    def __init__(self, width, height):
        """Initializer of rectangle

        Arguments:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
