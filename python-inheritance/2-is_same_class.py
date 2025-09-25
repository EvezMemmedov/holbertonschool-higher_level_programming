#!/usr/bin/python3
"""
this module retur true or false
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or
    an instance of a class that inherited from a_class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
