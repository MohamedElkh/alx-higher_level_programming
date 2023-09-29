#!/usr/bin/python3
"""script takes url and send post req to url"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
