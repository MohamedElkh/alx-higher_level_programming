#!/usr/bin/python3
def uppercase(str):
    d_str =""
    for x in range(len(str)):
        if (ord(str[x]) >= 97 and ord(str[x]) <= 122):
            d_str += chr(ord(str[x]) - 32)
            continue
        d_str += str[x]
print('{0}'.format(d_str))
