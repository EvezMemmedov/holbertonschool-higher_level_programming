#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """that is Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list):
            filtered = {}
            for i in attrs:
                if i in self.__dict__:
                    filtered[i]= self.__dict__[i]

            return filtered
        else:
            return self.__dict__
