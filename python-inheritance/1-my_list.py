#!/usr/bin/python3
"""
this module prunt list
"""


class MyList(list):
    """
    that prints the list, but sorted

    Prototyp: def print_sorted(self):
    """
    def print_sorted(self):
        x = sorted(self)
        print(x)
