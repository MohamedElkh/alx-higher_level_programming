#!/usr/bin/python3
"""
script that takes in an argument and displays all values
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curr = db.cursor()
    curr.execute("SELECT * FROM states \
                  WHERE CONVERT(`name` USING Latin1) \
                  COLLATE Latin1_General_CS = '{}';"
                  .format(sys.argv[4]))

    states = curr.fetchall()

    for st in states:
        print(st)
