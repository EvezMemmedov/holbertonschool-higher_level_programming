#!/usr/bin/python3


"""
that takes in the name of a state as an argument
and lists all cities of that state
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
    cur.execute("SELECT c.name FROM cities AS c\
        LEFT JOIN states AS s ON c.state_id=s.id\
        WHERE BINARY s.name = %s\
        ORDER BY c.id ASC", (argv[4]),)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
