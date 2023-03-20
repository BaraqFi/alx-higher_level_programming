#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(user=mysql_user,
                         passwd=mysql_pwd,
                         db=db_name,
                         port=3306,
                         host='localhost')

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
                .format(search_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
