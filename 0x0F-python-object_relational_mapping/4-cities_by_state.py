#!/usr/bin/python3
"""Lists all cities with states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="{}".format(argv[1]),
                         passwd="{}".format(argv[2]),
                         db="{}".format(argv[3]), port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities INNER JOIN states ON cities.state_id = states.id")
    selects = cur.fetchall()
    for i in selects:
        print("{}".format(i))
    cur.close()
    db.close()
