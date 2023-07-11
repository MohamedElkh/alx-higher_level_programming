#!/usr/bin/python3
""" define the model sys """


import sys

if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        nums = load_from_json_file("add_item.json")
    except FileNotFoundError:
        it = []
    it.extend(sys.argv[1:])
    save_to_json_file(it, "add_item.json")
