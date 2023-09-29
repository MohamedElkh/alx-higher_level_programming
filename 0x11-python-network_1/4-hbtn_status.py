#!/usr/bin/python3
"""python script fetch url with req pack"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    tx = req.text

    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(tx), tx))
