#!/usr/bin/python3
"""script that post the email"""
import sys
import requests


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=email)

    print(req.text)
