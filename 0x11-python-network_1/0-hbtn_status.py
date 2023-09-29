#!/usr/bin/python3
""" script that fetchs https://alx-intranet.hbtn.io/status."""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        con = resp.read()

        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content: {}".format(con))
        print("\t- utf8 content: {}".format(con.decode('utf-8')))
