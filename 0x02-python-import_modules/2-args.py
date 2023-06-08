#!/usr/bin/python3
if __name__ == '__main__'
    import sys
    num_len = len(sys:argv)
    if num_len == 1:
         print("{:d} arguments.".format(num_len - 1))
     elif num_len == 2:
         print("{:d} argument:".format(num_len - 1))
     else:
          print("{:d} arguments:".format(num_len - 1))

          for x in range(1, num_len):
              print("{:d}: {:s}".format(x, sys.argv[x]))
