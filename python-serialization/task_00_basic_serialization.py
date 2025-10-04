#!/usr/bin/python3
"""that adds the functionality to serialize
 a Python dictionary to a JSON file 
and deserialize the JSON file to recreate the Python Dictionary."""


import json


def serialize_and_save_to_file(data, filename):
    """that metod fix data"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """return result"""
    with open(filename, "r", encoding="utf-8") as f:
        result = json.load(f)
        return result
