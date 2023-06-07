#!/usr/bin/python3
def uppercase(str):
   for c in str:
       if ord(c) >= 65 and ord(c) <= 90:
           c = chr(ord(c))
           print(f"{c}", end="")
           print("")

