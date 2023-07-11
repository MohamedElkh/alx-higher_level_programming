#!/usr/bin/python3
""" define the model json """
import json


def save_to_json_file(my_obj, filename):
    """ function object to text file """
    with open(filename, "w") as fl:
        json.dumb(my_obj, fl)
