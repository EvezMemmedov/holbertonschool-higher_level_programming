#!/usr/bin/python3
"""
this module retur true or false
"""


def inherits_from(obj, a_class):
    """
    that return type

    Prototype:def is_same_class(obj, a_class):
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
