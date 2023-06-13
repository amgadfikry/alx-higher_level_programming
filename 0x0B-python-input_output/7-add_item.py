#!/usr/bin/python3
""" module that add args to file"""
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file
li = []
try:
    li.extend(load("add_item.json"))
except FileNotFoundError:
    pass
li.extend(sys.argv[1:])
save(li, "add_item.json")
