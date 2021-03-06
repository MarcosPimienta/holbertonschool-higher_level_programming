#!/usr/bin/python3
"""Lists all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="{}".format(argv[1]),
                         passwd="{}".format(argv[2]),
                         db="{}".format(argv[3]), port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name = %s\
                 ORDER BY id", (argv[4],))
    selects = cur.fetchall()
    for i in selects:
        print("{}".format(i))
    cur.close()
    db.close()
