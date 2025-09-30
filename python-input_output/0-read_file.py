#!/usr/bin/python3
"""
Module for reading text files and printing their contents to stdout.
"""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
