#!/usr/bin/python3
"""
do list all cities if the state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curr = db.cursor()
    curr.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{}';".format(sys.argv[4]))

    stat = curr.fetchall()

    print(", ".join([st[1] for st in stat]))
