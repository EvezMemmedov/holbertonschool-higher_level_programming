#!/usr/bin/python3
"""
this module print first amd last name
"""


def say_my_name(first_name, last_name=""):
    """
    print My name is <first name> <last name>
    args:
        first_name is first sitring
        last_name is second sitrings
    return:
        first and last name
    raise:
        TypeError if first_name and last_name not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
