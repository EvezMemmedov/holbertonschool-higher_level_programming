#!/usr/bin/python3
"""dictionary description with simple data structure"""


import json


def class_to_json(obj):
    """that returns the dictionary"""
    return obj.__dict__
