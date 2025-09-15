#!/usr/bin/python3
def add_integer(a, b=98):
    a = int(a)
    b = int(b)
    try:
        result = a + b
    except TypeError:
        print("a must be an integer")
    return result
