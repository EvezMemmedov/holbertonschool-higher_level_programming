#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}
    for idx in range(len(roman_string)):
        value = values[roman_string[idx]]
        if idx + 1 < len(roman_string) and value < values[roman_string[idx + 1]]:
            total -= values
        else:
            total += values
    return total
