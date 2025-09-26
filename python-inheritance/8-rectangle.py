#!/usr/bin/python3
"""
This module defines the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
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
