#!/usr/bin/python3
"""that adds all arguments to a Python list"""


import sys
import json
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    load_from_json_file(filename)
else:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
