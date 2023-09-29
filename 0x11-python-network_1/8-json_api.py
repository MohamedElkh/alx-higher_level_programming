#!/usr/bin/python3
"""script that takes in letter and send request"""
import sys
import requests


if __name__ == "__main__":
    lett = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": lett}
    req = requests.post("http://0.0.0.0:5000/search_user", data=load)

    try:
        resp = req.json()

        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))

    except ValueError:
        print("Not a valid JSON")
