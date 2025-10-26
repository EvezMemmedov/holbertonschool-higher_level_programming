#!/usr/bin/python3


"""
Takes in arguments and displays all values in the states table
where name matches the given argument (safe from MySQL injection).
"""


import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=database,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
     WHERE BINARY name = %s ORDER BY id ASC", (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
