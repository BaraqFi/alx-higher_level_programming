#!/usr/bin/python3

"""
Takes an argument and searchs the entire
database for that argument taken in
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` \
            WHERE name LIKE BINARY '{}' ORDER \
            BY id ASC".format(sys.argv[4]))
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()

