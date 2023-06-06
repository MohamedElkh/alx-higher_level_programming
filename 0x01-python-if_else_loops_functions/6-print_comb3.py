#!/usr/bin/python3
for x in range(10):
    for v in range(10):
        if (x != v and x < v) and x < 9:
            if (x == 8 and v == 9):
                print('{0}{1}'.format(x, v))
            else:
                print('{0}{1}, '.format(x, v), end='')
