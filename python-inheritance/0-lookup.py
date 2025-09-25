#!/usr/bin/python3
"""
this module return attributes and methods
"""


def lookup(obj):
    """
    Return a list of the available attributes and methods of an object.

    Prototype: def lookup(obj):
    Returns: list
    """
    return dir(obj)
