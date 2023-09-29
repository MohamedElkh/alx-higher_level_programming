#!/usr/bin/python3
"""script takes url and send req to url """


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as rs:
            print(rs.read().decode('UTF-8'))

    except error.HTTPError as err:
        print("Error code:", err.code)
