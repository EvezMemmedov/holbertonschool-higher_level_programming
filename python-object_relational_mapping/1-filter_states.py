#!/usr/bin/python3
"""1-filter_states

Select all states starting with 'N' from database on localhost:3306
Accepts username, password and database as argv
"""


import MySQLdb
import sys


if __name__ == '__main__':
    connct = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwod=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = connct.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connct.close()
