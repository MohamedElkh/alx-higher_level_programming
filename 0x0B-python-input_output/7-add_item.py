#!/usr/bin/python3
""" define the model sys """
from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    json_file = load_from_json_file('add_item.json')
else:
    json_file = []

for x in range(1, len(argv)):
    json_file.append(argv[x])

save_to_json_file(json_file, 'add_item.json')
