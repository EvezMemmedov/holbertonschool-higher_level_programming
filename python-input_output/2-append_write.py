#!/usr/bin/python3
"""that append text file"""


def append_write(filename="", text=""):
    """return append file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
