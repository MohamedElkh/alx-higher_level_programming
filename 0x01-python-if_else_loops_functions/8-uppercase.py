#!/usr/bin/python3
def uppercase(str):
   for x in range(len(str)):
       if ord(str[x]) >= 97 and ord(str[x]) <= 122:
           number = 32
       else:
           number = 0

           print("{:c}".format(ord(str[x]) - number, end="")
           print()

