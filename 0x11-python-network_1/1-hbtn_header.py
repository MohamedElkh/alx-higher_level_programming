#!/usr/bin/python3
"""script that takes the url and send a req to url"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
