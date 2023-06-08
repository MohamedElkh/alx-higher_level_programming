#!/usr/bin/python3

from sys import argv
x = 1
r = 0

if __name__ == '__main__':
    while x < len(argv):
        r += int(argv[x])
        x += 1
    print(r)
