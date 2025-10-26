#!/usr/bin/python3


"""
that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=database,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c\
        LEFT JOIN states AS s ON c.state_id=s.id\
        ORDER BY c.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
